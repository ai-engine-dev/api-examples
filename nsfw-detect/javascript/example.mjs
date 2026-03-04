// NSFW Detect API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/nsfw-detect

const HOST = "nsfw-detect3.p.rapidapi.com";
const URL = `https://${HOST}/nsfw-detect`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/violence.jpeg" }),
});

const data = await response.json();
const labels = data.body.ModerationLabels;
if (labels.length) {
  labels.forEach(l => console.log(`  ${l.Name}: ${l.Confidence.toFixed(1)}%`));
} else {
  console.log("  Image is safe");
}
