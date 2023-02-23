
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
// #include "drive.cpp"
// #include "control.cpp"

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


//output variables, 
int power, serviceBrakeCommand, emergencyBrakeState, autoDriveCommand, currentSpeed, commandedSpeed; 

int prevTime = 0; 

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
<<<<<<< HEAD
  int currTime = millis();
  int dt = currTime-prevTime;
  updateSwitchStates(switchStateArray);
  drive(dt);
  emergencyBrake();
  // automaticSpeedControl();
  // delay(10);
  prevTime = currTime;
=======
  updateSwitchStates(switchStateArray);
  drive(dt);
  emergencyBrake();
  // automaticSpeedControl();
  // delay(10);
>>>>>>> 817da9a (Proof of concept for test UI and Main UI)
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
<<<<<<< HEAD
}

void sendJSONData(int *switchStateArray){
  serialJSONOut="";
  // StaticJsonDocument<256> JSONdataOut;

  parseJSONData(switchStateArray);
  serializeJson(jsonDataOut, serialJSONOut);
  Serial.println(serialJSONOut);
}

void parseJSONData(int *switchStateArray){
  jsonDataOut["Power"] = power;
  jsonDataOut["Left Door Command"] = switchStateArray[3];
  jsonDataOut["Right Door Command"] = switchStateArray[2];
  jsonDataOut["Service Brake Command"] = serviceBrakeCommand;
  jsonDataOut["Emergency Brake Command"] = switchStateArray[6];
  jsonDataOut["External Light Command"] = switchStateArray[5];
  jsonDataOut["Internal Light Command"] = switchStateArray[4];
  jsonDataOut["AC"] = 999;
  jsonDataOut["Station Announcement"] = "text";
  jsonDataOut["Engine State"] = switchStateArray[0];
  jsonDataOut["Emergency Brake State"] = emergencyBrakeState;
  jsonDataOut["Service Brake State"] = jsonDataIn["Service Brake State"];
  jsonDataOut["Internal Lights State"] = switchStateArray[4];
  jsonDataOut["External Lights State"] = switchStateArray[5];
  jsonDataOut["Left Door State"] = jsonDataIn["Left Door State"];
  jsonDataOut["Right Door State"] = jsonDataIn["Right Door State"];
  jsonDataOut["Station"] = "text";
  jsonDataOut["Current Speed"] = jsonDataIn["Current Speed"];
  jsonDataOut["Commanded Speed"] = jsonDataIn["Commanded Speed"];
  jsonDataOut["Authority"] = jsonDataIn["Authority"];
  jsonDataOut["Speed Limit"] = jsonDataIn["Speed Limit"];
  jsonDataOut["Temperature"] = 999;
  jsonDataOut["Communications Status"] = 999;
  
>>>>>>> 817da9a (Proof of concept for test UI and Main UI)
}

////////////////////////////////Drive Shit/////////////////////////////////////Move later TODO:move it
int previousError = 0;
int previousU = 0; 

int calculatePower(int currentSpeed, int commandedSpeed, float dt){
  //power calculation here
  int Kp = 1;
  int Ki = 0.1;
  int error = commandedSpeed - currentSpeed;

  int power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
  previousU = (dt/2000)*(error-previousError);
  previousError = error;

  return power;

}

void automaticSpeedControl(){

}

bool calculateBrake(bool state){
  return state;
}



void drive(int dt){
    //this is the main drive function to make the train move. 
    //This also calls the power and brake functions
  autoDriveCommand = jsonDataIn["Manual Speed Override"];
  currentSpeed = jsonDataIn["Current Speed"];
  commandedSpeed = jsonDataIn["Commanded Speed"];
  if(true){
    autodrive(currentSpeed, commandedSpeed, dt);
  }else{
    power=1000;        
  }

}

void autodrive(int currentSpeed, int commandedSpeed, int dt){
  //autodrive code
  int error = commandedSpeed - currentSpeed;
  // int dt=0;
  if(error>0){
    power = calculatePower(currentSpeed, commandedSpeed, dt);
    serviceBrakeCommand = calculateBrake(false);    
  }else if (error<0){
    serviceBrakeCommand = calculateBrake(true);
    power = calculatePower(0, 0, dt);
    power = 0;
  }else{
    power=0;
  }
}

bool emergencyBrake(){
  emergencyBrakeState = switchStateArray[6];
  return emergencyBrakeState; 
=======
}

void sendJSONData(int *switchStateArray){
  serialJSONOut="";
  // StaticJsonDocument<256> JSONdataOut;

  parseJSONData(switchStateArray);
  serializeJson(jsonDataOut, serialJSONOut);
  Serial.println(serialJSONOut);
}

void parseJSONData(int *switchStateArray){
  jsonDataOut["Power"] = power;
  jsonDataOut["Left Door Command"] = switchStateArray[3];
  jsonDataOut["Right Door Command"] = switchStateArray[2];
  jsonDataOut["Service Brake Command"] = serviceBrakeCommand;
  jsonDataOut["Emergency Brake Command"] = switchStateArray[6];
  jsonDataOut["External Light Command"] = switchStateArray[5];
  jsonDataOut["Internal Light Command"] = switchStateArray[4];
  jsonDataOut["AC"] = 999;
  jsonDataOut["Station Announcement"] = "text";
  jsonDataOut["Engine State"] = switchStateArray[0];
  jsonDataOut["Emergency Brake State"] = emergencyBrakeState;
  jsonDataOut["Service Brake State"] = jsonDataIn["Service Brake State"];
  jsonDataOut["Internal Lights State"] = switchStateArray[4];
  jsonDataOut["External Lights State"] = switchStateArray[5];
  jsonDataOut["Left Door State"] = jsonDataIn["Left Door State"];
  jsonDataOut["Right Door State"] = jsonDataIn["Right Door State"];
  jsonDataOut["Station"] = "text";
  jsonDataOut["Current Speed"] = jsonDataIn["Current Speed"];
  jsonDataOut["Commanded Speed"] = jsonDataIn["Commanded Speed"];
  jsonDataOut["Authority"] = jsonDataIn["Authority"];
  jsonDataOut["Speed Limit"] = jsonDataIn["Speed Limit"];
  jsonDataOut["Temperature"] = 999;
  jsonDataOut["Communications Status"] = 999;
  
>>>>>>> 817da9a (Proof of concept for test UI and Main UI)
}

