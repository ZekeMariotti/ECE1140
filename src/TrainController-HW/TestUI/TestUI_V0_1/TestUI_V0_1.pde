import controlP5.*;
import processing.serial.*;

Serial myPort;  // The serial port

//Declaring controlP5 object
ControlP5 cp5;

//declaring global variables here
JSONObject jsonDataIn, jsonDataOut; 
String dataIn, dataOut;

//output variables
int testCommandedSpeed, testCurrentSpeed, testAuthority, undergroundState, testSpeedLimit, testTemperature, testEngineState,
      stationState, platformSide, testExternalLightState, testInternalLightState, testLeftDoorState, testRightDoorState, 
      engineStatus, commsStatus, emergencyBrake, serviceBrake, internalLights, externalLights,
      leftDoor, rightDoor, manualSpeedOverride, Kp, Ki;
String time, beacon, nextStationName;

//input cariables
int engineState, serviceBrakeState, emergencyBrakeState, internalLightState, externalLightState, leftDoorState,
      rightDoorState, currentSpeed, commandedSpeed, authority, speedLimit, temperature, communicationState, Time;
String stationName;

void setup() {
  //decalre screen size
  size(900, 800);

  cp5 = new ControlP5(this);
  
  //---------------------------Serial---------------------------
  // List all the available serial ports:
  print("List:");
  printArray(Serial.list());
  // Open the port you are using at the rate you want:
  myPort = new Serial(this, "COM8", 115200); //TODO: Uncomment
  println(Serial.list());
  //------------------------End Serial--------------------------


  // format is (name, low val, high val, xpos, ypos, xsize, ysize)
  //Slider s = cp5.addSlider("Speed", 0, 100, 10, 10, 200, 20);
  
  cp5.addSlider("testCurrentSpeed")
    .setPosition(50, 450)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Current Speed")
     ;  
  cp5.addSlider("testCommandedSpeed")
    .setPosition(50, 520)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Commanded Speed")
     ;  
  cp5.addSlider("testAuthority")
    .setPosition(50, 590)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Authority")
     ;  
  cp5.addSlider("testSpeedLimit")
    .setPosition(50, 660)
    .setSize(150, 40)
    .setColorCaptionLabel(255) 
    .setLabel("Speed Limit")
     ;

  
  cp5.addToggle("testExternalLightState")
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
  cp5.addToggle("testInternalLightState")
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
   cp5.addToggle("testRightDoorState")
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
  cp5.addToggle("testLeftDoorState")
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
   
   cp5.addToggle("emergencyBrake")
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
  cp5.addToggle("engineStatus")
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
  cp5.addToggle("serviceBrake")
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
   
   //delay(3000);
    
}

void draw() {
  //---------------------------Get Data---------------------------
  //dataIn = getSerialData();
  //println(dataIn);
  //println(dataIn);
  //if(dataIn!=null){
  //  jsonDataIn = getJSONData(dataIn);
  //}
   
  //-----------------------End Get Data---------------------------
  delay(100);

  
  background(255);
  ////println(jsonDataIn);
  //if (jsonDataIn!=null){
  //  //updateUI(jsonDataIn);
  //  //println(jsonDataIn.getInt("Right Door Command"));
  //  ////time = jsonDataIn.getString("Time");
  //  //engineState = jsonDataIn.getInt("Right Door Command");
  //  //serviceBrakeState = jsonDataIn.getInt("Service Brake State");
  //  //externalLightState = jsonDataIn.getInt("External Lights State");
  //  //internalLightState = jsonDataIn.getInt("Internal Lights State");
    
  //  //// //TODO: implemet current station in JSON
  //  //currentSpeed = jsonDataIn.getInt("Current Speed");
  //  ////jsonDataIn.getInt("Manual Speed Override"), 167);
  //  //emergencyBrakeState = jsonDataIn.getInt("Emergency Brake State");
    
  //  //commandedSpeed = jsonDataIn.getInt("Commanded Speed");
  //  //authority = jsonDataIn.getInt("Authority");
  //  //speedLimit = jsonDataIn.getInt("Speed Limit");
  //  //rightDoorState = jsonDataIn.getInt("Right Door State");
  //  //leftDoorState = jsonDataIn.getInt("Left Door State");
  //}
  
  //ui();

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
  //delay(1000);
}


