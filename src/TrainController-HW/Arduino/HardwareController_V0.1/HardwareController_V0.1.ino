
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

unsigned long update_period = 1000.0f / 50.0f; // in ms
unsigned long tsLastLoop = millis();
long tsUsed; // in ms


//Global and system wide variables 
int switchStateArray[NUMBEROFSWITCHES];
StaticJsonDocument<768> jsonDataIn;
StaticJsonDocument<768> jsonDataOut;
String serialJSONOut;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial1.begin(115200);
  
  //input setup for control interface
  setSwitches();
  updateSwitchStates(switchStateArray);
  // engineState = 
}

void loop() {
  // put your main code here, to run repeatedly:
  getJSONData();
  // delay(1000);
  updateSwitchStates(switchStateArray);
  // delay(10);
  sendJSONData(switchStateArray);
  
  // tsUsed = millis() - tsLastLoop;
  //   if (update_period > tsUsed) {
  //       // we still have some time remained
  //       delay(update_period - tsUsed);
  //   } else {
  //       Serial.print("too slow: remain_t (ms) =");
  //       Serial.println((long)update_period - tsUsed);
  //   }
  //   tsLastLoop = millis();

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
  String dat = Serial1.readStringUntil('&');
  // String dat1 = dat.replace(">","");
  // dat = dat.replace("<","");
  DeserializationError error = deserializeJson(jsonDataIn, dat);
  int x = jsonDataIn["Authority"];
  Serial.println(x);
  Serial.println(dat);
}

void sendJSONData(int *switchStateArray){
  serialJSONOut="";
  // StaticJsonDocument<256> JSONdataOut;

  parseJSONData(switchStateArray);
  serializeJson(jsonDataOut, serialJSONOut);
  Serial.println(serialJSONOut);
}

void parseJSONData(int *switchStateArray){
  jsonDataOut["Power"] = 10;
  jsonDataOut["Left Door Command"] = switchStateArray[3];
  jsonDataOut["Right Door Command"] = switchStateArray[2];
  jsonDataOut["Service Brake Command"] = 999;
  jsonDataOut["Emergency Brake Command"] = switchStateArray[6];
  jsonDataOut["External Light Command"] = switchStateArray[5];
  jsonDataOut["Internal Light Command"] = switchStateArray[4];
  jsonDataOut["AC"] = 999;
  jsonDataOut["Station Announcement"] = "text";
  jsonDataOut["Engine State"] = 999;
  jsonDataOut["Emergency Brake State"] = 999;
  jsonDataOut["Service Brake State"] = 999;
  jsonDataOut["Internal Lights State"] = 999;
  jsonDataOut["External Lights State"] = 999;
  jsonDataOut["Left Door State"] = 999;
  jsonDataOut["Right Door State"] = 999;
  jsonDataOut["Station"] = "text";
  jsonDataOut["Current Speed"] = 999;
  jsonDataOut["Commanded Speed"] = 999;
  jsonDataOut["Authority"] = jsonDataIn["Authority"];
  jsonDataOut["Speed Limit"] = 999;
  jsonDataOut["Temperature"] = 999;
  jsonDataOut["Communications Status"] = 999;
  
}

