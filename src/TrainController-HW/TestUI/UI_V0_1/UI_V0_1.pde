import controlP5.*;
import processing.serial.*;

Serial myPort;  // The serial port

//Declaring controlP5 object
ControlP5 cp5;

void setup() {
  //decalre screen size
  size(900, 800);

  cp5 = new ControlP5(this);

  //myPort = new Serial(this, Serial.list()[0], 9600);

  // format is (name, low val, high val, xpos, ypos, xsize, ysize)
  //Slider s = cp5.addSlider("Speed", 0, 100, 10, 10, 200, 20);

  
    cp5.addToggle("External Light State")
   .setValue(0)
   .setPosition(350,450)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    cp5.addToggle("Internal Light State")
   .setValue(0)
   .setPosition(350,520)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   cp5.addToggle("Right Door State")
   .setValue(0)
   .setPosition(350,590)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    cp5.addToggle("Left Door State")
   .setValue(0)
   .setPosition(350,660)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   
   cp5.addToggle("Emergency Brake State")
   .setValue(0)
   .setPosition(450,450)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    cp5.addToggle("Engine State")
   .setValue(0)
   .setPosition(450,520)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   cp5.addToggle("Underground State")
   .setValue(0)
   .setPosition(450,590)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    cp5.addToggle("Service Brake State")
   .setValue(0)
   .setPosition(450,660)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   //.setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    
}

void draw() {
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

  //draw a line to seprate the test UI
  rectMode(CORNER);  // Default rectMode is CORNER
  fill(0);  // Set fill to white
  rect(0, 405, 900, 5);  // Draw white rect using CORNER mode

  //Test UI inputs and outputs
  drawTextBoxWithBackground(50, 450, 200, 60, 32, "Cur Spd: ", 167);
  drawTextBoxWithBackground(50, 520, 200, 60, 32, "Auth: ", 167);
  drawTextBoxWithBackground(50, 590, 200, 60, 32, "Spd Lim: ", 167);
  drawTextBoxWithBackground(50, 660, 200, 60, 32, "Temp: ", 167);
  

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
