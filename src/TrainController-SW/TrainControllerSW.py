# Main Class for the Train Controller Software

from datetime import *
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder

# TODO: add manual speed override toggle, add unit conversions class, 
    # automatically: calculate power formula, update doors, update external lights, set service brake,
    #                display communications error, display correct current/next station, import RTC as a datetime type, 
    #                update currentTime and previousTime during each mainTimer loop, 

# Class for the TrainControllerSW
class TrainControllerSW:
    def __init__(self, commandedSpeed, currentSpeed, authority, time, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        
        self.MAX_SPEED = 70
        
        self.inputs = Inputs(commandedSpeed, currentSpeed, authority, time, undergroundState, speedLimit, temperature, engineState, 
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

    # Only used in Test UI - writes to input file
    def writeInputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWInputs.json"), "w") as filename:
            (json.dump(self.inputs.__dict__, filename, indent=4))

    # Only used in Test UI - reads from output file
    def readOutputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "r") as filename:
            self.outputs = Outputs(**json.loads(filename.read()))

    # Calculates the power to output to the train model based on currentSpeed, commandedSpeed, ...
    def calculatePower(self):
        self.power = None

    # Automatically opens/closes doors based on platformSide
    def autoUpdateDoorState(self):
        self.outputs.leftDoorCommand = None
        self.outputs.rightDoorCommand = None
    
    # Automatically turns on/off external lights based on underground state
    # NOTE: update based on time of day?
    def autoUpdateExternalLights(self):
        self.outputs.externalLightCommand = None

    # Automatically enable/disables the service brake based on currentSpeed, commandedSpeed, ...
    def autoSetServiceBrake(self):
        self.outputs.serviceBrakeCommand = None
            

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
        elif(self.inputs.rightDoorState == False):
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
    def __init__(self, commandedSpeed, currentSpeed, authority, time, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus):
        # Inputs
        self.commandedSpeed = commandedSpeed
        self.currentSpeed = currentSpeed
        self.authority = authority
        self.time = time
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