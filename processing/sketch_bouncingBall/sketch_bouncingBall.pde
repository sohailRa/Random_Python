//--------------------------- Bouncing Ball
float pointX;
float xspeed;

void setup() {
  size(600, 400);
  pointX = 0;
  xspeed = 10;
}
void draw() {
  background(1);
  fill(155);
  stroke(255);
  ellipse(pointX, height/2, 32,32);
  
  pointX = pointX + xspeed;
  
  if(pointX > width){
    xspeed = -10;
  }
  if(pointX < 0){
    xspeed = 10;
  }
}