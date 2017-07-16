// http://localhost:8000
// python -m SimpleHTTPServer
var bird;
var bird_img;
var score;
var pipes = [];
var wing;
var hit;
var point;
var startButton;
var start = false;

function preload(){
	wing = loadSound("sounds/wing.wav");
	hit = loadSound("sounds/hit.wav");
	point = loadSound("sounds/point.wav");
	bird_img = loadImage("f_bird.png");

}

function setup(){
	createCanvas(400,600);
	background(0,204,204);
	startt();
}

function draw(){
	if(start){
		background(0,204,204);
		startButton.remove();
		for(var i=pipes.length-1; i>=0; i--){
			pipes[i].show();
			pipes[i].update();

			if(pipes[i].hits(bird)){
				console.log("HIT");textSize(64);
				hit.play();
				start = false;
				fill(255,0,0);
				textAlign(CENTER);
				text("Game Over!!!", width/2, height/2);
				text(score, width/2, 70);
				gameOver();
				startt();
			}
			if(pipes[i].offscreen()){
				pipes.splice(i, 1);
			}
			if(pipes[i].point(bird)){
				score++;
				point.play();
			}
		}
		bird.show();
		bird.update();

		if(frameCount % 80 == 0){
			pipes.push(new Pipe());
		}
		textSize(64);
		fill(0);
		textAlign(CENTER);
		text(score, width/2, 70);
	}
	else{
		gameOver();
	}
}

function keyPressed(){
	if(key == ' '){
		wing.play();
		bird.up();
	}
}

function reset(){
	bird = new Bird();
	pipes.push(new Pipe());
	score = 0;
	start = true;
}

function startt(){
	startButton = createButton('Start');
	startButton.position(width/2, height/2+40);
	startButton.mousePressed(reset);
}

function gameOver(){
	for(var j=0; j<pipes.length; j++)
		pipes.splice(j, 1);
}