void ui(){
  int fontSize = 20;
  drawTextBoxWithBackground(50, 50, 200, 60, fontSize, "Time: "+time, 167);
  drawTextBoxWithBackground(50, 120, 200, 60, fontSize, "Engine State: "+engineState, 167);
  drawTextBoxWithBackground(50, 190, 200, 60, fontSize, "Service Brake: "+serviceBrakeState, 167);
  drawTextBoxWithBackground(50, 260, 200, 60, fontSize, "Ext Lights: "+externalLightState, 167);
  drawTextBoxWithBackground(50, 330, 200, 60, fontSize, "Int Lights: "+internalLightState, 167);

  drawTextBoxWithBackground(350, 50, 200, 60, fontSize, "Curr Station: ", 167); //TODO: implemet current station in JSON
  drawTextBoxWithBackground(350, 120, 200, 60+80, fontSize, "Speed: 20"+currentSpeed, 167);
  drawTextBoxWithBackground(350, 190+80, 200, 60, fontSize, "Manual Spd Ovrd: ", 167);
  drawTextBoxWithBackground(350, 260+80, 200, 60, fontSize, "Emergency Brake: "+emergencyBrakeState, 167);

  drawTextBoxWithBackground(650, 50, 200, 60, fontSize, "Comd Spd: "+commandedSpeed, 167);
  drawTextBoxWithBackground(650, 120, 200, 60, fontSize, "Authority: "+authority, 167);
  drawTextBoxWithBackground(650, 190, 200, 60, fontSize, "Spd Lim: "+speedLimit, 167);
  drawTextBoxWithBackground(650, 260, 200, 60, fontSize, "Right Door: "+rightDoorState, 167);
  drawTextBoxWithBackground(650, 330, 200, 60, fontSize, "Left Door: "+leftDoorState, 167);
}

void updateUI(JSONObject jsonDataIn){
  //int , , , , , ,
  //    , , , , , temperature, communicationState;
  //String stationName;
  
    //println(jsonDataIn.getInt("Right Door Command"));
    //time = jsonDataIn.getString("Time");
    engineState = jsonDataIn.getInt("Right Door Command");
    serviceBrakeState = jsonDataIn.getInt("Service Brake State");
    externalLightState = jsonDataIn.getInt("External Lights State");
    internalLightState = jsonDataIn.getInt("Internal Lights State");
    
    // //TODO: implemet current station in JSON
    currentSpeed = jsonDataIn.getInt("Current Speed");
    //jsonDataIn.getInt("Manual Speed Override"), 167);
    emergencyBrakeState = jsonDataIn.getInt("Emergency Brake State");
    
    commandedSpeed = jsonDataIn.getInt("Commanded Speed");
    authority = jsonDataIn.getInt("Authority");
    speedLimit = jsonDataIn.getInt("Speed Limit");
    rightDoorState = jsonDataIn.getInt("Right Door State");
    leftDoorState = jsonDataIn.getInt("Left Door State");
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
  //println(dataIn);
 JSONObject jsonIn = parseJSONObject(dataIn);
 return jsonIn;
}

String getSerialData(){
  String data="";
  if ( myPort.available() > 0) {
    data = myPort.readStringUntil('\n');
  }
  //println(data);
  return data;
}

//this will collect all the data and make a json object to send out
void sendJSONData(JSONObject jsonOut){
  String s = (jsonOut.toString().replace("\n ", "")).replace(": ",":").replace(", ",",").replace("{ ","{")
                  .replace(" }","}");
  myPort.write(""+s+"&"); //TODO: Uncomment
  println("<"+s+">");
}

JSONObject packJSONData(){
  JSONObject json;
  json = new JSONObject();
  
  json.setInt("Commanded Speed", testCommandedSpeed);
  json.setInt("Current Speed", testCurrentSpeed);
  json.setInt("Authority", testAuthority);
  json.setInt("Underground State", undergroundState);
  json.setInt("Speed Limit", testSpeedLimit);
  json.setInt("Temperature", testTemperature);
  json.setInt("Engine State", testEngineState);
  json.setInt("Station State", stationState);
  json.setInt("Platform Side", platformSide);
  json.setInt("External Light State", testExternalLightState);
  json.setInt("Internal Light State", testInternalLightState);
  json.setInt("Left Door State", testLeftDoorState);
  json.setInt("Right Door State", testRightDoorState);
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
