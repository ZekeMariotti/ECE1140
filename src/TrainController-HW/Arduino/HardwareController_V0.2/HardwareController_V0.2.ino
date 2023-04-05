
#define ENGINESWITCH 22
#define AUTODRIVESWITCH 23
#define RIGHTDOORSWITCH 24
#define LEFTDOORSWITCH 25
#define INTERIORLIGHTSWITCH 26
#define EXTERIORLIGHTSWICH 27
#define EMERGENCYBRAKESWITCH 28
#define SERVICEBRAKESWITCH 29
#define SPEEDPOT A8
#define BRAKEPOT A1

#define NUMBEROFSWITCHES 10


#include <ArduinoJson.h>
#include <StreamUtils.h>
#include <Ethernet.h>
#include <EthernetUdp.h>

//setup ethernet========================================================================
// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 101);
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

// buffers for receiving and sending data
char packetBuffer[600];
//======================================================================================

//output variables, 
int serviceBrakeCommand, emergencyBrakeState, autoDriveCommand, currentSpeed, commandedSpeed, manualCommandedSpeed, authority; 
unsigned long power; 

//internal beacon variables
bool isBeacon, firstBeaconPassed, secondBeaconPassed, stationState;

unsigned long prevTime = 0; 
unsigned int Kp;
unsigned int Ki;

//Global and system wide variables 
int switchStateArray[NUMBEROFSWITCHES];
StaticJsonDocument<768> jsonDataIn;
StaticJsonDocument<768> jsonDataOut;
StaticJsonDocument<768> jsonDataUI;
String serialJSONOut;
String serialJSONUI;


// we use includes below define so we can use definitions in library when needed
// #include "drive.cpp"
#include "TControl.h"
TControl tControl;

#include "Drive.h"
Drive driv(&tControl, &Kp, &Ki, &power, &serviceBrakeCommand, &emergencyBrakeState, switchStateArray);


unsigned long update_period = 1000.0f / 50.0f; // in ms
unsigned long tsLastLoop = millis();
long tsUsed; // in ms



void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial1.begin(9600);
  
  //input setup for control interface
  setSwitches();
  updateSwitchStates(switchStateArray);
  // engineState = 
  setupUDP();
  // Serial.println("End of setup");

  Kp = 1;
  Ki = 1;
  manualCommandedSpeed=0;
  
}

void loop() {
  // Serial.println(Ki);
  // Serial.println(Kp);
  // put your main code here, to run repeatedly:
  if(readUDP()){
    getJSONData();
  }
  
  // delay(1000);
  unsigned long currTime = millis();
  // int currTime = jsonDataIn["inputTime"];
  float dt = currTime-prevTime;
  updateSwitchStates(switchStateArray);
  // printSwitchStates();//this is to test the hardware
  drive(dt/1000);
  emergencyBrake();
  setStationState();
  // automaticSpeedControl();
  // delay(10);
  prevTime = currTime;
  
    
  tsUsed = millis() - tsLastLoop;
  if (200 > tsUsed) {
      //Do nothing
  } else {
    //send data
    sendJSONData(switchStateArray);
    tsLastLoop = millis();
  }

  //send data to the UI
  sendJSONDataUI(switchStateArray);
  
  // Serial.println("in loop");
  delay(50);

}

void updateSwitchStates(int *switchStateArray){
  switchStateArray[0]=!digitalRead(ENGINESWITCH);
  switchStateArray[1]=digitalRead(AUTODRIVESWITCH);
  switchStateArray[2]=!digitalRead(RIGHTDOORSWITCH);
  switchStateArray[3]=digitalRead(LEFTDOORSWITCH);
  switchStateArray[4]=digitalRead(INTERIORLIGHTSWITCH);
  switchStateArray[5]=!digitalRead(EXTERIORLIGHTSWICH);
  switchStateArray[6]=!digitalRead(EMERGENCYBRAKESWITCH);
  switchStateArray[7]=digitalRead(SERVICEBRAKESWITCH);
  switchStateArray[8]=map(analogRead(SPEEDPOT), 0, 1023, 0, 20);
  switchStateArray[9]=analogRead(BRAKEPOT);
}

