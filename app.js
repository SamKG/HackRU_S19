var express = require('express');
var app = express();
var path = require('path');
var cmd = require('node-cmd');

app.use(express.static('public'));
app.get("/",(req,res,next) => { res.sendFile(path.join(__dirname + '/index.html'))});
app.post("/video/:vidId",(req,res,next) => { 
    console.log("RECV POST "+req.params.vidId);
    cmd.get('cd ./algo_plus_chat && python3.7 main.py '+req.params.vidId,
        function(err,data,stderr){
            console.log(err);
            var l = [];
            data.split("\n").forEach(element => {
                var l2 = [];
                element.split(",").forEach(elem2=>{
                    elem2 = elem2.replace('(','');
                    elem2 = elem2.replace(')','');
                    elem2 = elem2.replace(' ','');
                    l2.push(elem2);
                })
                if (l2.length >= 2){
		    console.log(l2);
                    l.push(l2);
                }
               
            });
            console.log("SENDING RES");
            res.json(l);
        }
)})
app.listen(80, () => {
    
});

