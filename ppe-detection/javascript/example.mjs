// PPE Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/ppe-detection

const HOST = "ppe-detection1.p.rapidapi.com";
const URL = `https://${HOST}/detect-ppe`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/construction.jpg" }),
});

const data = await response.json();
data.body.Persons.forEach(p => console.log(`  Head: ${JSON.stringify(p.HeadCover)}, Face: ${JSON.stringify(p.FaceCover)}`));
