#ifndef Drive_h
#define Drive_h

#include "Arduino.h"

class Drive
{
private:
    /* data */
public:
    Drive();
    drive(int dt);
    autodrive(int currentSpeed, int commandedSpeed, int dt);
};

#endif