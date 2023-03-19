#include "Arduino.h"

Control::Control(){
    int previousError = 0;
    int previousU = 0; 
}
    
int Control::calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki){
    //power calculation here
    int error = commandedSpeed - currentSpeed;

    int power = Kp*error + Ki*(previousU + (dt/2)*(error-previousError));
    previousU = (dt/2000)*(error-previousError);
    previousError = error;

    return power;
}
    
    
bool Control::calculateBrake(bool state){
    return bool;
}