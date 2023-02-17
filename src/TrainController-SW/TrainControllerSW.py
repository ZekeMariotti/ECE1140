# Main Class for the Train Controller Software

from datetime import time
from distutils.cmd import Command
import sys
import os
import json
from json import JSONEncoder



# Class for the TrainControllerSW
class TrainControllerSW:
    # Constructor 
    def __init__(self, commandedSpeed, currentSpeed, authority, time, undergroundState, speedLimit, temperature, engineState, 
                 stationState, stationName, platformSide, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        # inputs
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

        # outputs
        self.power = power
        self.leftDoorCommand = leftDoorCommand
        self.rightDoorCommand = rightDoorCommand
        self.serviceBrakeCommand = serviceBrakeCommand
        self.emergencyBrakeCommand = emergencyBrakeCommand
        self.externalLightCommand = externalLightCommand
        self.internalLightCommand = internalLightCommand
        self.stationAnnouncement = stationAnnouncement   

    # methods   
    
    def writeOutputs(self):
        print(json.dumps(self.__dict__))
        with open(os.path.join(sys.path[0], "TrainControllerSWOutputs.json"), "w") as filename:
            filename.write("Test")


    def readInputs(self):
        with open(os.path.join(sys.path[0], "TrainControllerSWInputs.json"), "r") as filename:
            print(filename.read())

    def getEngineState(self):
        if(self.engineState == 0):
            return "OFF"
        elif(self.engineState == 1):
            return "ON"
        elif(self.engineState == 2):
            return "FAILURE"
        else:
            return "ERROR: UNKNOWN STATE"

    def getEmergencyBrakeState(self):
        if(self.emergencyBrakeState == False):
            return "DISABLED"
        elif(self.emergencyBrakeState == True):
            return "ENABLED"
        else:
            return "ERROR: UNKNOWN STATE"

    def getServiceBrakeState(self):
        if(self.emergencyBrakeState == 0):
            return "DISABLED"
        if(self.emergencyBrakeState == 1):
            return "ENABLED"
        if(self.emergencyBrakeState == 2):
            return "FAILURE"
        else:
            return "ERROR: UNKNOWN STATE"

    def getLeftDoorState(self):
        if(self.leftDoorState == True):
            return "Opened"
        elif(self.rightDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    def getRightDoorState(self):
        if(self.rightDoorState == True):
            return "Opened"
        elif(self.rightDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    def getInternalLightsState(self):
        if(self.internalLightsState == True):
            return "ON"
        elif(self.internalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"

    def getExternalLightsState(self):
        if(self.externalLightsState == True):
            return "ON"
        elif(self.externalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"
        