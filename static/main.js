function ellipse(x, y, r1, r2, c){
    ctx.beginPath();
    ctx.ellipse(x, y, r1, r2, 0, 0, 2 * Math.PI);
    ctx.strokeStyle = "black";
    ctx.fillStyle = c||"gray";
    ctx.stroke();
    ctx.fill();
}
function circle(x, y, r, c){
    ellipse(x, y, r, r, c);
}
function drawGame(){
    outln(str(map));
    console.log(str(map));
    ellipse(320, 240, 320, 240);
}
function initGame(){
    canvas = GEBI("canvas");
    ctx = canvas.getContext("2d");
    outln(ctx);
    drawGame();
}
fetch("/map")
    .then(response=>{
	return(response.json());
    })
    .then(data=>{
	map = data;
	initGame();
    })
    .catch(error=>{
	console.log("error");
    })