void setSwitches(){
    //input setup for control interface
  pinMode(ENGINESWITCH, INPUT);
  pinMode(AUTODRIVESWITCH, INPUT);
  pinMode(RIGHTDOORSWITCH, INPUT);
  pinMode(LEFTDOORSWITCH, INPUT);
  pinMode(INTERIORLIGHTSWITCH, INPUT);
  pinMode(EXTERIORLIGHTSWICH, INPUT);
  pinMode(EMERGENCYBRAKESWITCH, INPUT);
  pinMode(SERVICEBRAKESWITCH, INPUT);
  pinMode(SPEEDPOT, INPUT);
  pinMode(BRAKEPOT, INPUT);
}

void printSwitchStates(){
  String states = "";
  for(int i=0; i<NUMBEROFSWITCHES; i++){
    states = states + switchStateArray[i] + ", ";
  }
  Serial.println(states);
}


//------------------------------------------------------------------------------
//Data viualisation stuff 
//TODO: Move to own library
String formatData(int *switchStateArray){
  //here we format the data into a string or json file
  String s = "";
  for(int i=0; i<NUMBEROFSWITCHES; i++){
    s = s + switchStateArray[i] + ", ";
  }  
  return s;
}

//public methods for the library
void sendDataToUI(int *switchStateArray){
    Serial.println(formatData(*switchStateArray));
}
//------------------------------------------------------------------------------


//------------------------------------------------------------------------------
//JSON Stuff
const char RECV_START = '<';
const char RECV_END = '>';
const int RECV_BUF_SIZE = 128;
char recvBuffer[RECV_BUF_SIZE];
int currPos = 0;
bool recvInProgress = false;
/**
 *
 * @return Is data available (in recvBuffer);
 */
bool recvSerialWithStartEnd() {
    while (Serial1.available()) {
        char r = Serial1.read();
        if (recvInProgress) {
            if (r == RECV_END) {
                recvInProgress = false;
                if ( currPos+1 < RECV_BUF_SIZE )
                    recvBuffer[currPos+1] = '\0';
                return true;
            } else {
                if (currPos >= RECV_BUF_SIZE) {
                    // error, message too long.
                    //      TODO what to do? currently we are throwing away all the buffer message and wait for next new start.
                    recvInProgress = false;
                    Serial1.println("\n\n\nThrew Away Data");
                    
                } else {
                    recvBuffer[currPos++] = r;
                    // Serial.println("\n\n\n DIDNT Threw Away Data");
                }
            }
        } else if (r == RECV_START) {
            recvInProgress = true;
            currPos = 0;
        }
        //delayMicroseconds(100);
    }
    return false;
}

void getJSONData(){
  // if (recvSerialWithStartEnd()) {
  //       // We have JSON available in recv_buffer
  //             //  Serial.print("JSON available: ");
  //             //  Serial.write(recvBuffer, RECV_BUF_SIZE);
  //             //  Serial.println("");
  //   DeserializationError error = deserializeJson(jsonDataIn, recvBuffer);
  //   if (error) {
  //     Serial.print(F("deserializeJson() failed: "));
  //     Serial.println(error.f_str());
  //       return;
  //   }
  // }
  // recvSerialWithStartEnd();  
  
  // String dat = Serial1.readStringUntil('&'); //this is for the old test UI
  
  // String dat1 = dat.replace(">","");
  // dat = dat.replace("<","");
  DeserializationError error = deserializeJson(jsonDataIn, packetBuffer);
  // int x = jsonDataIn["commandedSpeed"];
  // Serial.println(x);
  // Serial.println(dat);
}

void sendJSONData(int *switchStateArray){
  serialJSONOut="";
  // StaticJsonDocument<256> JSONdataOut;

  parseJSONData(switchStateArray);
  serializeJson(jsonDataOut, serialJSONOut);
  // Serial.println(serialJSONOut);
  sendUDP();
}

