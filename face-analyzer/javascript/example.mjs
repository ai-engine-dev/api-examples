// Face Analyzer API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/face-analyzer

const HOST = "faceanalyzer-ai.p.rapidapi.com";
const URL = `https://${HOST}/faceanalysis`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/main/assets/samples/face.jpg" }),
});

const data = await response.json();
data.body.faces.forEach(f => console.log(`  Age: ${JSON.stringify(f.AgeRange)}, Gender: ${JSON.stringify(f.Gender)}`));
