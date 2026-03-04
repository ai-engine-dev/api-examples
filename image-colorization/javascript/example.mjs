// Image Colorization API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/image-colorization

const HOST = "photocolorizer-ai.p.rapidapi.com";
const URL = `https://${HOST}/colorize-photo`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-suzy-hazelwood-5292049.jpg" }),
});

const data = await response.json();
console.log("Colorized image:", data.body.imageUrl);
