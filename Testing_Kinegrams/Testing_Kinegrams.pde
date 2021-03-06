int n;
int slit_w;
int hole_w;
PImage photo;

void setup(){
  size(320, 240);
  photo = loadImage("cata3_difference.jpg");
  background(255);
  slit_w = 6;
  hole_w = 3;
  n = 0;
  fill(0,0,0);
  noStroke();
}

void draw(){
  background(255);
  image(photo, 0, 0);
  int start_x = n%(slit_w+hole_w)-slit_w;
  draw_slits(start_x);
  n += 1;
}

void draw_slits(int start_x){
  while(start_x <= width){
    rect(start_x, 0, slit_w, height); 
    start_x += slit_w + hole_w;
  }
}
