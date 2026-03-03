// Mask Detection API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/mask-detection

const HOST = "mask-detection2.p.rapidapi.com";
const URL = `https://${HOST}/detect-mask`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg" }),
});

const data = await response.json();
const summary = data.body.Summary;
console.log("With mask:", summary.PersonsWithMask);
console.log("Without mask:", summary.PersonsWithoutMask);
