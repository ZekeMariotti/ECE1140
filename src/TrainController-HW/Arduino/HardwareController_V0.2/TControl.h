#ifndef TControl_h
#define TControl_h

#include "Arduino.h"
#include <PID_v1.h>

class TControl
{
private:
    /* data */
    unsigned int previousError;
    unsigned int previousU; 
    // double Setpoint, Input, Output;
    // double lKp, lKi, lKd;
    // PID myPID;
    // myPID.SetMode(AUTOMATIC);
public:
    TControl();
    unsigned long calculatePower(int currentSpeed, int commandedSpeed, float dt, int Kp, int Ki);
    double calculatePower2(int currentSpeed, int commandedSpeed, float dt, unsigned int Kp, unsigned int Ki);
    bool calculateBrake(bool state);
};

#endif