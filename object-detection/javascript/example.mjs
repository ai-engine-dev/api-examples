// Object Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/object-detection

const HOST = "objects-detection.p.rapidapi.com";
const URL = `https://${HOST}/objects-detection`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/birds.jpeg" }),
});

const data = await response.json();
data.body.labels.forEach(obj => console.log(`  ${obj.Name}: ${obj.Confidence.toFixed(1)}%`));
