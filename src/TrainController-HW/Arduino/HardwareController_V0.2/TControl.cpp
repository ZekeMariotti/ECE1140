#include "Arduino.h"
#include "TControl.h"
#include <PID_v1.h>

// int previousError = 0;
// int previousU = 0; 
double Setpoint, Input, Output;
double lKp, lKi, lKd;
PID myPID(&Input, &Output, &Setpoint, lKp, lKi, lKd, DIRECT);

TControl::TControl(){
    previousError = 0;
    previousU = 0; 
    // double Setpoint, Input, Output;
    // double lKp=2, _Ki=5, _Kd=0;
    
    myPID.SetMode(AUTOMATIC);
    
}
    
unsigned long TControl::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
    //power calculation here
    int error = commandedSpeed - currentSpeed;
    // Serial.println(error);
    // Serial.println(Kp*error + Ki*(previousU + (dt/2)*(error-previousError)));

    if((Kp*error + Ki*(previousU + (dt/2)*(error-previousError)))<120000){
      // unsigned long power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
      unsigned long power = Kp*error;
      previousU = (dt/2)*(error-previousError);
      previousError = error;    
      // Serial.println(power);
      // Serial.println(Kp);
      // Serial.println(Ki);
      // Serial.println(error);
      return power;  
    }else{
      // Serial.println(120000);
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
    


double TControl::calculatePower2(int currentSpeed, int commandedSpeed, float dt, unsigned int Kp, unsigned int Ki){
  Setpoint = commandedSpeed;
  Input = currentSpeed;
  lKp=(double)Kp;
  lKi=(double)Ki;
  lKd=0;
  // myPID.SetSampleTime(dt);
  myPID.Compute();
  Serial.println(Input);
  Serial.println(Output);
  if(Output>120000){
    return 120000;  
  }else if(Output<0){
    return 0;  
  }else{
    // Serial.println(120000);
    return Output;
  }

}
    
bool TControl::calculateBrake(bool state){
    return state;
}