import controlP5.*;
import processing.serial.*;

Serial myPort;  // The serial port

//Declaring controlP5 object
ControlP5 cp5;

//declaring global variables here
JSONObject jsonDataIn, jsonDataOut; 
String dataIn, dataOut;

//output variables
int commandedSpeed, currentSpeed, authority, undergroundState, speedLimit, temperature, engineState,
      stationState, platformSide, externalLightState, internalLightState, leftDoorState, rightDootState, 
      serviceBrakeState, engineStatus, commsStatus, emergencyBrake, serviceBrake, internalLights, externalLights,
      leftDoor, rightDoor, manualSpeedOverride, Kp, Ki;
String time, beacon, nextStationName;

void setup() {
  //decalre screen size
  size(900, 800);

  cp5 = new ControlP5(this);
  
  //---------------------------Serial---------------------------
  // List all the available serial ports:
  print("List:");
  printArray(Serial.list());
  // Open the port you are using at the rate you want:
  //myPort = new Serial(this, Serial.list()[0], 115200); //TODO: Uncomment
  //------------------------End Serial--------------------------


  // format is (name, low val, high val, xpos, ypos, xsize, ysize)
  //Slider s = cp5.addSlider("Speed", 0, 100, 10, 10, 200, 20);
  
  cp5.addSlider("currentSpeed")
    .setPosition(50, 450)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Current Speed")
     ;  
  cp5.addSlider("commandedSpeed")
    .setPosition(50, 520)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Commanded Speed")
     ;  
  cp5.addSlider("authority")
    .setPosition(50, 590)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Authority")
     ;  
  cp5.addSlider("speedLimit")
    .setPosition(50, 660)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Speed Limit")
     ;

  
  cp5.addToggle("externalLightState")
   .setValue(0)
   .setPosition(350,450)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("External light state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
  cp5.addToggle("internalLightState")
   .setValue(0)
   .setPosition(350,520)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Internal Light State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   cp5.addToggle("rightDoorState")
   .setValue(0)
   .setPosition(350,590)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Right Door state")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
  cp5.addToggle("leftDoorState")
   .setValue(0)
   .setPosition(350,660)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("left Door State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   
   cp5.addToggle("emergencyBrakeState")
   .setValue(0)
   .setPosition(450,450)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Emergency Brake State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
  cp5.addToggle("engineState")
   .setValue(0)
   .setPosition(450,520)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Engine State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
   cp5.addToggle("undergroundState")
   .setValue(0)
   .setPosition(450,590)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Underground State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
  cp5.addToggle("serviceBrakeState")
   .setValue(0)
   .setPosition(450,660)
   .setSize(70,40)
   //.setColorForeground(0)
   //.setColorBackground(255)
   .setColorCaptionLabel(255) 
   .setLabel("Service Brake State")
   //.setValue(true)
   //.setMode(ControlP5.SWITCH)
   ;
    
}

void draw() {
  //---------------------------Get Data---------------------------
  //dataIn = getSerialData();
  //jsonDataIn = getJSONData(dataIn);
  
  //-----------------------End Get Data---------------------------
  
  int fontSize = 20;
  
  background(255);

  drawTextBoxWithBackground(50, 50, 200, 60, fontSize, "Time: "+jsonDataIn.getString("Time"), 167);
  drawTextBoxWithBackground(50, 120, 200, 60, fontSize, "Engine State: "+jsonDataIn.getInt("Engine Staus"), 167);
  drawTextBoxWithBackground(50, 190, 200, 60, fontSize, "Service Brake: "+jsonDataIn.getInt("Service Brake Status"), 167);
  drawTextBoxWithBackground(50, 260, 200, 60, fontSize, "Ext Lights: "+jsonDataIn.getInt("External Light State"), 167);
  drawTextBoxWithBackground(50, 330, 200, 60, fontSize, "Int Lights: "+jsonDataIn.getInt("Internal Light State"), 167);

  drawTextBoxWithBackground(350, 50, 200, 60, fontSize, "Curr Station: ", 167); //TODO: implemet current station in JSON
  drawTextBoxWithBackground(350, 120, 200, 60+80, fontSize, "Speed: 20"+jsonDataIn.getInt("Current Speed"), 167);
  drawTextBoxWithBackground(350, 190+80, 200, 60, fontSize, "Manual Spd Ovrd: "+jsonDataIn.getInt("Manual Speed Override"), 167);
  drawTextBoxWithBackground(350, 260+80, 200, 60, fontSize, "Emergency Brake: "+jsonDataIn.getInt("Emergency Brake State"), 167);

  drawTextBoxWithBackground(650, 50, 200, 60, fontSize, "Comd Spd: "+jsonDataIn.getInt("Commanded Speed"), 167);
  drawTextBoxWithBackground(650, 120, 200, 60, fontSize, "Authority: "+jsonDataIn.getInt("Authority"), 167);
  drawTextBoxWithBackground(650, 190, 200, 60, fontSize, "Spd Lim: "+jsonDataIn.getInt("Speed Limit"), 167);
  drawTextBoxWithBackground(650, 260, 200, 60, fontSize, "Right Door: "+jsonDataIn.getInt("Right Door State"), 167);
  drawTextBoxWithBackground(650, 330, 200, 60, fontSize, "Left Door: "+jsonDataIn.getInt("Left Door State"), 167);

  //draw a line to seprate the test UI
  rectMode(CORNER);  // Default rectMode is CORNER
  fill(0);  // Set fill to white
  rect(0, 405, 900, 5);  // Draw white rect using CORNER mode

  ////Test UI inputs and outputs
  //drawTextBoxWithBackground(50, 450, 200, 60, 32, "Cur Spd: ", 167);
  //drawTextBoxWithBackground(50, 520, 200, 60, 32, "Auth: ", 167);
  //drawTextBoxWithBackground(50, 590, 200, 60, 32, "Spd Lim: ", 167);
  //drawTextBoxWithBackground(50, 660, 200, 60, 32, "Temp: ", 167);
  

  jsonDataOut = packJSONData();
  sendJSONData(jsonDataOut);
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


JSONObject getJSONData(String dataIn){
 JSONObject jsonIn = parseJSONObject(dataIn);
 return jsonIn;
}

String getSerialData(){
  String data="";
  if ( myPort.available() > 0) {
    data = myPort.readStringUntil('\n');
  }
  println(data);
  return data;
}

//this will collect all the data and make a json object to send out
void sendJSONData(JSONObject jsonOut){
  //myPort.write("<"+jsonOut+">"); //TODO: Uncomment
  //println(jsonOut);
}

JSONObject packJSONData(){
  JSONObject json;
  json = new JSONObject();
  
  json.setInt("Commanded Speed", commandedSpeed);
  json.setInt("Current Speed", currentSpeed);
  json.setInt("Authority", authority);
  json.setInt("Underground State", undergroundState);
  json.setInt("Speed Limit", speedLimit);
  json.setInt("Temperature", temperature);
  json.setInt("Engine State", engineState);
  json.setInt("Station State", stationState);
  json.setInt("Platform Side", platformSide);
  json.setInt("External Light State", externalLightState);
  json.setInt("Internal Light State", internalLightState);
  json.setInt("Left Door State", leftDoorState);
  json.setInt("Right Door State", rightDootState);
  json.setInt("Service Brake State", serviceBrakeState);
  json.setInt("Engine Status", engineStatus);
  json.setInt("Communications Status", commsStatus);
  json.setInt("Emergency Brake", emergencyBrake);
  json.setInt("Service Brake", serviceBrake);
  json.setInt("Internal Lights", internalLights);
  json.setInt("External Lights", externalLights);
  json.setInt("Left Door", leftDoor);
  json.setInt("Right Door", rightDoor);
  json.setInt("Manual Speed Override", manualSpeedOverride);
  json.setInt("Kp", Kp);
  json.setInt("Ki", Ki);
  //println(currentSpeed);
  json.setString("Time", time); 
  json.setString("Beacon", beacon); 
  json.setString("Next Station Name", nextStationName); 
  
  return json;
}
