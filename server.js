const express = require("express");
const app = express();
const spawner = require("child_process").spawn;
const { exec } = require("child_process");
app.use(express.json());
const cors =require( "cors")

app.use(cors({
  origin: "*",
  // credentials: true  
}))

app.get("/",(req,res)=>{
  console.log("someone is using")
  res.send("Welcome, use the /answer end point with method as post to get the answer<br><br>The input format :<br> {<br>question:string<br>}<br><br>Output format :<br>{<br>validation:true | false | '',<br>answer:justification,<br>link:link_string | ''<br>}")
})

app.post("/summarize", async(req, res) => {
  // console.log(req.body)
  console.log("Saving the data")
  const py_process = spawner("python", ["store.py", JSON.stringify(req.body)]);
  py_process.stdout.on("data", (data) => {
    // console.log(data.toString())
    res.send(data.toString());
  });

});

app.post("/answer", (req, res) => {
  // console.log(req.body.content[1])
  console.log(req.body)
  const py_process = spawner("python", ["Answer.py",req.body.question]);
  py_process.stdout.on("data", (data,error) => {
    // console.log(data.toString())
    res.send(data.toString());
  });
});

app.post("/data",  async(req, res) => {
  // console.log("collecting the data from link")
  const command = `curl -s ${req.body.link} | unfluff`;
  exec(command, (error, stdout, stderr) => {
    const data=JSON.parse(stdout)
    // console.log(data.text)
    res.send(data.text)
  })
});
const port=process.env.PORT || 8081
app.listen(port, () => {
    console.log(`listerning to ${port}`);
});