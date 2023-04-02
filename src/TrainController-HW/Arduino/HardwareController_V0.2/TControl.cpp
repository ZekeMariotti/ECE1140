#include "Arduino.h"
#include "TControl.h"

// int previousError = 0;
// int previousU = 0; 

TControl::TControl(){
    previousError = 0;
    previousU = 0; 
}
    
unsigned long TControl::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
    //power calculation here
    int error = commandedSpeed - currentSpeed;

    if(Kp*error + Ki*(previousU + (dt/2)*(error-previousError))>120000){
      unsigned long power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
      previousU = (dt/2)*(error-previousError);
      previousError = error;    
      Serial.println(power);
      return power;  
    }else{
      Serial.println(120000);
      return 120000;
    }

  }

  // unsigned long TControl::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
  //   //power calculation here
  //   int error = commandedSpeed - currentSpeed;

  //   unsigned long power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
  //   previousU = (dt/2)*(error-previousError);
  //   previousError = error;

  //   Serial.println(power);
  //   if (power>999999){
  //     return 120000; 
  //   }else{
  //     return power;
  //   }
  // }

// unsigned long TControl::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
//     //power calculation here
//     int error = commandedSpeed - currentSpeed;

//     unsigned long power = Kp*error;
//     if (power>999999){
//       Serial.println(power);
//       Serial.println(error);
//       return 120000; 
//     }else{
//       Serial.println(power);
//       Serial.println(error);
//       return power;
//     }
// }
    
    
bool TControl::calculateBrake(bool state){
    return state;
}