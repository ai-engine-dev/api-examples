"""MCP server for the AI Engine image APIs (background removal, OCR, NSFW detection)."""

import os
from pathlib import Path

import requests
from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

BG_HOST = "background-removal-ai.p.rapidapi.com"
OCR_HOST = "ocr-wizard.p.rapidapi.com"
NSFW_HOST = "nsfw-detect3.p.rapidapi.com"
TIMEOUT = 120

mcp = MCPServer(
    name="ai-engine",
    instructions=(
        "Image tools from AI Engine. Pass a local file path or a public http(s) URL as `image`. "
        "Use remove_background for transparent PNG cutouts, extract_text and extract_pdf_text "
        "to read text from images and scanned PDFs, and check_nsfw before publishing an image."
    ),
    website_url="https://ai-engine.net",
)


def _headers(host):
    key = os.environ.get("RAPIDAPI_KEY")
    if not key:
        raise ToolError("Set the RAPIDAPI_KEY environment variable to your RapidAPI key.")
    return {"x-rapidapi-host": host, "x-rapidapi-key": key}


def _is_url(value):
    return value.startswith(("http://", "https://"))


def _local(path):
    p = Path(path).expanduser().resolve()
    if not p.is_file():
        raise ToolError(f"File not found: {p}")
    return p


def _post(host, endpoint, image, url_field, file_field="image", extra=None, as_json=False):
    """Send a local file as multipart, or a URL in `url_field`."""
    url = f"https://{host}/{endpoint}"
    headers = _headers(host)
    extra = extra or {}
    if _is_url(image):
        payload = {url_field: image, **extra}
        if as_json:
            r = requests.post(url, headers=headers, json=payload, timeout=TIMEOUT)
        else:
            r = requests.post(url, headers=headers, data=payload, timeout=TIMEOUT)
    else:
        with open(_local(image), "rb") as f:
            r = requests.post(url, headers=headers, files={file_field: f}, data=extra, timeout=TIMEOUT)
    if r.status_code != 200:
        raise ToolError(f"{endpoint} failed with HTTP {r.status_code}: {r.text[:300]}")
    return r.json()


def _output_path(image, output_path, suffix):
    if output_path:
        return Path(output_path).expanduser().resolve()
    stem = Path(image.split("?")[0]).stem or "image"
    base = Path.cwd() if _is_url(image) else _local(image).parent
    return base / f"{stem}_{suffix}.png"


def _save_result(data, image, output_path, suffix):
    out = _output_path(image, output_path, suffix)
    out.parent.mkdir(parents=True, exist_ok=True)
    png = requests.get(data["image_url"], timeout=TIMEOUT)
    png.raise_for_status()
    out.write_bytes(png.content)
    return {"saved_to": str(out), "image_url": data["image_url"],
            "width": data.get("width"), "height": data.get("height")}


def _rgba(color):
    """Accept '#RRGGBB', '#RRGGBBAA' or 'R,G,B[,A]' and return 'R,G,B,A'."""
    c = color.strip()
    if c.startswith("#"):
        h = c[1:]
        if len(h) not in (6, 8):
            raise ToolError("Use #RRGGBB or #RRGGBBAA")
        parts = [int(h[i:i + 2], 16) for i in range(0, len(h), 2)]
    else:
        try:
            parts = [int(p) for p in c.split(",")]
        except ValueError:
            raise ToolError("Color must be #RRGGBB or R,G,B,A with values 0-255")
    if len(parts) == 3:
        parts.append(255)
    if len(parts) != 4 or not all(0 <= p <= 255 for p in parts):
        raise ToolError("Color must be #RRGGBB or R,G,B,A with values 0-255")
    return ",".join(map(str, parts))


