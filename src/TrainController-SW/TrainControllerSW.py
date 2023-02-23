# Main Class for the Train Controller Software

from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder

# TODO: add unit conversions class, doors must close after leaving station 

# Class for the TrainControllerSW
class TrainControllerSW:
    def __init__(self, commandedSpeed, currentSpeed, authority, inputTime, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        
        # Constants
        # serviceBrake deceleration = 1.2 m/s^2, e-brake deceleration = 2.73 m/s^2
        # Max Speed in km/hr
        self.MAX_SPEED = 70

        # Max Power in Watts
        self.MAX_POWER = 120000
        
        self.realTime = None
        self.previousTime = None
        self.currentTime = None
        self.commandedSpeedInternal = None
        self.manualMode = False

        # Power variables (ek1/uk1 = previous ek/uk, or e(k-1)/u(k-1) )
        self.ek = None
        self.ek1 = 0
        self.uk = None
        self.uk1 = 0
        
        self.T = 1
        self.Kp = 1
        self.Ki = 1

        # Variables to check states between mainEventLoops
        self.lightsEnabledPrevious = None
        self.undergroundStatePrevious = None
        
        self.inputs = Inputs(commandedSpeed, currentSpeed, authority, inputTime, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus)
        self.outputs = Outputs(power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement)
           

    # methods   
    
    # Writes all output variables to output JSON file
    def writeOutputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "w") as filename:
            (json.dump(self.outputs.__dict__, filename, indent=4))

    # Reads in all input fields from input JSON file and updates Input variables
    def readInputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWInputs.json"), "r") as filename:
            self.inputs = Inputs(**json.loads(filename.read()))
        self.convertTime()

    # Only used in Test UI and commandedSpeed manual input - writes to input file
    def writeInputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWInputs.json"), "w") as filename:
            (json.dump(self.inputs.__dict__, filename, indent=4))

    # Only used in Test UI - reads from output file
    def readOutputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "r") as filename:
            self.outputs = Outputs(**json.loads(filename.read()))

    # Calculates the power to output to the train model 
    def calculatePower(self):
        # ek = velocity error
        self.ek = self.inputs.commandedSpeed - self.inputs.currentSpeed
        
        # Don't update uk if at max power
        if (self.outputs.power < self.MAX_POWER):
            self.uk = self.uk1 + 0.5*self.T*(self.ek + self.ek1)
        else:
            self.uk = self.uk1

        # Final power calculation - don't send power while braking
        if(self.inputs.serviceBrakeState or self.inputs.emergencyBrakeState):
            self.outputs.power = 0
            self.ek = 0
            self.uk = 0
        else:
            self.outputs.power = self.Kp*self.ek + self.Ki*self.uk

        # 0 <= power <= 120000 Watts
        if(self.outputs.power > 120000):
            self.outputs.power = 120000
        elif(self.outputs.power < 0):
            self.outputs.power = 0
        else:
            self.outputs.power = self.outputs.power

        # Set ek1/uk1 to current ek/uk
        self.ek1 = self.ek
        self.uk1 = self.uk

    # Automatically opens/closes doors based on platformSide
    def autoUpdateDoorState(self):
        if(self.inputs.stationState == True and self.inputs.currentSpeed == 0):
            if(self.inputs.platformSide == 0):
                self.outputs.leftDoorCommand = True
                self.outputs.rightDoorCommand = False
            elif(self.inputs.platformSide == 1):
                self.outputs.leftDoorCommand = False
                self.outputs.rightDoorCommand = True
            elif(self.inputs.platformSide == 2):
                self.outputs.leftDoorCommand = True
                self.outputs.rightDoorCommand = True
            else:
                self.outputs.leftDoorCommand = False
                self.outputs.rightDoorCommand = False
    
    # Automatically turns on/off lights based on underground state
    # NOTE: update based on time of day? (currently always on between 8pm - 5am)
    def autoUpdateLights(self):
        if(self.inputs.undergroundState == True):
            self.outputs.externalLightCommand = True
            self.outputs.internalLightCommand = True
            self.undergroundStatePrevious = True
            self.lightsEnabledPrevious = True
        else:
            if(self.lightsEnabledPrevious == True and self.undergroundStatePrevious == True):
                self.outputs.externalLightCommand = False
                self.outputs.internalLightCommand = False
                self.undergroundStatePrevious = False
                self.lightsEnabledPrevious = False

        if(self.realTime.hour >= 20 or self.realTime.hour <= 5):
            self.outputs.externalLightCommand = True
            self.outputs.internalLightCommand = True

    # Automatically enable/disables the service brake
    def autoSetServiceBrake(self):
        if(self.inputs.commandedSpeed == 0):
            self.outputs.serviceBrakeCommand = True
        else:
            self.outputs.serviceBrakeCommand = False

    # Lowers commanded speed if it's higher than speed limit
    def stayBelowSpeedLimit(self):
        if(int(self.inputs.commandedSpeed) > int(self.inputs.speedLimit)):
            self.inputs.commandedSpeed = self.inputs.speedLimit

    # Converts input time string to time object ex "2023-02-20T04:52:48.3940347-05:00"
    def convertTime(self):
        inputTime = stringRemove(self.inputs.inputTime, 26)
        self.realTime = datetime.strptime(inputTime, "%Y-%m-%dT%H:%M:%S.%f%z")   

    def getEngineState(self):
        if(self.inputs.engineStatus == False):
            return "FAILURE"
        elif(self.inputs.engineState == False):
            return "OFF"
        elif(self.inputs.engineState == True):
            return "ON"
        else:
            return "ERROR: UNKNOWN STATE"

    def getEmergencyBrakeState(self):
        if(self.inputs.emergencyBrakeState == True):
            return "ENABLED"
        elif(self.inputs.emergencyBrakeState == False):
            return "DISABLED"
        else:
            return "ERROR: UNKNOWN STATE"

    def getServiceBrakeState(self):
        if(self.inputs.serviceBrakeStatus == False):
            return "FAILURE"
        elif(self.inputs.serviceBrakeState == True):
            return "ENABLED"
        elif(self.inputs.serviceBrakeState == False):
            return "DISABLED"
        else:
            return "ERROR: UNKNOWN STATE"

    def getLeftDoorState(self):
        if(self.inputs.leftDoorState == True):
            return "Opened"
        elif(self.inputs.leftDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    def getRightDoorState(self):
        if(self.inputs.rightDoorState == True):
            return "Opened"
        elif(self.inputs.rightDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    def getInternalLightsState(self):
        if(self.inputs.internalLightsState == True):
            return "ON"
        elif(self.inputs.internalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"

    def getExternalLightsState(self):
        if(self.inputs.externalLightsState == True):
            return "ON"
        elif(self.inputs.externalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"
        
# class for TrainController ouputs
class Inputs:
    def __init__(self, commandedSpeed, currentSpeed, authority, inputTime, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus):
        # Inputs
        self.commandedSpeed = commandedSpeed
        self.currentSpeed = currentSpeed
        self.authority = authority
        self.inputTime = str(inputTime)
        self.undergroundState = undergroundState
        self.speedLimit = speedLimit
        self.temperature = temperature
        self.engineState = engineState
        self.stationState = stationState
        self.stationName = stationName
        self.platformSide = platformSide
        self.externalLightsState = externalLightsState
        self.internalLightsState = internalLightsState
        self.leftDoorState = leftDoorState
        self.rightDoorState = rightDoorState
        self.serviceBrakeState = serviceBrakeState
        self.emergencyBrakeState = emergencyBrakeState
        self.serviceBrakeStatus = serviceBrakeStatus
        self.engineStatus = engineStatus
        self.communicationsStatus = communicationsStatus

# class for TrainController inputs
class Outputs:
    def __init__(self, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        # outputs
        self.power = power
        self.leftDoorCommand = leftDoorCommand
        self.rightDoorCommand = rightDoorCommand
        self.serviceBrakeCommand = serviceBrakeCommand
        self.emergencyBrakeCommand = emergencyBrakeCommand
        self.externalLightCommand = externalLightCommand
        self.internalLightCommand = internalLightCommand
        self.stationAnnouncement = stationAnnouncement
        
# Function to remove character from a string at nth position
def stringRemove(string, n):  
      first = string[: n]   
      last = string[n+1:]  
      return first + last