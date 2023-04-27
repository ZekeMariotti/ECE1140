# Main Class for the Train Controller Software

from datetime import *
from distutils.cmd import Command
import sys
import os
import __main__


sys.path.append(__file__.replace("\TrainControllerSoftware\TrainControllerSW.py", ""))

import csv
from Inputs import Inputs
from Outputs import Outputs
import Integration.Conversions as Conversions
from Integration.TMTCSignals import *
from Integration.TimeSignals import *
from Integration.BlocksClass import *

from json import JSONEncoder

# Class for the TrainControllerSW
class TrainControllerSW:
    def __init__(self, trainId, line, commandedSpeed, currentSpeed, authority, inputTime, undergroundState, temperature, 
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
        TMTCSignals.blockCountSignal.connect(self.blockCountSignalHandler)
        TMTCSignals.fromSwitchSignal.connect(self.fromSwitchSignal)
        TMTCSignals.switchBlockSignal.connect(self.switchBlockSignal)
        TMTCSignals.polaritySignal.connect(self.polaritySignal)


        # Train id and line
        self.trainId = trainId
        self.line = line

        # Internal Variables
        self.stationState = False
        self.atSwitchBlock = False
        self.firstBeaconPassed = False
        self.secondBeaconPassed = False
        self.firstSwitchBeaconPassed = False
        self.secondSwitchBeaconPassed = False
        self.speedLimit = 100
        self.commandedSpeedManual = 0
        self.manualMode = False
        self.simulationSpeed = 1 

        # Beacon data
        self.blockList = [0]*2
        self.blockCount = 1
        self.nextBlock = 0
        self.switchBlock = 0
        self.blockCountDirection = 1
        self.countUpOrDown = 0
        self.polarity = False
        self.previousPolarity = False

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
        TMTCSignals.emergencyBrakeCommandSignal.emit(self.trainId, self.outputs.emergencyBrakeCommand)
        TMTCSignals.leftDoorCommandSignal.emit(self.trainId, self.outputs.leftDoorCommand)
        TMTCSignals.rightDoorCommandSignal.emit(self.trainId, self.outputs.rightDoorCommand)
        TMTCSignals.serviceBrakeCommandSignal.emit(self.trainId, self.outputs.serviceBrakeCommand)
        TMTCSignals.externalLightCommandSignal.emit(self.trainId, self.outputs.externalLightCommand)
        TMTCSignals.internalLightCommandSignal.emit(self.trainId, self.outputs.internalLightCommand)

        if(self.stationState):
            TMTCSignals.stationAnnouncementSignal.emit(self.trainId, self.inputs.stationName)
        else:
            TMTCSignals.stationAnnouncementSignal.emit(self.trainId, self.inputs.nextStationName)

        TMTCSignals.stationStateSignal.emit(self.trainId, self.stationState)

    def getBlocksData(self):
        if (__main__.__file__[-7:] == "main.py"):
            greenPath = os.path.join(sys.path[0], "TrackModel", "GreenLine.csv")
            redPath = os.path.join(sys.path[0], "TrackModel", "RedLine.csv")
        else:   
            greenPath = os.path.join(sys.path[0], "..", "TrackModel", "GreenLine.csv")
            redPath = os.path.join(sys.path[0], "..", "TrackModel", "RedLine.csv")

        if self.line == "Green":
            self.blockList = [0] * 151
            self.blockCount = 62
            self.blockCountDirection = 1
            self.inputs.nextStationName = "GLENBURY"
            self.outputs.stationAnnouncement = "GLENBURY"
            with open (greenPath) as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if (row[0] == "BlockNo"):
                        continue
                    else:
                        self.blockList[int(row[0])] = blocks(int(row[0]), float(row[1]), float(row[5]), float(row[3]), bool(int(row[7])))
        elif self.line == "Red":
            self.blockList = [0] * 77
            self.blockCount = 10
            self.blockCountDirection = -1
            self.inputs.nextStationName = "SHADYSIDE"
            self.outputs.stationAnnouncement = "SHADYSIDE"
            with open(redPath) as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if (row[0] == "BlockNo"):
                        continue
                    else:
                        self.blockList[int(row[0])] = blocks(int(row[0]), float(row[1]), float(row[5]), float(row[3]), bool(int(row[7])))    

    # Determines whether the train is at a station or not
    def setStationState(self):
        # If self.inputs.stationName != "" beacon is at a station
        if (self.inputs.stationName != "0"):
            # if isBeacon and !firstBeaconPassed, entering station
            if(self.inputs.isBeacon == True and self.firstBeaconPassed == False):
                self.firstBeaconPassed = True
            elif(self.inputs.isBeacon == False and self.firstBeaconPassed == True):
                self.stationState = True

            # if isBeacon and stationState and !secondBeaconPassed, exiting station
            if(self.inputs.isBeacon == True and self.stationState == True and self.secondBeaconPassed == False):
                self.secondBeaconPassed = True

            # if !isBeacon and secondBeaconPassed, reset stationState and beaconPassed variables (left the station)
            if(self.inputs.isBeacon == False and self.secondBeaconPassed == True):
                self.stationState = False
                self.firstBeaconPassed = False
                self.secondBeaconPassed = False

    # Increments or decrements block count after a polarity change
    def checkBlockPolarity(self):
        if (self.polarity != self.previousPolarity):
            self.blockCount += self.blockCountDirection
            self.previousPolarity = self.polarity

    # Decides what to set the current block to based on data from beacons and switch blocks 
    def setCurrentBlock(self):
        self.checkBlockPolarity()

        # If self.switchBlock != -1, train is at a switch beacon
        if (self.switchBlock != -1):
            # if isBeacon and !firstSwitchBeaconPassed, entering station
            if (self.inputs.isBeacon == True and self.firstSwitchBeaconPassed == False):
                self.firstSwitchBeaconPassed = True
            elif (self.inputs.isBeacon == False and self.firstSwitchBeaconPassed == True):
                self.atSwitchBlock = True

            # if isBeacon and atSwitchBlock and !secondSwitchBeaconPassed, exiting station
            if(self.inputs.isBeacon == True and self.atSwitchBlock == True and self.secondSwitchBeaconPassed == False):
                self.secondSwitchBeaconPassed = True

            # if !isBeacon and secondSwitchBeaconPassed, reset atSwitchBlock and beaconPassed variables (left the switch)
            if(self.inputs.isBeacon == False and self.secondSwitchBeaconPassed == True):
                self.atSwitchBlock = False
                self.firstSwitchBeaconPassed = False
                self.secondSwitchBeaconPassed = False

                if (self.nextBlock > 0):
                    self.blockCount = self.nextBlock

                if (self.countUpOrDown == 1):
                    self.blockCountDirection = -1
                else:
                    self.blockCountDirection = 1

        # Set current block
        if (self.atSwitchBlock == True and self.switchBlock > 0):
            self.blockCount = self.switchBlock

    # Calculates the power to output to the train model 
    def calculatePower(self):
        # Set T value
        T = self.currentTime - self.previousTime
        self.T = T.total_seconds()

        # Set commanded speed based on low authority (3, 2, or 1 blocks)
        match self.inputs.authority:
            case 3:
                self.inputs.commandedSpeed = Conversions.milesPerHourToMetersPerSecond(20)
            case 2:
                self.inputs.commandedSpeed = Conversions.milesPerHourToMetersPerSecond(15)
            case 1:
                self.inputs.commandedSpeed = Conversions.milesPerHourToMetersPerSecond(10)

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
        else:
            self.outputs.externalLightCommand = False
            self.outputs.internalLightCommand = False

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
        try:
            self.speedLimit = Conversions.kmPerHourToMetersPerSecond(self.blockList[self.blockCount].speedLimit)
        except Exception as ex:
            self.getBlocksData()

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
        
    # Signal handlers
    def rtcSignalHandler(self, rtcString):
        self.inputs.inputTime = rtcString
        self.convertTime()

    def commandedSpeedSignalHandler(self, id, cmdSpeed):
        if(self.trainId == id):
            if (cmdSpeed < 0):
                cmdSpeed = 0

            self.inputs.commandedSpeed = cmdSpeed
    
    def currentSpeedSignalHandler(self, id, currSpeed):
        if(self.trainId == id):
            self.inputs.currentSpeed = currSpeed

    def authoritySignalHandler(self, id, auth):
        if(self.trainId == id):
            if (auth < 0):
                auth = 0

            self.inputs.authority = auth

    def undergroundSignalHandler(self, id, undgnd):
        if(self.trainId == id):
            self.inputs.undergroundState = undgnd

    def temperatureSignalHandler(self, id, temp):
        if(self.trainId == id):
            self.inputs.temperature = temp

    def stationNameSignalHandler(self, id, statName):
        if(self.trainId == id and statName != "0"):
            self.inputs.stationName = statName

    def platformSideSignalHandler(self, id, platSide):
        if(self.trainId == id):
            self.inputs.platformSide = platSide

    def nextStationNameSignalHandler(self, id, nxtStatName):
        if(self.trainId == id and nxtStatName != "0"):
            self.inputs.nextStationName = nxtStatName

    def isBeaconSignalHandler(self, id, isBeac):
        if(self.trainId == id):
            self.inputs.isBeacon = isBeac
            if (isBeac):
                print(f'stationName: {self.inputs.stationName}, platform: {self.inputs.platformSide}, nextStation: {self.inputs.nextStationName}, IsBeacon: {self.inputs.isBeacon}, outwardBlock: {self.nextBlock}, up/down: {self.countUpOrDown}, switchBlock: {self.switchBlock} ')
            self.setStationState()
            self.setCurrentBlock()

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
            if (emgBrk == True and self.outputs.emergencyBrakeCommand == False):
                self.outputs.emergencyBrakeCommand = True
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

    def blockCountSignalHandler(self, id, nxtBlk):
        if(self.trainId == id):
            self.nextBlock = nxtBlk
        
    def fromSwitchSignal(self, id, countUpOrDown):
        if((self.trainId == id) and (countUpOrDown != -1)):
            self.countUpOrDown = countUpOrDown

    def switchBlockSignal(self, id, swtchBlk):
        if(self.trainId == id):
            self.switchBlock = swtchBlk
        
    def polaritySignal(self, id, plrty):
        if(self.trainId == id):
            self.polarity = plrty
            self.checkBlockPolarity()
        
# Function to remove character from a string at nth position
def stringRemove(string, n):  
      first = string[: n]   
      last = string[n+1:]  
      return first + last