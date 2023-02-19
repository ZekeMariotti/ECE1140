import controlP5.*;
import processing.serial.*;

Serial myPort;  // The serial port

//Declaring controlP5 object
ControlP5 control;

void setup(){
  //decalre screen size
  size(900,600);
  
  control = new ControlP5(this);
  
  //myPort = new Serial(this, Serial.list()[0], 9600);
  
  // format is (name, low val, high val, xpos, ypos, xsize, ysize)
  //Slider s = control.addSlider("Speed", 0, 100, 10, 10, 200, 20);
}

void draw(){
  background(255);
  
  drawTextBoxWithBackground(50, 50, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(50, 120, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(50, 190, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(50, 260, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(50, 330, 200, 60, 32, "Time: ", 167);
  
  drawTextBoxWithBackground(350, 50, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(350, 120, 200, 60+80, 32, "Speed: 20", 167);
  drawTextBoxWithBackground(350, 190+80, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(350, 260+80, 200, 60, 32, "Emergency Brake: ", 167);
  
  drawTextBoxWithBackground(650, 50, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(650, 120, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(650, 190, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(650, 260, 200, 60, 32, "Time: ", 167);
  drawTextBoxWithBackground(650, 330, 200, 60, 32, "Time: ", 167);
}

void drawTextBoxWithBackground(int x, int y, int xsize, int ysize,
  int textSize, String text, int colour)
{
  //rectMode(CORNER);  // Default rectMode is CORNER
  //fill(0);  // Set fill to white
  //rect(50, 50, 400, 200);  // Draw white rect using CORNER mode
  
  //fill(255);
  //textSize(128);
  //textAlign(LEFT);
  //text("word111", 50, 55, 410, 200); 
  
  rectMode(CORNER);  // Default rectMode is CORNER
  fill(colour);  // Set fill to white
  rect(x, y, xsize, ysize);  // Draw white rect using CORNER mode
  
  fill(0);
  textSize(textSize);
  textAlign(LEFT);
  text(text, x, y+5, xsize+10, ysize); 
}
