// Face Restoration API: JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/face-restoration

const HOST = "face-restoration.p.rapidapi.com";
const URL = `https://${HOST}/enhance-face`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ image_url: "https://openmediadata.s3.eu-west-3.amazonaws.com/face_restoration_api_demo_source.jpg", mode: "single" }),
});

const data = await response.json();
console.log("Result:", data.image_url);
console.log("Faces restored:", data.faces_detected);
