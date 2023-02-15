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
        nextStationName = None
        platformSide = None
        externalLightState = None
        internalLightState = None
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
        

