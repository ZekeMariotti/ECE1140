#ifndef TControl_h
#define TControl_h

#include "Arduino.h"

class TControl
{
private:
    /* data */
    unsigned int previousError;
    unsigned int previousU; 
public:
    TControl();
    unsigned long calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki);
    bool calculateBrake(bool state);
};

#endif