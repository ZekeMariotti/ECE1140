#include "Arduino.h"
#include "Drive.h"
#include "TControl.h"

Drive::Drive(TControl *_tc, int *_Kp, int *_Ki, int *_power, 
    int *_serviceBrakeCommand, int *_emergencyBrakeState, int *_switchStateArray){
     tc=_tc;
     Kp=_Kp;
     Ki=_Ki;
     power=_power;
     serviceBrakeCommand=_serviceBrakeCommand;
     emergencyBrakeState=_emergencyBrakeState;
     switchStateArray=_switchStateArray;
}
    
void Drive::autodrive(int currentSpeed, int commandedSpeed, int dt){
    //autodrive code
    int error = commandedSpeed - currentSpeed;
    // int dt=0;
    if(error>0){
        *power = tc->calculatePower(currentSpeed, commandedSpeed, dt, *Kp, *Ki);
        *serviceBrakeCommand = (int)tc->calculateBrake(false);    
    }else if (error<0){
        *serviceBrakeCommand = (int)tc->calculateBrake(true);
        *power = tc->calculatePower(0, 0, dt, *Kp, *Ki);
        *power = 0;
    }else{
        *power=0;
    }
}
    
    
// bool Drive::drive(int dt){
//     //this is the main drive function to make the train move. 
//     //This also calls the power and brake functions
//     autoDriveCommand = switchStateArray[1];//jsonDataIn["Manual Speed Override"];
//     currentSpeed = jsonDataIn["Current Speed"];
//     commandedSpeed = jsonDataIn["Commanded Speed"];
//     if(autoDriveCommand){
//         autodrive(currentSpeed, commandedSpeed, dt);
//     }else{
//         power = tControl.calculatePower(currentSpeed, commandedSpeed, dt, Kp, Ki);  
//         serviceBrakeCommand = tControl.calculateBrake((bool)switchStateArray[7]);
//         if(serviceBrakeCommand || emergencyBrakeState){
//             power=0; //set the power to 0 if service brake or emergency brake requested - redundancy for emergency brake
//         }
//     }

// }