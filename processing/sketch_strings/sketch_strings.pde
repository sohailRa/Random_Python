String[] words;
IntDict concordance;

int index = 0;
void setup(){
  //size(600,400);
  String [] lines = loadStrings("file.txt");
  String alltext = join(lines, " ");
  words = splitTokens(alltext, " ,.:;!");
  concordance = new IntDict();
  
  for(int i=0; i<words.length; i++){
    concordance.increment(words[i].toLowerCase());
  }
  concordance.sortValues();
  println(concordance);
}

void draw(){
  background(0);
  //textSize(64);
  //textAlign(CENTER);
  //text(words[index], width/2, height/2);
  //index++;
  String[] keys = concordance.keyArray();
  for(int i=0; i<keys.length; i++){
    int count = concordance.get(keys[i]);
    println(keys[i], count);
  }
  noLoop();
}