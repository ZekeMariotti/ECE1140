# Main Class for the Train Controller Software

from datetime import time
from distutils.cmd import Command
import sys



# Class for the TrainControllerSW
class TrainControllerSW():
    # Constructor 
    def __init__(self):
        # inputs
        commandedSpeed = None
        currentSpeed = None
        authority = None
        time = None
        undergroundState = None
        speedLimit = None
        temperature = None
        engineState = None
        stationState = None
        stationName = None
        platformSide = None
        externalLightsState = None
        internalLightsState = None
        leftDoorState = None
        rightDoorState = None
        serviceBrakeState = None
        emergencyBrakeState = None
        serviceBrakeStatus = None
        engineStatus = None
        communicationsStatus = None

        # outputs
        power = None
        leftDoorCommand = None
        rightDoorCommand = None
        serviceBrakeCommand = None
        emergencyBrakeCommand = None
        externalLightCommand = None
        internalLightCommand = None
        stationAnnouncement = None   

    # methods
    def writeOutputs(self):
        filename = open("TrainControllerSWOutputs.json", "w")
        filename.write("Test")


    def readInputs(self):
        test=None

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
        