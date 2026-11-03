// PPE Detection API: JavaScript (Node.js) example
// Docs: https://ai-engine.net/apis/ppe-detection

const HOST = "ppe-detection1.p.rapidapi.com";
const URL = `https://${HOST}/detect-ppe`;

const response = await fetch(URL, {
  method: "POST",
  headers: {
    "x-rapidapi-host": HOST,
    "x-rapidapi-key": process.env.RAPIDAPI_KEY || "YOUR_API_KEY",
    "Content-Type": "application/x-www-form-urlencoded",
  },
  body: new URLSearchParams({ url: "https://openmediadata.s3.eu-west-3.amazonaws.com/pexels-antoni-shkraba-5493662.jpg" }),
});

const data = await response.json();
const parts = ["HeadCover", "FaceCover", "LeftHandCover", "RightHandCover"];
for (const person of data.body.Persons) {
  const covered = parts.filter((part) => person[part]);
  console.log(`Person ${person.Id}: ${covered.join(", ") || "no equipment"}`);
}
