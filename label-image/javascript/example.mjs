// Label Image API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/label-image

const HOST = "label-image.p.rapidapi.com";
const URL = `https://${HOST}/detect-label`;

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
data.body.labels.forEach(l => console.log(`  ${l.description}: ${l.score.toFixed(3)}`));
