// Logo Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/logo-detection

const HOST = "logos-detection.p.rapidapi.com";
const URL = `https://${HOST}/detect-logo`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-macbook.jpg" }),
});

const data = await response.json();
data.body.logos.forEach(l => console.log(`  ${l.description}: ${l.score.toFixed(3)}`));
