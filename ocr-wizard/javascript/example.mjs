// OCR Wizard API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/ocr-wizard

const HOST = "ocr-wizard.p.rapidapi.com";
const URL = `https://${HOST}/ocr`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-monstera-5709059.jpg" }),
});

const data = await response.json();
console.log("Language:", data.body.detectedLanguage);
console.log("Text:", data.body.fullText);
