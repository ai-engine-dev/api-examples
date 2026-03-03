// Landmark Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/landmark-detection

const HOST = "landmarks-detection.p.rapidapi.com";
const URL = `https://${HOST}/detect-landmarks`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/landmark.jpg" }),
});

const data = await response.json();
data.body.landmarks.forEach(lm => {
  const loc = lm.locations[0] || {};
  console.log(`  ${lm.description} (${lm.score.toFixed(2)}) — ${loc.latitude}, ${loc.longitude}`);
});
