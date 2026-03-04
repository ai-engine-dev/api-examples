// Photo to Anime API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/photo-to-anime

const HOST = "phototoanime1.p.rapidapi.com";
const URL = `https://${HOST}/cartoonize`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ image_url: "https://openmediadata.s3.eu-west-3.amazonaws.com/face.jpg" }),
});

const data = await response.json();
console.log("Result:", data.image_url);
console.log("Size:", data.width, "x", data.height);