@mcp.tool()
def remove_background(image: str, output_path: str | None = None) -> dict:
    """Remove the background of a photo and save a transparent PNG.

    Args:
        image: Local file path or public http(s) URL of the image.
        output_path: Where to save the PNG. Default: <name>_nobg.png next to the input
            (or in the current directory for URLs).
    """
    data = _post(BG_HOST, "remove-background", image, "image_url", as_json=True)
    return _save_result(data, image, output_path, "nobg")


@mcp.tool()
def color_background(image: str, color: str = "#FFFFFF", output_path: str | None = None) -> dict:
    """Replace the background with a solid color, for example white for product photos.

    Args:
        image: Local file path or public http(s) URL of the image.
        color: '#RRGGBB', '#RRGGBBAA' or 'R,G,B,A'. Default white.
        output_path: Where to save the PNG. Default: <name>_color.png.
    """
    data = _post(BG_HOST, "color-background", image, "image_url",
                 extra={"bg_color": _rgba(color)}, as_json=True)
    return _save_result(data, image, output_path, "color")


@mcp.tool()
def blur_background(image: str, blur_radius: int = 15, output_path: str | None = None) -> dict:
    """Keep the subject sharp and blur the background (portrait effect).

    Args:
        image: Local file path or public http(s) URL of the image.
        blur_radius: Blur strength in pixels. Default 15.
        output_path: Where to save the PNG. Default: <name>_blur.png.
    """
    data = _post(BG_HOST, "blur-background", image, "image_url",
                 extra={"blur_radius": blur_radius}, as_json=True)
    return _save_result(data, image, output_path, "blur")


@mcp.tool()
def extract_text(image: str, include_words: bool = False) -> dict:
    """Read the text in an image (photo, screenshot, receipt, scanned page).

    Args:
        image: Local file path or public http(s) URL of the image.
        include_words: Also return every word with its bounding box (pixel coordinates).
    """
    body = _post(OCR_HOST, "ocr", image, "url")["body"]
    result = {"text": body.get("fullText", ""), "language": body.get("detectedLanguage")}
    if include_words:
        result["words"] = [{"text": w["text"], "box": w["boundingPoly"]}
                           for w in body.get("annotations", [])]
    return result


@mcp.tool()
def extract_pdf_text(pdf_path: str, first_page: int = 1, last_page: int = 10) -> dict:
    """Read the text of a scanned or digital PDF, page by page (up to 10 pages per call).

    Args:
        pdf_path: Local path of the PDF file.
        first_page: First page to read (1-based).
        last_page: Last page to read. At most first_page + 9; call again for the next pages.
    """
    if last_page < first_page:
        raise ToolError("last_page must be >= first_page")
    last_page = min(last_page, first_page + 9)
    host = OCR_HOST
    with open(_local(pdf_path), "rb") as f:
        r = requests.post(f"https://{host}/ocr-pdf", headers=_headers(host), files={"pdf_file": f},
                          data={"first_page": first_page, "last_page": last_page}, timeout=TIMEOUT)
    if r.status_code != 200:
        raise ToolError(f"ocr-pdf failed with HTTP {r.status_code}: {r.text[:300]}")
    body = r.json()["body"]
    pages = body if isinstance(body, list) else body.get("pages", [])
    return {"pages": [{"page": first_page + i, "text": p.get("fullText", ""),
                       "language": p.get("detectedLanguage")} for i, p in enumerate(pages)],
            "next_first_page": first_page + len(pages) if len(pages) == last_page - first_page + 1 else None}


@mcp.tool()
def check_nsfw(image: str) -> dict:
    """Check an image for nudity, violence and other unsafe content before publishing it.

    Args:
        image: Local file path or public http(s) URL of the image.
    """
    body = _post(NSFW_HOST, "nsfw-detect", image, "url")["body"]
    labels = [{"name": l["Name"], "parent": l.get("ParentName", ""),
               "confidence": round(l["Confidence"], 1)} for l in body.get("ModerationLabels", [])]
    return {"safe": not labels, "labels": labels}


def main():
    mcp.run()


if __name__ == "__main__":
    main()
