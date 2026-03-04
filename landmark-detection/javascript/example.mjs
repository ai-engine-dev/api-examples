// Landmark Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/landmark-detection

const HOST = "landmarks-detection.p.rapidapi.com";
const URL = `https://${HOST}/detect-landmarks`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-david-vives-2846896.jpg" }),
});

const data = await response.json();
data.body.landmarks.forEach(lm => {
  const loc = lm.locations[0] || {};
  console.log(`  ${lm.description} (${lm.score.toFixed(2)}) — ${loc.latitude}, ${loc.longitude}`);
});
