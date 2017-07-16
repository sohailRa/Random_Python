
var bird;
var score;
var pipes = [];
var wing;
var hit;
var point;
var startButton;

function preload(){
	wing = loadSound("sounds/wing.wav");
	hit = loadSound("sounds/hit.wav");
	point = loadSound("sounds/point.wav");
}

function setup(){
	createCanvas(400,600);
	bird = new Bird();
	pipes.push(new Pipe());
	score = 0;
}

function draw(){
	background(0);
	for(var i=pipes.length-1; i>=0; i--){
		pipes[i].show();
		pipes[i].update();

		if(pipes[i].hits(bird)){
			console.log("HIT");textSize(64);
			fill(255,0,0);
			textAlign(CENTER);
			text("Game Over!", width/2, height/2);
			text(score, width/2, 70);
			hit.play();
			startButton = createButton('Start');
			startButton.position(width/2, height/2+40);
			exit();
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
	fill(0,102,153);
	textAlign(CENTER);
	text(score, width/2, 70);
	
}

function keyPressed(){
	if(key == ' '){
		wing.play();
		bird.up();
	}
}

// function score(){
// 	textSize(64);
// 	fill(0,102,153);
// 	textAlign(CENTER);
// 	text(score, width/2, 70);
// }

