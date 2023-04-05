# Main Class for the Train Controller Software

from datetime import *
from distutils.cmd import Command
import sys
import os


sys.path.append(__file__.replace("\TrainControllerSoftware\TrainControllerSW.py", ""))

import json
from Inputs import Inputs
from Outputs import Outputs
import Integration.Conversions as Conversions
from Integration.TMTCSignals import *
from Integration.TimeSignals import *

from json import JSONEncoder

# Class for the TrainControllerSW
class TrainControllerSW:
    def __init__(self, trainId, commandedSpeed, currentSpeed, authority, inputTime, undergroundState, temperature, 
                 stationName, platformSide, nextStationName, isBeacon, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        
        # Signals
        rtcSignals.rtcSignal.connect(self.rtcSignalHandler)
        TMTCSignals.commandedSpeedSignal.connect(self.commandedSpeedSignalHandler)
        TMTCSignals.currentSpeedSignal.connect(self.currentSpeedSignalHandler)
        TMTCSignals.authoritySignal.connect(self.authoritySignalHandler)
        TMTCSignals.undergroundSignal.connect(self.undergroundSignalHandler)
        TMTCSignals.temperatureSignal.connect(self.temperatureSignalHandler)
        TMTCSignals.stationNameSignal.connect(self.stationNameSignalHandler)
        TMTCSignals.platformSideSignal.connect(self.platformSideSignalHandler)
        TMTCSignals.nextStationNameSignal.connect(self.nextStationNameSignalHandler)
        TMTCSignals.isBeaconSignal.connect(self.isBeaconSignalHandler)
        TMTCSignals.externalLightsStateSignal.connect(self.externalLightsStateSignalHandler)
        TMTCSignals.internalLightsStateSignal.connect(self.internalLightsStateSignalHandler)
        TMTCSignals.leftDoorStateSignal.connect(self.leftDoorStateSignalHandler)
        TMTCSignals.rightDoorStateSignal.connect(self.rightDoorStateSignalHandler)
        TMTCSignals.serviceBrakeStateSignal.connect(self.serviceBrakeStateSignalHandler)
        TMTCSignals.emergencyBrakeStateSignal.connect(self.emergencyBrakeStateSignalHandler)
        TMTCSignals.serviceBrakeStatusSignal.connect(self.serviceBrakeStatusSignalHandler)
        TMTCSignals.engineStatusSignal.connect(self.engineStatusSignalHandler)
        TMTCSignals.communicationsStatusSignal.connect(self.communicationsStatusSignalHandler)      

        # Train id
        self.trainId = trainId

        # Internal Variables
        self.stationState = False
        self.firstBeaconPassed = False
        self.secondBeaconPassed = False
        self.exitBeacon = False
        self.speedLimit = 100
        self.commandedSpeedManual = 0
        self.manualMode = False
        self.simulationSpeed = 1        

        # Constants
        # Max Speed in km/hr
        self.MAX_SPEED = 70

        # Max Power in Watts
        self.MAX_POWER = 120000

        # Time variables
        self.realTime = datetime
        self.previousTime = datetime
        self.currentTime = datetime     

        # Power variables (ek1/uk1 = previous ek/uk, or e(k-1)/u(k-1) )
        self.ek = None
        self.ek1 = 0
        self.uk = None
        self.uk1 = 0
        
        self.T = timedelta
        self.Kp = 50000
        self.Ki = 2500

        # Variables to check states between mainEventLoops
        self.lightsEnabledPrevious = None
        self.undergroundStatePrevious = None
        
        self.inputs = Inputs(commandedSpeed, currentSpeed, authority, inputTime, undergroundState, temperature, 
                 stationName, platformSide, nextStationName, isBeacon, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus)
        self.outputs = Outputs(power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement)
        
        # Convert initial time
        self.convertTime()
        
           

    # methods   

    def writeOutputs(self):
        TMTCSignals.commandedPowerSignal.emit(self.trainId, self.outputs.power)
        TMTCSignals.leftDoorCommandSignal.emit(self.trainId, self.outputs.leftDoorCommand)
        TMTCSignals.rightDoorCommandSignal.emit(self.trainId, self.outputs.rightDoorCommand)
        TMTCSignals.serviceBrakeCommandSignal.emit(self.trainId, self.outputs.serviceBrakeCommand)
        TMTCSignals.emergencyBrakeCommandSignal.emit(self.trainId, self.outputs.emergencyBrakeCommand)
        TMTCSignals.externalLightCommandSignal.emit(self.trainId, self.outputs.externalLightCommand)
        TMTCSignals.internalLightCommandSignal.emit(self.trainId, self.outputs.internalLightCommand)

        if(self.stationState):
            TMTCSignals.stationAnnouncementSignal.emit(self.trainId, self.inputs.stationName)
        else:
            TMTCSignals.stationAnnouncementSignal.emit(self.trainId, self.inputs.nextStationName)

        TMTCSignals.stationStateSignal.emit(self.trainId, self.stationState)

    # Signal handlers
    def rtcSignalHandler(self, rtcString):
        self.inputs.inputTime = rtcString
        self.convertTime()

    def commandedSpeedSignalHandler(self, id, cmdSpeed):
        if(self.trainId == id):
            self.inputs.commandedSpeed = cmdSpeed
    
    def currentSpeedSignalHandler(self, id, currSpeed):
        if(self.trainId == id):
            self.inputs.currentSpeed = currSpeed

    def authoritySignalHandler(self, id, auth):
        if(self.trainId == id):
            self.inputs.authority = auth

    def undergroundSignalHandler(self, id, undgnd):
        if(self.trainId == id):
            self.inputs.undergroundState = undgnd

    def temperatureSignalHandler(self, id, temp):
        if(self.trainId == id):
            self.inputs.temperature = temp

    def stationNameSignalHandler(self, id, statName):
        if(self.trainId == id):
            self.inputs.stationName = statName

    def platformSideSignalHandler(self, id, platSide):
        if(self.trainId == id):
            self.inputs.platformSide = platSide

    def nextStationNameSignalHandler(self, id, nxtStatName):
        if(self.trainId == id):
            self.inputs.nextStationName = nxtStatName

    def isBeaconSignalHandler(self, id, isBeac):
        if(self.trainId == id):
            #if (self.trainId == 2):
            #    print("isBeacon in Train Controller: ", isBeac)
            self.inputs.isBeacon = isBeac
            self.setStationState()

    def externalLightsStateSignalHandler(self, id, extLight):
        if(self.trainId == id):
            self.inputs.externalLightsState = extLight

    def internalLightsStateSignalHandler(self, id, intLight):
        if(self.trainId == id):
            self.inputs.internalLightsState = intLight

    def leftDoorStateSignalHandler(self, id, lftDoor):
        if(self.trainId == id):
            self.inputs.leftDoorState = lftDoor

    def rightDoorStateSignalHandler(self, id, rghtDoor):
        if(self.trainId == id):
            self.inputs.rightDoorState = rghtDoor

    def serviceBrakeStateSignalHandler(self, id, srvcBrk):
        if(self.trainId == id):
            self.inputs.serviceBrakeState = srvcBrk

    def emergencyBrakeStateSignalHandler(self, id, emgBrk):
        if(self.trainId == id):
            self.inputs.emergencyBrakeState = emgBrk

    def serviceBrakeStatusSignalHandler(self, id, srvcBrkStatus):
        if(self.trainId == id):
            self.inputs.serviceBrakeStatus = srvcBrkStatus

    def engineStatusSignalHandler(self, id, engStatus):
        if(self.trainId == id):
            self.inputs.engineStatus = engStatus

    def communicationsStatusSignalHandler(self, id, comStatus):
        if(self.trainId == id):
            self.inputs.communicationsStatus = comStatus

    # Determines whether the train is at a station or not
    def setStationState(self):
        # if isBeacon and !firstBeaconPassed, entering station
        if(self.inputs.isBeacon == True and self.firstBeaconPassed == False):
            self.firstBeaconPassed = True
            #print("First Beacon Passed")
        elif(self.inputs.isBeacon == False and self.firstBeaconPassed == True):
            self.stationState = True
            #print("WE GOT TO A STATION")

        # if isBeacon and stationState and !secondBeaconPassed, exiting station
        if(self.inputs.isBeacon == True and self.stationState == True and self.secondBeaconPassed == False):
            self.secondBeaconPassed = True
            #print("Second Beacon Passed")

        # if !isBeacon and secondBeaconPassed, reset stationState and beaconPassed variables (left the station)
        if(self.inputs.isBeacon == False and self.secondBeaconPassed == True):
            #print("Reset Data")
            self.stationState = False
            self.firstBeaconPassed = False
            self.secondBeaconPassed = False

    # Calculates the power to output to the train model 
    def calculatePower(self):
        # Set T value
        T = self.currentTime - self.previousTime
        self.T = T.total_seconds()
        #print(self.T)
        #print(f'prevTime: {self.previousTime.time()}')
        #print(f'currTime: {self.currentTime.time()}\n')

        # Temporary set T to fixed value
        #self.T = timedelta(0, 0, 0, 100).total_seconds()

        # ek = velocity error
        if(self.manualMode == True):
            self.ek = float(self.commandedSpeedManual) - float(self.inputs.currentSpeed)
        else:
            self.ek = float(self.inputs.commandedSpeed) - float(self.inputs.currentSpeed)
        
        # Don't update uk if at max power
        if (self.outputs.power < self.MAX_POWER):
            self.uk = float(self.uk1) + float(0.5*self.T*(self.ek + self.ek1))
        else:
            self.uk = self.uk1

        # Final power calculation - don't send power while braking
        if(self.inputs.serviceBrakeState or self.inputs.emergencyBrakeState):
            self.outputs.power = 0
            self.ek = 0
            self.uk = 0
        else:
            self.outputs.power = float(self.Kp*self.ek) + float(self.Ki*self.uk)

        # 0 <= power <= 120000 Watts
        if (self.inputs.authority == 0):
            self.outputs.power = 0
        elif(self.outputs.power > 120000):
            self.outputs.power = 120000
        elif(self.outputs.power < 0):
            self.outputs.power = 0
        else:
            self.outputs.power = round(self.outputs.power, 1)

        # If currentSpeed > commandedSpeed, power = 0
        if(self.manualMode == True):
            if(self.inputs.currentSpeed > self.commandedSpeedManual):
                self.outputs.power = 0
        else:
            if(self.inputs.currentSpeed > self.inputs.commandedSpeed):
                self.outputs.power = 0

        # Set ek1/uk1 to current ek/uk
        self.ek1 = self.ek
        self.uk1 = self.uk

    # Automatically opens/closes doors based on platformSide and stationState
    def autoUpdateDoorState(self):
        if(self.stationState == True and self.inputs.currentSpeed == 0 and self.inputs.commandedSpeed == 0):
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
        if (self.inputs.authority == 0):
            self.outputs.serviceBrakeCommand = True
        elif (self.inputs.commandedSpeed == 0):   # ADDED IF FOR COMMANDED SPEED
            self.outputs.serviceBrakeCommand = True
        elif(self.inputs.currentSpeed > self.inputs.commandedSpeed + 0.5):
            self.outputs.serviceBrakeCommand = True
        else:
            self.outputs.serviceBrakeCommand = False

    # Lowers commanded speed if it's higher than speed limit
    def stayBelowSpeedLimitAndMaxSpeed(self):
        if(float(self.inputs.commandedSpeed) > float(self.speedLimit)):
            self.inputs.commandedSpeed = self.speedLimit
        elif(float(self.inputs.commandedSpeed) > Conversions.kmPerHourToMetersPerSecond(self.MAX_SPEED)):
            self.inputs.commandedSpeed = Conversions.kmPerHourToMetersPerSecond(self.MAX_SPEED)

    # Runs when there is a communications failure
    def failureMode(self):
        if(self.inputs.communicationsStatus == False):
            self.outputs.emergencyBrakeCommand = True   
        elif(self.inputs.serviceBrakeStatus == False):
            self.outputs.emergencyBrakeCommand = True
        elif(self.inputs.engineStatus == False):
            self.outputs.emergencyBrakeCommand = True   

    # Converts input time string to time object ex "2023-02-20T04:52:48.3940347-05:00"
    def convertTime(self):
        inputTime = stringRemove(self.inputs.inputTime, 26)
        self.realTime = datetime.strptime(inputTime, "%Y-%m-%dT%H:%M:%S.%f%z")   

    # Returns a string that represents the state of the engine
    def getEngineState(self):
        if(self.inputs.engineStatus == False):
            return "FAILURE"
        elif(self.inputs.engineStatus == True):
            return "ON"
        else:
            return "ERROR: UNKNOWN STATE"
    
    # Returns a string that represents the state of the emergency brake
    def getEmergencyBrakeState(self):
        if(self.inputs.emergencyBrakeState == True):
            return "ENABLED"
        elif(self.inputs.emergencyBrakeState == False):
            return "DISABLED"
        else:
            return "ERROR: UNKNOWN STATE"

    # Returns a string that represents the state of the service brake
    def getServiceBrakeState(self):
        if(self.inputs.serviceBrakeStatus == False):
            return "FAILURE"
        elif(self.inputs.serviceBrakeState == True):
            return "ENABLED"
        elif(self.inputs.serviceBrakeState == False):
            return "DISABLED"
        else:
            return "ERROR: UNKNOWN STATE"

    # Returns a string that represents the state of the left door
    def getLeftDoorState(self):
        if(self.inputs.leftDoorState == True):
            return "Opened"
        elif(self.inputs.leftDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    # Returns a string that represents the state of the right door
    def getRightDoorState(self):
        if(self.inputs.rightDoorState == True):
            return "Opened"
        elif(self.inputs.rightDoorState == False):
            return "Closed"
        else:
            return "ERROR: UNKNOWN STATE"

    # Returns a string that represents the state of the internal lights
    def getInternalLightsState(self):
        if(self.inputs.internalLightsState == True):
            return "ON"
        elif(self.inputs.internalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"

    # Returns a string that represents the state of the external lights
    def getExternalLightsState(self):
        if(self.inputs.externalLightsState == True):
            return "ON"
        elif(self.inputs.externalLightsState == False):
            return "OFF"
        else:
            return "ERROR: UNKNOWN STATE"
        
# Function to remove character from a string at nth position
def stringRemove(string, n):  
      first = string[: n]   
      last = string[n+1:]  
      return first + last