void sendJSONDataUI(int *switchStateArray){
  serialJSONUI="";
  // StaticJsonDocument<256> JSONdataOut;

  parseJSONDataUI(switchStateArray);
  serializeJson(jsonDataUI, serialJSONUI);
  Serial1.println(serialJSONUI);
}

void parseJSONDataUI(int *switchStateArray){
  jsonDataUI["Power"] = power;
  jsonDataUI["Left Door Command"] = switchStateArray[3];
  jsonDataUI["Right Door Command"] = switchStateArray[2];
  jsonDataUI["Service Brake Command"] = serviceBrakeCommand;
  jsonDataUI["Emergency Brake Command"] = switchStateArray[6];
  jsonDataUI["External Light Command"] = switchStateArray[5];
  jsonDataUI["Internal Light Command"] = switchStateArray[4];
  jsonDataUI["AC"] = 999;
  jsonDataUI["Station Announcement"] = "text";
  jsonDataUI["Engine State"] = switchStateArray[0];
  jsonDataUI["Emergency Brake State"] = emergencyBrakeState;
  jsonDataUI["Service Brake State"] = jsonDataIn["serviceBrakeState"];
  jsonDataUI["Internal Lights State"] = switchStateArray[4];
  jsonDataUI["External Lights State"] = switchStateArray[5];
  jsonDataUI["Left Door State"] = jsonDataIn["leftDoorState"];
  jsonDataUI["Right Door State"] = jsonDataIn["rightDoorState"];
  jsonDataUI["Station"] = (stationState) ? jsonDataIn["stationName"] : jsonDataIn["nextStationName"];
  jsonDataUI["Current Speed"] = jsonDataIn["currentSpeed"];
  jsonDataUI["Commanded Speed"] = jsonDataIn["commandedSpeed"];
  jsonDataUI["Manual Commanded Speed"] = manualCommandedSpeed;
  jsonDataUI["Authority"] = jsonDataIn["authority"];
  jsonDataUI["Speed Limit"] = 999;
  jsonDataUI["Temperature"] = 999;
  jsonDataUI["Communications Status"] = jsonDataIn["communicationsStatus"];
  jsonDataUI["Kp"] = Kp;
  jsonDataUI["Ki"] = Ki;
  
}

void parseJSONData(int *switchStateArray){
  jsonDataOut["power"] = power;
  jsonDataOut["leftDoorCommand"] = switchStateArray[3];
  jsonDataOut["rightDoorCommand"] = switchStateArray[2];
  jsonDataOut["serviceBrakeCommand"] = serviceBrakeCommand;
  jsonDataOut["emergencyBrakeCommand"] = emergencyBrakeState;
  jsonDataOut["externalLightCommand"] = switchStateArray[5];
  jsonDataOut["internalLightCommand"] = switchStateArray[4];
  jsonDataOut["stationAnnouncement"] = jsonDataIn["stationName"];
  jsonDataOut["isAtStation"] = stationState;
  int x = jsonDataOut["power"];
  Serial.print("JSON OUT:");
  Serial.println(x);
  
}
////////////////////////////////UDP Shit////////////////////////////////////
void setupUDP(){
  Ethernet.init(10);  // Most Arduino shields

  // start the Ethernet
  Ethernet.begin(mac);

  // Open serial communications and wait for port to open:
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  //startup sequence 
  Serial.println("Before UDP Begin");
  // start UDP to listen 
  //TODO:Implement this
  Udp.begin(27000);
  Serial.println("After UDP Begin");
  //Udp.endPacket();
}
void sendUDP(){
  Udp.beginPacket("192.168.1.2", 27001);
  char Buf[300];
  // Serial.println("Before conversion");
  serialJSONOut.toCharArray(Buf, 300);
  // Serial.println("After conversion");
  Udp.write(Buf);
  Udp.endPacket();
  // Serial.println("After write");
  // Serial.println(Udp.endPacket());
  // Serial.println("End of UDP Send");
}

