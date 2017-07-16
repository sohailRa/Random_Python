function Pipe(){

	var spacing = random(80, height/4);
	var centery = random(spacing, height-spacing);
	this.top = centery - spacing/2;
	this.bottom = height - (centery + spacing/2);
	this.x = width;
	this.w = 35;
	this.speed = 3;
	this.highlight = false;

	this.show = function(){
		fill(0,204,0);
		if(this.highlight)
			fill(0,204,0);
		rect(this.x, 0, this.w, this.top);
		rect(this.x, height-this.bottom, this.w, this.bottom);		
	}

	this.update = function(){
		this.x -= this.speed;
	}

	this.offscreen = function(){
		return (this.x < -this.w);
	}

	this.point = function(){
		return (bird.x == this.x+this.w);
	}

	this.hits = function(){
		if(bird.y < this.top || bird.y > height - this.bottom){
			if(bird.x+25 > this.x && bird.x+25 < this.x+this.w){
				this.highlight = true;
				return true;
			}
		}
		this.highlight = false;
		return false;
	}
}