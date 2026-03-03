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
  body: new URLSearchParams({ url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/bw-portrait.jpg" }),
});

const data = await response.json();
console.log("Colorized image:", data.body.imageUrl);
