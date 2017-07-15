//Grid tile
size(400, 300);
background(0);
stroke(255);
strokeWeight(2);

for (int y=0; y<height; y=y+20) {
  for (int x=0; x<width; x= x+20) {
    fill(random(255));
    rect(x, y, 20, 20);
  }
}