#ifndef Drive_h
#define Drive_h

#include "Arduino.h"
#include "TControl.h"

class Drive
{
private:
    /* data */
    TControl *tc;
    int *Kp;
    int *Ki;
    int *power;
    int *serviceBrakeCommand;
    int *emergencyBrakeState;
    int *switchStateArray;
public:
    Drive(TControl *_tc, int *_Kp, int *_Ki, int *_power, 
    int *_serviceBrakeCommand, int *_emergencyBrakeState, int *_switchStateArray);
    void autodrive(int currentSpeed, int commandedSpeed, int dt);
    void drive(int dt);
};

#endif