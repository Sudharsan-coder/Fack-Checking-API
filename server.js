const express = require("express");
const app = express();
const spawner = require("child_process").spawn;
const { exec } = require("child_process");
app.use(express.json());
const cors =require( "cors")

app.use(cors({
  origin: ["http://localhost:5173","http://localhost:5174"],
  // credentials: true  
}))


app.get("/",(req,res)=>{
  console.log("someone is using")
  res.send("Welcome, use the /answer end point with method as post to get the answer<br><br>The input format :<br> {<br>question:string<br>}<br><br>Output format :<br>{<br>validation:true | false | '',<br>answer:justification,<br>link:link_string | ''<br>}")
})

app.post("/summarize", async(req, res) => {
  // console.log(req.body)
  console.log("Saving the data")
  const py_process = spawner("python3.11", ["store.py", JSON.stringify(req.body)]);
  py_process.stdout.on("data", (data) => {
    console.log(data.toString())
    res.send(data.toString());
  });

});

app.post("/answer", (req, res) => {
  // console.log(req.body.content[1])
  console.log(req.body)
  const py_process = spawner("python3.11", ["Answer.py",req.body.question]);
  py_process.stdout.on("data", (data) => {
    console.log(data.toString())
    res.send(data.toString());
  });
});

app.post("/data",  async(req, res) => {
  console.log("collecting the data from link")
  const command = `curl -s ${req.body.link} | unfluff`;
  exec(command, (error, stdout, stderr) => {
    const data=JSON.parse(stdout)
    // console.log(data.text)
    res.send(data.text)
  })
});
app.listen(8081, () => {
    console.log("listerning to 8081");
});