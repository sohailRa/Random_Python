float x = 0;
float y =0;
int spacing = 50;

void setup() {
  size(400,300);
}

void draw(){
  background(0);
  stroke(255);
  strokeWeight(2);
  
  
  //Simple Grid
  //x = spacing;
  //y = spacing;
  //while(x < width){
  //  line(x,0,x,height);
  //  x = x+spacing;
  //}
  //for(y=0; y<height; y = y+spacing){
  //  line(0,y,width,y);
  //}
  //Tile Grid
  fill(127);
  for(int y=0; y<height; y=y+spacing){
    for(int x=0; x<width; x= x+spacing){
      fill(random(255));
      rect(x,y,20,20);
    }
  }
}