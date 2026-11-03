// AI All-in-One API: JavaScript (Node.js) example
// One key for OCR, face analysis, background removal, text analysis and more.
// Docs: https://ai-engine.net/apis/all-in-one

const HOST = "ai-all-in-one.p.rapidapi.com";

async function call(path, params) {
  const response = await fetch(`https://${HOST}${path}`, {
    method: "POST",
    headers: {
      "x-rapidapi-host": HOST,
      "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams(params),
  });
  return response.json();
}

// Extract text from an image
const ocr = await call("/v1/ocr", { url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-monstera-5709059.jpg" });
console.log("Text:", ocr.body.fullText);

// Same key, another endpoint: sentiment of a review
const sentiment = await call("/v1/sentiment", { text: "I love this product, it works great" });
console.log("Sentiment:", sentiment.sentiment.label, sentiment.sentiment.score);
