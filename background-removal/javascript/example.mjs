// Background Removal API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/background-removal

const HOST = "background-removal-ai.p.rapidapi.com";
const URL = `https://${HOST}/remove-background`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ image_url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/object.jpg" }),
});

const data = await response.json();
console.log("Result:", data.image_url);
console.log("Size:", data.width, "x", data.height);
