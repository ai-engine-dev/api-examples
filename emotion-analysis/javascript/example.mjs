// Emotion & Personality Analysis API — JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/emotion-analysis

const HOST = "emotion-sentiment-personality-analysis.p.rapidapi.com";
const URL = `https://${HOST}/emotions`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ text: "I am so happy today! The weather is beautiful and I feel great." }),
});

const data = await response.json();
data.emotions.forEach(e => console.log(`  ${e.label}: ${e.score.toFixed(3)}`));
