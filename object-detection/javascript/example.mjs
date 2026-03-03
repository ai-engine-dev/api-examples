// Object Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/object-detection

const HOST = "objects-detection.p.rapidapi.com";
const URL = `https://${HOST}/objects-detection`;

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
data.body.labels.forEach(obj => console.log(`  ${obj.Name}: ${obj.Confidence.toFixed(1)}%`));
