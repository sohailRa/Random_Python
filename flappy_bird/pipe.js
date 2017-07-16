function Pipe(){
	this.top = random(height/2);
	this.bottom = random(height/2);
	this.x = width;
	this.w = 20;

	this.show = function(){
		fill(255);
	}
}