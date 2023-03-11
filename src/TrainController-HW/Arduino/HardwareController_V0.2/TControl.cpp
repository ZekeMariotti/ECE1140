#include "Arduino.h"
#include "TControl.h"

// int previousError = 0;
// int previousU = 0; 

TControl::TControl(){
    previousError = 0;
    previousU = 0; 
}
    
int TControl::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
    //power calculation here
    int error = commandedSpeed - currentSpeed;

    int power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
    previousU = (dt/2000)*(error-previousError);
    previousError = error;

    return power;
}
    
    
bool TControl::calculateBrake(bool state){
    return state;
}