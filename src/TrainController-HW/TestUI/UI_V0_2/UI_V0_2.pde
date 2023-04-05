import controlP5.*;
import processing.serial.*;

Serial myPort;  // The serial port

//Declaring controlP5 object
ControlP5 cp5;

//declaring global variables here
JSONObject jsonDataIn, jsonDataOut; 
String dataIn, dataOut;

////output variables
//int testCommandedSpeed, testCurrentSpeed, testAuthority, undergroundState, testSpeedLimit, testTemperature, testEngineState,
//      stationState, platformSide, testExternalLightState, testInternalLightState, testLeftDoorState, testRightDoorState, 
//      engineStatus, commsStatus, emergencyBrake, serviceBrake, internalLights, externalLights,
//      leftDoor, rightDoor, manualSpeedOverride, Kp, Ki;
//String time, beacon, nextStationName;

//input cariables
int engineState, serviceBrakeState, emergencyBrakeState, internalLightState, externalLightState,
      currentSpeed, commandedSpeed, authority, speedLimit, temperature, communicationState, time,
      power;
      
boolean rightDoorState, leftDoorState;
String stationName;

void setup(){
  //decalre screen size
  size(900, 600);

  cp5 = new ControlP5(this);
  
  //---------------------------Serial---------------------------
  // List all the available serial ports:
  print("List:");
  printArray(Serial.list());
  // Open the port you are using at the rate you want:
  myPort = new Serial(this, "COM6", 9600); //TODO: Uncomment
  println(Serial.list());
  //------------------------End Serial--------------------------
}

void draw(){
  //---------------------------Get Data---------------------------
  dataIn = getSerialData();
  //println(dataIn);
  println(dataIn);
  if(dataIn!=null){
    jsonDataIn = getJSONData(dataIn);
  }
   
  //-----------------------End Get Data---------------------------
  
  background(255);
  
  if (jsonDataIn!=null){
    updateUI(jsonDataIn);
    //println(jsonDataIn.getInt("Right Door Command"));
    ////time = jsonDataIn.getString("Time");
    //engineState = jsonDataIn.getInt("Right Door Command");
    //serviceBrakeState = jsonDataIn.getInt("Service Brake State");
    //externalLightState = jsonDataIn.getInt("External Lights State");
    //internalLightState = jsonDataIn.getInt("Internal Lights State");
    
    //// //TODO: implemet current station in JSON
    //currentSpeed = jsonDataIn.getInt("Current Speed");
    ////jsonDataIn.getInt("Manual Speed Override"), 167);
    //emergencyBrakeState = jsonDataIn.getInt("Emergency Brake State");
    
    //commandedSpeed = jsonDataIn.getInt("Commanded Speed");
    //authority = jsonDataIn.getInt("Authority");
    //speedLimit = jsonDataIn.getInt("Speed Limit");
    //rightDoorState = jsonDataIn.getInt("Right Door State");
    //leftDoorState = jsonDataIn.getInt("Left Door State");
  }
  
  ui();

  //draw a line to seprate the test UI
  rectMode(CORNER);  // Default rectMode is CORNER
  fill(0);  // Set fill to white
  rect(0, 405, 900, 5);  // Draw white rect using CORNER mode

  ////Test UI inputs and outputs
  //drawTextBoxWithBackground(50, 450, 200, 60, 32, "Cur Spd: ", 167);
  //drawTextBoxWithBackground(50, 520, 200, 60, 32, "Auth: ", 167);
  //drawTextBoxWithBackground(50, 590, 200, 60, 32, "Spd Lim: ", 167);
  //drawTextBoxWithBackground(50, 660, 200, 60, 32, "Temp: ", 167);
  

  //jsonDataOut = packJSONData();
  //sendJSONData(jsonDataOut);
  //delay(1000);
}

void ui(){
  int fontSize = 20;
  drawTextBoxWithBackground(50, 50, 200, 60, fontSize, "Time: "+time, 167);
  drawTextBoxWithBackground(50, 120, 200, 60, fontSize, "Engine State: "+((boolean(engineState)) ? "On" : "Off"), 167);
  drawTextBoxWithBackground(50, 190, 200, 60, fontSize, "Service Brake: "+serviceBrakeState, 167);
  drawTextBoxWithBackground(50, 260, 200, 60, fontSize, "Ext Lights: "+externalLightState, 167);
  drawTextBoxWithBackground(50, 330, 200, 60, fontSize, "Int Lights: "+internalLightState, 167);

  drawTextBoxWithBackground(350, 50, 200, 60, fontSize, "Curr Station: ", 167); //TODO: implemet current station in JSON
  drawTextBoxWithBackground(350, 120, 200, 60+80, fontSize, "Speed: "+currentSpeed+"MPH", 167);
  drawTextBoxWithBackground(350, 190+80, 200, 60, fontSize, "Manual Spd Ovrd: ", 167);
  drawTextBoxWithBackground(350, 260+80, 200, 60, fontSize, "Emergency Brake: "+emergencyBrakeState, 167);

  drawTextBoxWithBackground(650, 50, 200, 60, fontSize, "Comd Spd: "+commandedSpeed+"MPH", 167);
  drawTextBoxWithBackground(650, 120, 200, 60, fontSize, "Authority: "+authority+"Blocks", 167);
  drawTextBoxWithBackground(650, 190, 200, 60, fontSize, "Spd Lim: "+speedLimit+"MPH", 167);
  drawTextBoxWithBackground(650, 260, 200, 60, fontSize, "Right Door: "+rightDoorState, 167);
  drawTextBoxWithBackground(650, 330, 200, 60, fontSize, "Left Door: "+leftDoorState, 167);
  
  drawTextBoxWithBackground(50, 480, 200, 60, fontSize, "Power: "+power, 167);
  drawTextBoxWithBackground(50, 550, 200, 60, fontSize, "Service Brake State: "+serviceBrakeState, 167);
  drawTextBoxWithBackground(350, 480, 200, 60, fontSize, "Curr Station: ", 167); //TODO: implemet current station in JSON
  drawTextBoxWithBackground(350, 550, 200, 60+80, fontSize, "Speed: "+currentSpeed, 167);
  drawTextBoxWithBackground(650, 480, 200, 60, fontSize, "Comd Spd: "+commandedSpeed, 167);
  drawTextBoxWithBackground(650, 550, 200, 60, fontSize, "Authority: "+authority, 167);
}

void updateUI(JSONObject jsonDataIn){
  //int , , , , , ,
  //    , , , , , temperature, communicationState;
  //String stationName;
  
    //println(jsonDataIn.getInt("Right Door Command"));
    //time = jsonDataIn.getString("Time");
    engineState = jsonDataIn.getInt("Right Door Command");
    serviceBrakeState = jsonDataIn.getInt("Service Brake Command");
    externalLightState = jsonDataIn.getInt("External Lights State");
    internalLightState = jsonDataIn.getInt("Internal Lights State");
    
    // //TODO: implemet current station in JSON
    currentSpeed = jsonDataIn.getInt("Current Speed");
    //jsonDataIn.getInt("Manual Speed Override"), 167);
    emergencyBrakeState = jsonDataIn.getInt("Emergency Brake State");
    
    commandedSpeed = jsonDataIn.getInt("Commanded Speed");
    authority = jsonDataIn.getInt("Authority");
    speedLimit = (int)jsonDataIn.getFloat("Speed Limit");
    rightDoorState = jsonDataIn.getBoolean("Right Door State");
    leftDoorState = jsonDataIn.getBoolean("Left Door State");
    power = jsonDataIn.getInt("Power");
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
