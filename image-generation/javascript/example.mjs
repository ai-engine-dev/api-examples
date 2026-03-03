// Image Generation API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/image-generation

const HOST = "imagegenius-ai.p.rapidapi.com";
const URL = `https://${HOST}/generate-image`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ prompt: "A futuristic city at sunset with flying cars" }),
});

const data = await response.json();
console.log("Generated image:", data.body.imageUrl);
