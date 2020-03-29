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
    ctx.fillStyle = "blue";
    ctx.fillRect(0, 0, 640, 480);
    ellipse(320, 240, 320, 240, 'green');
    console.log(str(map.cities));
    for(var n=0;n<map.cities.length;n++){
	var c = map.cities[n];
	var player = map.players[c.owner];
	circle(c.pos[0], c.pos[1], 5, player.color);
    }
}
function initGame(){
    canvas = GEBI("canvas");
    canvas.width  = 640;
    canvas.height = 480;
    ctx = canvas.getContext("2d");
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
