PImage car;

void setup(){
  size(300,200);
  car = loadImage("car.jpg");
}

void draw(){
  background(0);
  image(car, 0,0, mouseX, mouseY);
}