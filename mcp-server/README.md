# AI Engine MCP Server

An [MCP](https://modelcontextprotocol.io) server that gives AI assistants like Claude and Cursor tools to edit and read images with the [AI Engine](https://ai-engine.net?utm_source=github&utm_medium=referral&utm_campaign=mcp-server) APIs:

- remove the background of a photo and save a transparent PNG
- put the subject on a solid color or blur the background
- read the text in images and scanned PDFs (OCR)
- check an image for nudity or violence before publishing it

Ask your assistant things like *"remove the background of every photo in ./products and put them on white"* or *"read invoice.pdf and list the totals"*, and it calls these tools for you.

## Tools

| Tool | What it does | API |
|------|--------------|-----|
| `remove_background` | Transparent PNG cutout | [Background Removal](https://ai-engine.net/apis/background-removal?utm_source=github&utm_medium=referral&utm_campaign=mcp-server) |
| `color_background` | Replace the background with a color (`#FFFFFF` by default) | Background Removal |
| `blur_background` | Keep the subject sharp, blur the rest | Background Removal |
| `extract_text` | Text of an image, optionally every word with its box | [OCR Wizard](https://ai-engine.net/apis/ocr-wizard?utm_source=github&utm_medium=referral&utm_campaign=mcp-server) |
| `extract_pdf_text` | Text of a PDF, page by page, 10 pages per call | OCR Wizard |
| `check_nsfw` | Moderation labels and a `safe` flag | [NSFW Detect](https://ai-engine.net/apis/nsfw-detect?utm_source=github&utm_medium=referral&utm_campaign=mcp-server) |

Images can be a local path or a public URL. Edited images are saved next to the input as `<name>_nobg.png`, `<name>_color.png` or `<name>_blur.png`, unless you give an `output_path`.

## Get a key

The tools call the APIs on RapidAPI. You need one RapidAPI key and a subscription to each API you want to use:

1. Create a free account on [RapidAPI](https://rapidapi.com).
2. Open the API pages and click **Subscribe to Test**. Each API has a free plan:
   - [Background Removal](https://rapidapi.com/ai-engine-ai-engine-default/api/background-removal-ai) for `remove_background`, `color_background` and `blur_background`
   - [OCR Wizard](https://rapidapi.com/ai-engine-ai-engine-default/api/ocr-wizard) for `extract_text` and `extract_pdf_text`
   - [NSFW Detect](https://rapidapi.com/ai-engine-ai-engine-default/api/nsfw-detect3) for `check_nsfw`
3. Copy your key: on any of these pages, open the **Endpoints** tab, the key is the value of the `X-RapidAPI-Key` header in the code snippet.

The same key works for all three APIs. A tool whose API you did not subscribe to returns an error, the others keep working.

Replace `your_key` in the commands below with this key.

## Install

You need [uv](https://docs.astral.sh/uv/getting-started/installation/). `uvx` downloads and runs the server, nothing else to install.

### Claude Code

```bash
claude mcp add ai-engine -e RAPIDAPI_KEY=your_key -- \
  uvx --from "git+https://github.com/ai-engine-dev/api-examples#subdirectory=mcp-server" ai-engine-mcp
```

### Claude Desktop

Add this to `claude_desktop_config.json` (Settings > Developer > Edit Config) and restart Claude:

```json
{
  "mcpServers": {
    "ai-engine": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/ai-engine-dev/api-examples#subdirectory=mcp-server",
        "ai-engine-mcp"
      ],
      "env": { "RAPIDAPI_KEY": "your_key" }
    }
  }
}
```

### Cursor

Same block in `~/.cursor/mcp.json` (or `.cursor/mcp.json` in a project).

### From a clone

```bash
git clone https://github.com/ai-engine-dev/api-examples.git
cd api-examples/mcp-server
pip install .
RAPIDAPI_KEY=your_key ai-engine-mcp
```

## Example

In Claude Code, in a folder with `shirt.jpg`:

```text
> Remove the background of shirt.jpg, then check whether shirt.jpg is safe to publish.

Background removed: saved as shirt_nobg.png (900x1200 transparent PNG) next to the original.
Safety check: shirt.jpg came back safe to publish, with no nudity, violence or other unsafe content flagged.
```

## Keep your key private

- The server reads the key from the `RAPIDAPI_KEY` environment variable and sends it only to RapidAPI. It is never written to disk or returned to the assistant.
- Never commit a config file that contains your key. `claude mcp add` stores it in your user config (`~/.claude.json`), not in your project. Claude Desktop keeps it in `claude_desktop_config.json` on your machine. In Cursor, prefer the global `~/.cursor/mcp.json` over a project file.
- To share a setup with your team, commit a `.mcp.json` that references the variable instead of the key, and let each person export their own `RAPIDAPI_KEY`:

```json
{
  "mcpServers": {
    "ai-engine": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/ai-engine-dev/api-examples#subdirectory=mcp-server", "ai-engine-mcp"],
      "env": { "RAPIDAPI_KEY": "${RAPIDAPI_KEY}" }
    }
  }
}
```

- If a key leaks, regenerate it in your RapidAPI dashboard (Apps > your app > Authorization) and update your config.

## Notes

- `extract_pdf_text` reads 10 pages per call. When there are more, the result has `next_first_page`, and the assistant calls it again.
- Python 3.10 or newer.

## License

MIT
