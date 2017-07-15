void setup() {
  size(600, 600);
  background(50);
}
void draw() {
  stroke(255);
  line(pmouseX, pmouseY, mouseX, mouseY);
}