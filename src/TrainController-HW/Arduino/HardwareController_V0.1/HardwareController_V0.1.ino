
#define ENGINESWITCH 22
#define AUTODRIVESWITCH 23
#define RIGHTDOORSWITCH 24
#define LEFTDOORSWITCH 25
#define INTERIORLIGHTSWITCH 26
#define EXTERIORLIGHTSWICH 27
#define EMERGENCYBRAKESWITCH 28
#define SERVICEBRAKESWITCH 29
#define SPEEDPOT A0
#define BRAKEPOT A1

#define NUMBEROFSWITCHES 10

// we use includes below define so we can use definitions in library when needed
// #include "ui.h"
#include <ArduinoJson.h>
#include <StreamUtils.h>


//Global and system wide variables 
int switchStateArray[NUMBEROFSWITCHES];
StaticJsonDocument<768> JSONdataIn;
StaticJsonDocument<256> JSONdataOut;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  //input setup for control interface
  setSwitches();
  updateSwitchStates(switchStateArray);
  // engineState = 
}

void loop() {
  // put your main code here, to run repeatedly:

}

void updateSwitchStates(int *switchStateArray){
  switchStateArray[0]=digitalRead(ENGINESWITCH);
  switchStateArray[1]=digitalRead(AUTODRIVESWITCH);
  switchStateArray[2]=digitalRead(RIGHTDOORSWITCH);
  switchStateArray[3]=digitalRead(LEFTDOORSWITCH);
  switchStateArray[4]=digitalRead(INTERIORLIGHTSWITCH);
  switchStateArray[5]=digitalRead(EXTERIORLIGHTSWICH);
  switchStateArray[6]=digitalRead(EMERGENCYBRAKESWITCH);
  switchStateArray[7]=digitalRead(SERVICEBRAKESWITCH);
  switchStateArray[8]=analogRead(SPEEDPOT);
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
    while (Serial.available()) {
        char r = Serial.read();
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
                    Serial.println("\n\n\nThrew Away Data");
                    
                } else {
                    recvBuffer[currPos++] = r;
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
  recvSerialWithStartEnd();  
  DeserializationError error = deserializeJson(JSONdataIn, recvBuffer);
  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return;
  }
}

void sendJSONData(){
  JsonObject dataOut = doc.createNestedObject();
}

