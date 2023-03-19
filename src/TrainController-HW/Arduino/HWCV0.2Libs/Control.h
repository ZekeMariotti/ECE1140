#ifndef Control_h
#define Control_h

#include "Arduino.h"

class Control
{
private:
    /* data */
    int previousError;
    int previousU; 
public:
    Control();
    calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki);
    calculateBrake(bool state);
};

#endif