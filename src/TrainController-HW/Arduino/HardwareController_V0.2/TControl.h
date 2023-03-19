#ifndef TControl_h
#define TControl_h

#include "Arduino.h"

class TControl
{
private:
    /* data */
    int previousError;
    int previousU; 
public:
    TControl();
    int calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki);
    bool calculateBrake(bool state);
};

#endif