bool readUDP(){

  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    // Serial.print("Received packet of size ");
    // Serial.println(packetSize);
    // Serial.print("From ");
    // IPAddress remote = Udp.remoteIP();
    // for (int i=0; i < 4; i++) {
    //   Serial.print(remote[i], DEC);
    //   if (i < 3) {
    //     Serial.print(".");
    //   }
    // }
    // Serial.print(", port ");
    // Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    Udp.read(packetBuffer, 600);
    // Serial.println("Contents:");
    // Serial.println(packetBuffer);
    return true;
  }else{
    return false;
  }
}

////////////////////////////////Drive Shit////////////////////////////////////


////////////////////////////////Drive Shit/////////////////////////////////////Move later TODO:move it
// int previousError = 0;
// int previousU = 0; 

// int calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
//   //power calculation here
//   int error = commandedSpeed - currentSpeed;

//   int power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
//   previousU = (dt/2000)*(error-previousError);
//   previousError = error;

//   return power;

// }


// bool calculateBrake(bool state){
//   return state;
// }



void drive(int dt){
    //this is the main drive function to make the train move. 
    //This also calls the power and brake functions
  autoDriveCommand = switchStateArray[1];//jsonDataIn["Manual Speed Override"];
  // Serial.println(autoDriveCommand);
  currentSpeed = jsonDataIn["currentSpeed"];
  commandedSpeed = jsonDataIn["commandedSpeed"];
  authority = jsonDataIn["authority"];
  if(autoDriveCommand){
    if (authority>0){
      autodrive(currentSpeed, commandedSpeed, dt);
    }else{
      power=0;
      serviceBrakeCommand = tControl.calculateBrake(true);
    }
    Serial.println(power);
  }else{
    manualCommandedSpeed = switchStateArray[8];
    autodrive(currentSpeed, manualCommandedSpeed, dt);
    // power = tControl.calculatePower(currentSpeed, commandedSpeed, dt, Kp, Ki);
    serviceBrakeCommand = tControl.calculateBrake((bool)switchStateArray[7]);
    if(serviceBrakeCommand || emergencyBrakeState){
      power=0; //set the power to 0 if service brake or emergency brake requested - redundancy for emergency brake
    }
  }

}

void autodrive(int currentSpeed, int commandedSpeed, int dt){
  //autodrive code
  int error = commandedSpeed - currentSpeed;
  // int dt=0;
  if(error>0){
    power = tControl.calculatePower(currentSpeed, commandedSpeed, dt, Kp, Ki);
    serviceBrakeCommand = tControl.calculateBrake(false);    
  }else if (error<0){
    serviceBrakeCommand = tControl.calculateBrake(true);
    power = tControl.calculatePower(0, 0, dt, Kp, Ki);
    power = 0;
  }else{
    power=0;
  }
}

bool emergencyBrake(){
  emergencyBrakeState = switchStateArray[6];
  return emergencyBrakeState; 
}


//==============BEACON SHIT================
void setStationState(){
  // # if isBeacon and !firstBeaconPassed, entering station
  if(isBeacon && !firstBeaconPassed){
    firstBeaconPassed = true;
    // #print("First Beacon Passed")
  }else if(!isBeacon && firstBeaconPassed){
    stationState = true;
      // #print("WE GOT TO A STATION")
  }      

  // # if isBeacon and stationState and !secondBeaconPassed, exiting station
  if(isBeacon && stationState && !secondBeaconPassed){
    secondBeaconPassed = true;
      // #print("Second Beacon Passed")
  }
      

  // # if !isBeacon and secondBeaconPassed, reset stationState and beaconPassed variables (left the station)
  if(!isBeacon && secondBeaconPassed){
    //  #print("Reset Data")
    stationState = false;
    firstBeaconPassed = false;
    secondBeaconPassed = false;
  }
     
}
//=========================================



