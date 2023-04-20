# Train Model Back End
import sys
import csv
import os
sys.path.append(__file__.replace("\TrainModelFolder\TrainModel.py", ""))

from random import randint
from math import cos, asin, exp
from datetime import *
from TrainModelFolder.TrainModelSignals import *
from Integration.TMTkMSignals import *
from Integration.TMTCSignals import *
from Integration.TimeSignals import *
from Integration.BlocksClass import *
from PyQt6.QtCore import *

class TrainModel():

    # Green Line Track Sections
    greenSection0  = [0, 63]    # Yard to Block 63
    greenSection1  = [63, 76]   # Sections K, L, and M
    greenSection2  = [77, 85]   # Section N
    greenSection2R = [85, 77]   # Section N Reverse
    greenSection3  = [86, 100]  # Sections O, P, Q
    greenSection4  = [101, 150] # Sections R, S, T, U, V, W, X, Y, Z
    greenSection5  = [29, 13]   # Sections F, E, D
    greenSection5R = [13, 29]   # Sections F, E, D Reverse
    greenSection6  = [12, 1]    # Sections C, B, A
    greenSection7  = [30, 57]   # Sections G, H, I
    greenSection8  = [58, 62]   # Section J
    greenSection9  = [57, 0]    # Block 57 to Yard

    # Red Line Track Sections
    redSection0   = [0, 9]   # Yard to Block 9
    redSection0R  = [9, 0]   # Block 9 to Yard
    redSection1   = [9, 1]   # Sections C, B, A
    redSection1R  = [1, 9]   # Sections C, B, A Reverse
    redSection2   = [16, 27] # Sections F, G, Part 1 of H
    redSection2R  = [27, 16] # Sections F, G, Part 1 of H Reverse
    redSection3   = [28, 32] # Part 2 of H
    redSection3R  = [32, 28] # Part 2 of H Reverse
    redSection4   = [33, 38] # Part 3 of H
    redSection4R  = [38, 33] # Part 3 of H Reverse
    redSection5   = [39, 43] # Part 4 of H
    redSection5R  = [43, 39] # Part 4 of H Reverse
    redSection6   = [44, 52] # Part 5 of H and Part 1 of J
    redSection6R  = [52, 44] # Part 5 of H and Part 1 of J Reverse
    redSection7   = [53, 66] # Part 2 of J, Sections K, L, M
    redSection7R  = [66, 53] # Part 2 of J, Sections K, L, M Reverse
    redSection8   = [67, 71] # Sections O, P, Q
    redSection8R  = [71, 67] # Sections O, P, Q Reverse
    redSection9   = [72, 76] # Sections R, S, T
    redSection9R  = [76, 72] # Sections R, S, T Revese
    redSection10  = [15, 10] # Sections E, D
    redSection10R = [10, 15] # Sections E, D Reverse

    # Dictionary of constants to be used througout the class
    constants = {
        "serviceBrake"       : -1.2,         # Deceleration due to the service brake in meters per second ^ 2
        "emergencyBrake"     : -2.73,        # Deceleration due to the emergency brake in meters per second ^ 2
        "mediumAcceleration" : 0.5,          # Medium acceleration used for initial time period acceleration in meters per second ^ 2
        "maxSpeed"           : 70,           # Maximum speed of the train in kilometers per hour
        "gravity"            : 9.81,         # Acceleration due to gravity in meters per second ^ 2
        "length"             : 32.2,         # Length of one instance of the Flexity 2 Train in meters
        "massOfTrain"        : 40900.0,      # Mass of an unloaded train car in kilograms
        "massOfHuman"        : 68.0389,      # Mass of a human for this simulation in kilograms
        "maxPassengers"      : 222,          # Maximum number of passengers that can be on the train at one time
        "friction"           : 0.006         # Coefficient of friction used for both static and dynamic friction
    }

    def __init__(self, trainId, Line):
        
        self.blocks = []

        # data variable to store all the data needed for the back end
        self.data = {
            "id"               : 0,              # Train ID for if there are multiple trains instantiated
            "rtc"              : "",             # Real Time Clock in ISO 8601 Format
            "prevRTC"          : "",             # Previous State RTC in ISO 8601 Format
            "simSpeed"         : 1,              # Simulation Speed of the system
            "passengers"       : 0,              # Number of passengers on the train
            "passengersOn"     : 0,              # Number of passengers getting on the train
            "passengersOff"    : 0,              # Number of passengers getting off the train
            "crew"             : 1,              # Number of crew members on the train (Default of driver and conductor)
            "underground"      : False,          # State of whether the train is underground or not
            "length"           : 0.0,            # Length of the Train in meters
            "mass"             : 40900.0,        # Mass of the Train, changes based on number of passengers, defaults to mass of an unloaded train, in kilograms
            "velocity"         : 0.0,            # Current Velocity of the Train in meters per second
            "acceleration"     : 0.0,            # Current Acceleration of the Train in meters per second ^ 2
            "prevVelocity"     : 0.0,            # Previous Velocity of the Train in meters per second
            "prevAcceleration" : 0.0,            # Previous Acceleration of the Train in meters per second ^ 2
            "power"            : 0.0,            # Power input from the Train Controller in watts
            "station"          : "The Yard",     # Name of the next Station 
            "atStation"        : False,          # State of whether the train is at a station or not
            "commStatus"       : True,           # True if all communications are good, false is communications are disabled
            "engineStatus"     : True,           # True if engine is operational, false if it is disabled
            "brakeStatus"      : True,           # True is the service brake is operational, false if it is disabled
            "eBrakeState"      : False,          # State of the emergency brake, True if engaged, False if disengaged
            "sBrakeState"      : False,          # State of the service brake, True if engaged, False if disengaged
            "lDoors"           : False,          # State of the left doors, True if doors are open, False if they are closed
            "rDoors"           : False,          # State of the right doors, True if doors are open, False if they are closed
            "iLights"          : False,          # State of the internal lights, True if they are on, False if they are off
            "eLights"          : False,          # State of the external lights, True if they are on, False if they are off
            "currTemp"         : 68.0,           # Current temperature inside the train in degrees fahrenheit
            "goalTemp"         : 68.0,           # Temperature goal given by the user in degrees fahrenehit
            "numCars"          : 1,              # Length of the train based on number of cars attached to the train
            "runOnce"          : False,          # Boolean used for calculating passengers on and off at a station
        }

        # Dictionary used for intercommunication between the track model and train model only
        self.trackData = {
            "currBlock"        : 0,              # Current block that the train is on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
            "prevBlock"        : 0,              # Previous block that the train was on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
            "distance"         : 0.0,            # Distance the train has traveled since the last time period in meters
            "remDistance"      : 0.1,            # Distance remaining in the current block, if any, in meters (Initialized as 10 meters for coming out of the yard)
            "switch"           : True,           # If the current block is attached to a switch, True if on a switch, false if otherwise
            "switchState"      : 1,              # State of the switch if the current block is attached to one (default is 0)
            "blockLength"      : 10.0,           # Length of the current block, provided by the Track Model
            "elevation"        : 0.0,            # Relative elevation increase of the block, provided by the Track Model
            "trainLine"        : "",             # Line the train is on
            "trackSection"     : [0, 0],         # Section of the track that the train is on
            "overflow"         : False,          # Overflow boolean used for current Block Calculations
            "backTrain"        : False,          # Whether the back of the train is in the previous block still or not
            "polarity"         : False,          # Polarity of the current block (0 if even, 1 if odd)
        }

        # Dictionary used for different eBrake States from train controller and user input
        self.eBrakes = {
            "user"               : False,        # State of the emergency brake from the passenger
            "trainController"    : False         # State of the emergency brake from the driver
        }

        # Dictionary for pass through data (Only data to be passed through the module and not used within)
        self.passThroughData = {
            "commandedSpeed"  : 0.0,                       # Commanded speed for the train in m/s
            "authority"       : 0,                         # Authority of the train in blocks
            "beacon"          : ["", 0, "", False, -1, 0, 0]  # Beacon Inputs from the most recent Beacon
        }

        self.TrainID = trainId
        self.trackData["trainLine"] = Line

        self.getBlocksData()

        # Signals from the Main UI
        trainSignals.commButtonPressedSignal.connect(self.communicationsFailure)
        trainSignals.engineButtonPressedSignal.connect(self.engineFailure)
        trainSignals.brakeButtonPressedSignal.connect(self.serviceBrakeFailure)
        trainSignals.eBrakePressedSignal.connect(self.emergencyBrakeDeceleration)
        trainSignals.tempChangedSignal.connect(self.tempChangeHandler)

        # Track Model Train Model Signals
        TMTkMSignals.authoritySignal.connect(self.authoritySignalHandler)
        TMTkMSignals.commandedSpeedSignal.connect(self.commandedSpeedSignalHandler)
        TMTkMSignals.passengersEnteringSignal.connect(self.passengersEnteringSignalHandler)
        TMTkMSignals.undergroundStateSignal.connect(self.undergroundStateSignalHandler)
        TMTkMSignals.beaconSignal.connect(self.beaconSignalHandler)
        TMTkMSignals.switchSignal.connect(self.switchSignalHandler)
        TMTkMSignals.switchStateSignal.connect(self.switchStateSignalHandler)
        TMTkMSignals.blockLengthSignal.connect(self.blockLengthSignalHandler)
        TMTkMSignals.elevationSignal.connect(self.elevationSignalHandler)

        # Train Controller Train Model Signals
        TMTCSignals.commandedPowerSignal.connect(self.commandedPowerSignalHandler)
        TMTCSignals.leftDoorCommandSignal.connect(self.leftDoorCommandSignalHandler)
        TMTCSignals.rightDoorCommandSignal.connect(self.rightDoorCommandSignalHandler)
        TMTCSignals.serviceBrakeCommandSignal.connect(self.serviceBrakeCommandSignalHandler)
        TMTCSignals.emergencyBrakeCommandSignal.connect(self.emergencyBrakeCommandSignalHandler)
        TMTCSignals.externalLightCommandSignal.connect(self.externalLightCommandSignalHandler)
        TMTCSignals.internalLightCommandSignal.connect(self.internalLightCommandSignalHandler)
        TMTCSignals.stationAnnouncementSignal.connect(self.stationAnnouncementSignalHandler)
        TMTCSignals.stationStateSignal.connect(self.stationStateSignalHandler)

        # Time From Main Signal
        rtcSignals.rtcSignal.connect(self.realTimeHandler)

        self.data["rtc"] = datetime.now().isoformat() + "0-05:00"
        self.data["prevRTC"] = datetime.now().isoformat() + "0-05:00"
        self.data["length"] = self.constants["length"] * self.data["numCars"]

    def getBlocksData(self):
        if self.trackData["trainLine"] == "Green":
            self.blocks = [0] * 151
            with open (os.path.join(sys.path[0], "..", "TrackModel", "GreenLine.csv")) as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if (row[0] == "BlockNo"):
                        continue
                    else:
                        self.blocks[int(row[0])] = blocks(int(row[0]), float(row[1]), float(row[5]), float(row[3]), bool(int(row[7])))
        elif self.trackData["trainLine"] == "Red":
            self.blocks = [0] * 77
            with open (os.path.join(sys.path[0], "..", "TrackModel", "RedLine.csv")) as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for row in rows:
                    if (row[0] == "BlockNo"):
                        continue
                    else:
                        self.blocks[int(row[0])] = blocks(int(row[0]), float(row[1]), float(row[5]), float(row[3]), bool(int(row[7])))

    def realTimeHandler(self, rtc):
        self.data["rtc"] = rtc

    def setFirstSection(self):
        if self.trackData["trainLine"] == "Green":
            self.trackData["trackSection"] = self.greenSection0
        elif self.trackData["trainLine"] == "Red":
            self.trackData["trackSection"] = self.redSection0

    # Data Handler for Outputs to the Train Controller
    def writeTMtoTC(self):
        TMTCSignals.commandedSpeedSignal.emit(self.TrainID, self.passThroughData["commandedSpeed"])
        TMTCSignals.currentSpeedSignal.emit(self.TrainID, self.data["velocity"])
        TMTCSignals.authoritySignal.emit(self.TrainID, self.passThroughData["authority"])
        TMTCSignals.undergroundSignal.emit(self.TrainID, self.data["underground"])
        TMTCSignals.temperatureSignal.emit(self.TrainID, self.data["currTemp"])
        if (self.passThroughData["beacon"][3] == 1):
            TMTCSignals.stationNameSignal.emit(self.TrainID, self.passThroughData["beacon"][0])
            TMTCSignals.platformSideSignal.emit(self.TrainID, self.passThroughData["beacon"][1])
            TMTCSignals.nextStationNameSignal.emit(self.TrainID, self.passThroughData["beacon"][2])
            TMTCSignals.blockCountSignal.emit(self.TrainID, self.passThroughData["beacon"][4])
            TMTCSignals.fromSwitchSignal.emit(self.TrainID, self.passThroughData["beacon"][5])
            TMTCSignals.switchBlockSignal.emit(self.TrainID, self.passThroughData["beacon"][6])
        TMTCSignals.isBeaconSignal.emit(self.TrainID, self.passThroughData["beacon"][3])
        TMTCSignals.externalLightsStateSignal.emit(self.TrainID, self.data["eLights"])
        TMTCSignals.internalLightsStateSignal.emit(self.TrainID, self.data["iLights"])
        TMTCSignals.leftDoorStateSignal.emit(self.TrainID, self.data["lDoors"])
        TMTCSignals.rightDoorStateSignal.emit(self.TrainID, self.data["rDoors"])
        TMTCSignals.serviceBrakeStateSignal.emit(self.TrainID, self.data["sBrakeState"])
        TMTCSignals.emergencyBrakeStateSignal.emit(self.TrainID, self.data["eBrakeState"])
        TMTCSignals.serviceBrakeStatusSignal.emit(self.TrainID, self.data["brakeStatus"])
        TMTCSignals.engineStatusSignal.emit(self.TrainID, self.data["engineStatus"])
        TMTCSignals.communicationsStatusSignal.emit(self.TrainID, self.data["commStatus"])
        TMTCSignals.polaritySignal.emit(self.TrainID, self.trackData["polarity"])

    # Data Handlers from Input from the Train Controller SW
    # Commanded Power input handler
    def commandedPowerSignalHandler(self, id, power):
        if (id == self.TrainID):
            self.data["power"] = power

    # Left Door Command input handler
    def leftDoorCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["lDoors"] = state

    # Right Door Command input handler
    def rightDoorCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["rDoors"] = state

    # Service Brake Command input handler
    def serviceBrakeCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["sBrakeState"] = state

    # Emergency Brake Command (Train Controller) input handler
    def emergencyBrakeCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.eBrakes["trainController"] = state

    # External Light Command input handler
    def externalLightCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["eLights"] = state

    # Internal Light Command input handler
    def internalLightCommandSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["iLights"] = state

    # Station Announcement input handler
    def stationAnnouncementSignalHandler(self, id, station):
        if (id == self.TrainID):
            self.data["station"] = station

    # Station State input handler
    def stationStateSignalHandler(self, id, atStation):
        if (id == self.TrainID):
            self.data["atStation"] = atStation

    # Data Handler for Outputs to the Track Model
    def writeTMtoTkM(self):
        TMTkMSignals.currBlockSignal.emit(self.TrainID, self.trackData["currBlock"], self.trackData["prevBlock"], self.trackData["overflow"], self.trackData["backTrain"])

    # Data Handlers for Inputs from the Track Model
    # Authority Input Handler
    def authoritySignalHandler(self, id, numBlocks):
        if (id == self.TrainID):
            self.passThroughData["authority"] = numBlocks
    
    # Commanded Speed Input Handler
    def commandedSpeedSignalHandler(self, id, cmdSpeed):
        if (id == self.TrainID):
            self.passThroughData["commandedSpeed"] = cmdSpeed

    # Passengers Entering Input Handler
    def passengersEnteringSignalHandler(self, id, passengers):
        if (id == self.TrainID):
            self.data["passengersOn"] = passengers
            self.passengersGettingOn()

    # Underground State Input Handler
    def undergroundStateSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.data["underground"] = state

    # Beacons Input Handler
    def beaconSignalHandler(self, id, stationName, platformSide, nextStationName, isBeacon, blockCount, fromSwitch, switchBlock):
        if (id == self.TrainID):
            self.passThroughData["beacon"][0] = stationName
            self.passThroughData["beacon"][1] = platformSide
            self.passThroughData["beacon"][2] = nextStationName
            self.passThroughData["beacon"][3] = isBeacon
            self.passThroughData["beacon"][4] = blockCount
            self.passThroughData["beacon"][5] = fromSwitch
            self.passThroughData["beacon"][6] = switchBlock

    # Switch Input Handler
    def switchSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.trackData["switch"] = state

    # Switch State Input Handler
    def switchStateSignalHandler(self, id, state):
        if (id == self.TrainID):
            self.trackData["switchState"] = state

    # Block Length Input Handler
    def blockLengthSignalHandler(self, id, length):
        if (id == self.TrainID):
            self.trackData["blockLength"] = length

    # Elevation Input Handler
    def elevationSignalHandler(self, id, height):
        if (id == self.TrainID):
            self.trackData["elevation"] = height

    # Function to run all internal methods when the method is called by the updater in the UI
    #def runFunctions(self): 
    #    #self.readTrainControllerToTrainModel()
    #    #self.readTrackModelToTrainModel()
    #    tempTimeDiff = self.findTimeDifference()
    #    self.failureStates()
    #    self.brakeCaclulator()
    #    self.findCurrentAcceleration(tempTimeDiff)
    #    self.findCurrentVelocity(tempTimeDiff)
    #    self.findCurrentDistance(tempTimeDiff)
    #    self.findBlockExiting()
    #    self.airConditioningControl()
    #    if self.data["atStation"]:
    #        self.passengersGettingOff()
    #        self.passengersGettingOn()
    #    self.findCurrentMass()
    #    if tempTimeDiff != 0:
    #        self.moveToPrevious()
    #    #self.writeTrainModelToTrackModel()
    #    #self.writeTrainModelToTrainController()
    #    self.writeTMtoTkM()
    #    self.writeTMtoTC()
        
    # Function to move the current velocity and acceleration to previous in order to calculate next time periods values
    def moveToPrevious(self):
        self.data["prevVelocity"] = self.data["velocity"]
        self.data["prevAcceleration"] = self.data["acceleration"]
        self.data["prevRTC"] = self.data["rtc"]

    # Finds the current acceleration of a train
    def findCurrentAcceleration(self, time = 1) :

        # Limits the power of the engine if it is > 120000
        if self.data["power"] > 120000:
            self.data["power"] = 120000
        
        # Limits the power of the engine if it is < 0
        if self.data["power"] < 0:
            self.data["power"] = 0

        # Find the force of friction and the force of mass on the train
        frictionalForce = -(self.data["mass"] * self.constants["gravity"] * self.constants["friction"] * cos(asin(self.trackData["elevation"] / self.trackData["blockLength"])))
        gravitationalForce = -(self.data["mass"] * self.constants["gravity"] * (self.trackData["elevation"] / self.trackData["blockLength"]))
        powerForce = 0
        brakeForce = 0

        # Deal with finding the force from the power input

        # If the train is not moving, but has power input, set the medium acceleration to 0.5 m/s^2 regardless of
        if (self.data["prevVelocity"] == 0.0) & (self.data["power"] > 0.0):
            #self.data["acceleration"] = self.constants["mediumAcceleration"]
            powerForce = self.constants["mediumAcceleration"] * self.data["mass"]
        
        # If the train is moving and has power input
        elif (self.data["power"] > 0.0):
            powerForce = self.data["power"] / self.data["prevVelocity"]
            if(powerForce > 4000000):
                powerForce = 120000
        

        # If the Service Brake is pulled
        if (self.data["sBrakeState"]):
            brakeForce = self.constants["serviceBrake"] * self.data["mass"]

        # If the Emergency Brake is pulled
        if (self.data["eBrakeState"]):
            brakeForce = self.constants["emergencyBrake"] * self.data["mass"]

        # Calculate the sum of the forces and current Acceleration
        forces = powerForce + brakeForce + frictionalForce + gravitationalForce
        tempAcceleration = forces / self.data["mass"]

        # Limit the acceleration to follow F = ma
        if (time > 0):
            self.data["acceleration"] = tempAcceleration if tempAcceleration <= (forces / self.data["mass"]) else (forces / self.data["mass"])

        # Limits the power of the engine
        #if self.data["power"] > 120000:
        #    self.data["power"] = 120000

        # If Emergency or service brakes are enabled, do not change acceleration
        #if (self.data["eBrakeState"] | self.data["sBrakeState"]):
        #    return
        
        # If the train is not moving and has no power input
        #if ((self.data["prevVelocity"] == 0.0) & (self.data["power"] == 0.0)):
        #    force = 0.0

        # If the train is not moving but has a power input
        #elif (self.data["prevVelocity"] == 0.0):
        #    force = self.data["mass"] * self.constants["mediumAcceleration"]

        # All other cases
        #else:
        #    force = self.data["power"] / self.data["prevVelocity"]

        # If the train is not on an incline or decline, use this calculation
        #if (self.trackData["elevation"] == 0.0):
        #    tempAcceleration = force / self.data["mass"]

        # If the train is on an incline or decline, use this calculation
        #else:
            # Calculating the effect of mass * gravity when on an incline
        #    tempAcceleration = (force - (self.data["mass"] * self.constants["gravity"] * (self.trackData["elevation"] / self.trackData["blockLength"]))) / self.data["mass"]

        # Limit the acceleration to something that is possible for the train according to F = ma
        #if (time > 0):
        #    self.data["acceleration"] = tempAcceleration if tempAcceleration <= (force / self.data["mass"]) else (force / self.data["mass"])

    # Finds the current velocity of a train
    def findCurrentVelocity(self, time = 1):
        currVelocity = self.data["prevVelocity"] + ((time / 2) * (self.data["acceleration"] + self.data["prevAcceleration"]))
        currVelocity = currVelocity if currVelocity >= 0 else 0.0
        self.data["velocity"] = currVelocity

    # Get distance since the last state update of the system
    def findCurrentDistance(self, time = 1):
        self.trackData["distance"] = ((time / 2) * (self.data["prevVelocity"] + self.data["velocity"]))

    # Find the difference in time between current iteration and previous iteration of data in seconds from ISO 8601 Format
    def findTimeDifference(self):
        if (self.data["prevRTC"] == "") & (self.data["rtc"] == ""):
            return 0
        if (self.data["prevRTC"] == "") & (self.data["rtc"] != ""):
            return 1
        currTime = datetime.fromisoformat(self.data["rtc"])
        prevTime = datetime.fromisoformat(self.data["prevRTC"])
        newTime = currTime - prevTime
        return float(newTime.total_seconds())

    # Finds the Block the train is on and the Block the train is exiting
    def findBlockExiting(self):
        # If the train overflowed, and we had to get a new blockLength
        if (self.trackData["overflow"]):
            tempOverflow = 100 - self.trackData["remDistance"]
            self.trackData["remDistance"] = self.trackData["blockLength"] - tempOverflow
            self.trackData["overflow"] = False
        
        # If the train is derailed (Block 333)
        if (self.trackData["currBlock"] == 333):
            return
        # Case if the distance traveled leaves you somewhere in the block you started in
        elif self.trackData["distance"] < self.trackData["remDistance"]:
            self.trackData["remDistance"] -= self.trackData["distance"]
            self.trackData["prevBlock"] = self.trackData["currBlock"]
            if ((self.trackData["blockLength"] - self.trackData["remDistance"]) < (self.data["length"] / 2)):
                self.trackData["backTrain"] = True
            else:
                self.trackData["backTrain"] = False

        # Case otherwise
        else:
            # Find total overflow distance into the next block
            tempDistance = self.trackData["distance"] - self.trackData["remDistance"]
            self.trackData["currBlock"] = self.findNextBlock()
            self.trackData["remDistance"] = 100 - tempDistance
            self.data["underground"] = self.blocks[self.trackData["currBlock"]].undergroundState
            self.trackData["blockLength"] = self.blocks[self.trackData["currBlock"]].blockLength
            self.trackData["elevation"] = self.blocks[self.trackData["currBlock"]].elevation
            self.trackData["polarity"] = self.trackData["currBlock"] % 2
            if (tempDistance < (self.data["length"] / 2)):
                self.trackData["backTrain"] = True
            else:
                self.trackData["backTrain"] = False
            self.trackData["overflow"] = True
            
    # Finds the next block in sequence based on a switch state saved internally
    def findNextBlock(self):
        # If the train is on the green line
        if self.trackData["trainLine"] == "Green":
            # If the train is in the yard, done with it's cycle
            if (self.trackData["trackSection"] == [0, 0]):
                self.trackData["prevBlock"] = self.trackData["currBlock"]
                return 0
            
            # If the train is on a switch block and the switch state is 0
            elif (self.trackData["switch"] == True) & (self.trackData["switchState"] == 0):

                # Cases for where the train would proceed normally
                if (self.trackData["currBlock"] == 76) | (self.trackData["currBlock"] == 85) | (self.trackData["currBlock"] == 13) | (self.trackData["currBlock"] == 29) | (self.trackData["currBlock"] == 57) | (self.trackData["currBlock"] == 62):
                    match self.trackData["currBlock"]:
                        case 76:
                            self.trackData["trackSection"] = self.greenSection2
                        case 85:
                            self.trackData["trackSection"] = self.greenSection3
                        case 13:
                            self.trackData["trackSection"] = self.greenSection6
                        case 29:
                            self.trackData["trackSection"] = self.greenSection7
                        case 57:
                            self.trackData["trackSection"] = self.greenSection8
                        case 62:
                            self.trackData["trackSection"] = self.greenSection1
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return self.trackData["trackSection"][0]
                
                # Cases for derailment
                elif (self.trackData["currBlock"] == 77) | (self.trackData["currBlock"] == 100) | (self.trackData["currBlock"] == 150) | (self.trackData["currBlock"] == 1) | (self.trackData["currBlock"] == 0):
                    print("Derailment1")
                    return 333
                
            # If the train is on a switch block and the switch state is 1
            elif (self.trackData["switch"] == True) & (self.trackData["switchState"] == 1):

                # Cases for derailment
                if (self.trackData["currBlock"] == 76) | (self.trackData["currBlock"] == 85) | (self.trackData["currBlock"] == 13) | (self.trackData["currBlock"] == 29) | (self.trackData["currBlock"] == 62):
                    print("Derailment2")
                    return 333
                
                # Cases where the train would proceed normally
                elif (self.trackData["currBlock"] == 77) | (self.trackData["currBlock"] == 100) | (self.trackData["currBlock"] == 150) | (self.trackData["currBlock"] == 1) | (self.trackData["currBlock"] == 57) | (self.trackData["currBlock"] == 0):
                    match self.trackData["currBlock"]:
                        case 77:
                            self.trackData["trackSection"] = self.greenSection4
                        case 100:
                            self.trackData["trackSection"] = self.greenSection2R
                        case 150:
                            self.trackData["trackSection"] = self.greenSection5
                        case 1:
                            self.trackData["trackSection"] = self.greenSection5R
                        case 57:
                            self.trackData["trackSection"] = [0, 0]
                            self.trackData["prevBlock"] = self.trackData["currBlock"]
                            return 0
                        case 0:
                            self.trackData["trackSection"] = self.greenSection1
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return self.trackData["trackSection"][0]
                
            # Case where the train needs to just increase block by 1
            else:
                if self.trackData["trackSection"][0] < self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] + 1)
                elif self.trackData["trackSection"][0] > self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] - 1)
        # Case if the train is on the red line
        elif self.trackData["trainLine"] == "Red":
            # If the train is in the yard, done with it's cycle
            if (self.trackData["trackSection"] == [0, 0]):
                self.trackData["prevBlock"] = self.trackData["currBlock"]
                return 0

            elif (self.trackData["switch"] == True) & (self.trackData["switchState"] == 0):
                if (self.trackData["currBlock"] == 0) | (self.trackData["currBlock"] == 9) | (self.trackData["currBlock"] == 10) | (self.trackData["currBlock"] == 15) | (self.trackData["currBlock"] == 16) | (self.trackData["currBlock"] == 27) | (self.trackData["currBlock"] == 28) | (self.trackData["currBlock"] == 32) | (self.trackData["currBlock"] == 33) | (self.trackData["currBlock"] == 38) | (self.trackData["currBlock"] == 39) | (self.trackData["currBlock"] == 43) | (self.trackData["currBlock"] == 44) | (self.trackData["currBlock"] == 52) | (self.trackData["currBlock"] == 53):
                    match self.trackData["currBlock"]:
                        case 0:
                            print("Derailment3")
                            return 333
                        case 9:
                            self.trackData["trackSection"] = self.redSection10R
                        case 10:
                            self.trackData["trackSection"] = self.redSection1
                        case 15:
                            self.trackData["trackSection"] = self.redSection2
                        case 16:
                            self.trackData["trackSection"] = self.redSection10
                        case 27:
                            self.trackData["trackSection"] = self.redSection3
                        case 28:
                            self.trackData["trackSection"] = self.redSection2R
                        case 32:
                            self.trackData["trackSection"] = self.redSection4
                        case 33:
                            self.trackData["trackSection"] = self.redSection3R
                        case 38:
                            self.trackData["trackSection"] = self.redSection5
                        case 39:
                            self.trackData["trackSection"] = self.redSection4R
                        case 43:
                            self.trackData["trackSection"] = self.redSection6
                        case 44:
                            self.trackData["trackSection"] = self.redSection5R
                        case 52:
                            self.trackData["trackSection"] = self.redSection7
                        case 53:
                            self.trackData["trackSection"] = self.redSection6R
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return self.trackData["trackSection"][0]

                elif (self.trackData["currBlock"] == 1) | (self.trackData["currBlock"] == 66) | (self.trackData["currBlock"] == 67) | (self.trackData["currBlock"] == 71) | (self.trackData["currBlock"] == 72) | (self.trackData["currBlock"] == 76):
                    print("Derailment4")
                    return 333
            elif (self.trackData["switch"] == True) & (self.trackData["switchState"] == 1):
                if (self.trackData["currBlock"] == 0) | (self.trackData["currBlock"] == 1) | (self.trackData["currBlock"] == 9)  | (self.trackData["currBlock"] == 16) | (self.trackData["currBlock"] == 27) | (self.trackData["currBlock"] == 33) | (self.trackData["currBlock"] == 38) | (self.trackData["currBlock"] == 44) | (self.trackData["currBlock"] == 52) | (self.trackData["currBlock"] == 66) | (self.trackData["currBlock"] == 67) | (self.trackData["currBlock"] == 71) | (self.trackData["currBlock"] == 72) | (self.trackData["currBlock"] == 76):
                    match self.trackData["currBlock"]:
                        case 0:
                            self.trackData["trackSection"] = self.redSection1
                        case 1:
                            self.trackData["trackSection"] = self.redSection2
                        case 9:
                            self.trackData["trackSection"] = [0, 0]
                            self.trackData["prevBlock"] = self.trackData["currBlock"]
                            return 0
                        case 16:
                            self.trackData["trackSection"] = self.redSection1R
                        case 27:
                            self.trackData["trackSection"] = self.redSection9R
                        case 33:
                            self.trackData["trackSection"] = self.redSection9
                        case 38:
                            self.trackData["trackSection"] = self.redSection8R
                        case 44:
                            self.trackData["trackSection"] = self.redSection8
                        case 52:
                            self.trackData["trackSection"] = self.redSection7R
                        case 66:
                            self.trackData["trackSection"] = self.redSection6R
                        case 67:
                            self.trackData["trackSection"] = self.redSection6
                        case 71:
                            self.trackData["trackSection"] = self.redSection4R
                        case 72:
                            self.trackData["trackSection"] = self.redSection4
                        case 76:
                            self.trackData["trackSection"] = self.redSection2R
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return self.trackData["trackSection"][0]
                elif (self.trackData["currBlock"] == 10) | (self.trackData["currBlock"] == 15) | (self.trackData["currBlock"] == 28) | (self.trackData["currBlock"] == 32) | (self.trackData["currBlock"] == 39) | (self.trackData["currBlock"] == 43) | (self.trackData["currBlock"] == 53):
                    print("Derailment5")
                    return 333
                        # Case where the train needs to just increase block by 1
            else:
                if self.trackData["trackSection"][0] < self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] + 1)
                elif self.trackData["trackSection"][0] > self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] - 1)
        else:
            print("IDK How I even got here")


    # Air Conditioning System that changes based on user input
    def airConditioningControl(self, time = 1):
        if self.data["currTemp"] < self.data["goalTemp"]:
            self.data["currTemp"] += (0.1 * time / 2)
        elif self.data["currTemp"] == self.data["goalTemp"]:
            self.data["currTemp"] += 0
        else:
            self.data["currTemp"] -= (0.1 * time / 2)
        self.data["currTemp"] = round(self.data["currTemp"], 2)

    # Find the current mass of the entire train including passengers 
    def findCurrentMass(self):
        self.data["mass"] = (self.constants["massOfTrain"] * self.data["numCars"]) + (self.constants["massOfHuman"] * (self.data["passengers"] + self.data["crew"]))

    # Handle Emergency Brake being pulled by the Passenger
    def emergencyBrakeDeceleration(self, id):
        if (id == self.TrainID):
            if (self.eBrakes["user"] == False):
                self.eBrakes["user"] = True
            else:
                self.eBrakes["user"] = False

    # Function to be called when updating the values to set the emergency brake state
    def brakeCaclulator(self):
        self.data["eBrakeState"] = self.eBrakes["user"] | self.eBrakes["trainController"]

    # Handle change in input from the user about temperature
    def tempChangeHandler(self, id, temp):
        if (id == self.TrainID):
            self.data["goalTemp"] = temp
            self.goalTemp = temp


    # Determines how many passengers get off at each station
    def passengersGettingOff(self):
        if (~self.data["runOnce"]):
            self.data["passengersOff"] = randint(0, self.data["passengers"])
            self.data["passengers"] -= self.data["passengersOff"]
            self.data["runOnce"] = True

    # Adds passengers getting on to total passengers
    def passengersGettingOn(self):
        if (self.data["passengers"] + self.data["passengersOn"]) > 222:
            self.data["passengers"] = 222
        else:
            self.data["passengers"] += self.data["passengersOn"]

    ##################
    # FAILURE STATES #
    ##################

    def failureStates(self):
        if self.data["commStatus"] == False:
            self.passThroughData["commandedSpeed"] = 0.0
            self.passThroughData["authority"] = 0
            self.passThroughData["beacon"] = ["", 0, "", False, -1, False]
        if self.data["engineStatus"] == False:
            self.data["power"] = 0.0
        if self.data["brakeStatus"] == False:
            self.data["sBrakeState"] = False

    # Handle loss of communications
    def communicationsFailure(self, id):
        if (id == self.TrainID):
            if self.data["commStatus"] == False:
                self.data["commStatus"] = True
            else:
                self.data["commStatus"] = False

    # Handle engine failure
    def engineFailure(self, id):
        if (id == self.TrainID):
            if self.data["engineStatus"] == False:
                self.data["engineStatus"] = True
            else:
                self.data["engineStatus"] = False
            self.data["power"] = 0.0

    # Handle service brake failure
    def serviceBrakeFailure(self, id):
        if (id == self.TrainID):
            if self.data["brakeStatus"] == False:
                self.data["brakeStatus"] = True
            else:
                self.data["brakeStatus"] = False
            self.data["sBrakeState"] = False