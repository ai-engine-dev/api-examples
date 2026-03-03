// Face Swap API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/face-swap

const HOST = "deepfake-face-swap-ai.p.rapidapi.com";
const URL = `https://${HOST}/swap-face`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ source_url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face.jpg", target_url: "https://raw.githubusercontent.com/ai-engine-dev/api-examples/master/assets/samples/face2.jpg" }),
});

const data = await response.json();
console.log("Result:", data.image_url);
console.log("Size:", data.width, "x", data.height);
