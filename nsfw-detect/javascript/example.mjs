// NSFW Detect API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/nsfw-detect

const HOST = "nsfw-detect3.p.rapidapi.com";
const URL = `https://${HOST}/nsfw-detect`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/street.jpg" }),
});

const data = await response.json();
const labels = data.body.ModerationLabels;
if (labels.length) {
  labels.forEach(l => console.log(`  ${l.Name}: ${l.Confidence.toFixed(1)}%`));
} else {
  console.log("  Image is safe");
}
