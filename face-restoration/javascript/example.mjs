// Face Restoration API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/face-restoration

const HOST = "face-restoration.p.rapidapi.com";
const URL = `https://${HOST}/submit`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ image_url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg" }),
});

const data = await response.json();
const jobId = data.jobId;
console.log("Job submitted:", jobId);
console.log("Poll GET /result?jobId=" + jobId + " until status is done");
