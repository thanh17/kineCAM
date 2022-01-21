// must print at 200 PPI

// Change this variables to update width of each hole and
// number of frames according to your chosen variable numbers in gpio_button.py
float hole_w = 3;
int numframes = 3;


int n;
float mask_w;
PImage photo;
int y_pos = 0;
float scale = 1.61;

float stripes_w;
float step = 0;
boolean test = true;
boolean redraw = false;
float mouseYstart = 0;

void setup() {
  size(379, 509);
  
  photo = loadImage("flapping.jpg");
  hole_w *= scale;

  mask_w = (numframes-1)*hole_w;
  stripes_w = hole_w*numframes;

  noStroke();
  background(255, 0);


  //save("strips.png");
}


void draw() {
  fill(255);
  rect(0, 0, width, height);

  if (test) image(photo, 0, 0);
  update();
}

void mouseMoved() {
  if (test) mouseYstart = mouseY;
}

void update() {
  y_pos = 0;
  for (int i = 0; i < 2*height/stripes_w; i++) {
    // grayscale
    fill(50);
    rect(0, step + mouseYstart + y_pos, width, mask_w);

    y_pos += stripes_w;
  }
  //step-=0.25;
}

void keyReleased() {
  if (keyCode == UP) {
    step -= hole_w;
    println(hole_w, mask_w); 
  } else if (keyCode == DOWN) {
    step += hole_w;
  } else if (keyCode == SHIFT) {
    save("strips.png");
  }
}
