# Train Model Back End

from random import randint
from math import cos, asin
from datetime import *
from TrainModelSignals import *
from PyQt6.QtCore import *
import sys
import os
import json
import csv

class TrainModel():

    # data variable to store all the data needed for the back end
    data = {
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
    }

    # Dictionary used for intercommunication between the track model and train model only
    trackData = {
        "currBlock"        : 0,              # Current block that the train is on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
        "prevBlock"        : 0,              # Previous block that the train was on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
        "distance"         : 0.0,            # Distance the train has traveled since the last time period in meters
        "remDistance"      : 10.0,           # Distance remaining in the current block, if any, in meters (Initialized as 10 meters for coming out of the yard)
        "switch"           : True,           # If the current block is attached to a switch, True if on a switch, false if otherwise
        "switchState"      : 0,              # State of the switch if the current block is attached to one (default is 0)
        "blockLength"      : 10.0,           # Length of the current block, provided by the Track Model
        "elevation"        : 0.0,            # Relative elevation increase of the block, provided by the Track Model
        "trainLine"        : "Green",        # Line the train is on
        "trackSection"     : [0, 63]         # Section of the track that the train is on
    }

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
        "friction"           : 0.6           # Coefficient of friction used for both static and dynamic friction
    }

    # Dictionary used for different eBrake States from train controller and user input
    eBrakes = {
        "user"               : False,        # State of the emergency brake from the passenger
        "trainController"    : False         # State of the emergency brake from the driver
    }

    # Dictionary for pass through data (Only data to be passed through the module and not used within)
    passThroughData = {
        "commandedSpeed"  : 0.0,                   # Commanded speed for the train in m/s
        "speedLimit"      : 0.0,                   # Speed limit of the train in m/s
        "authority"       : 0,                     # Authority of the train in blocks
        "beacon"          : ["", 0, "", False]     # Beacon Inputs from the most recent Beacon
    }

    # Dictionary for inputs from the Train Controller JSON File
    trainControllerToTrainModel = {
        "id"                    : 0,         # ID number for the train
        "power"                 : 0.0,       # Power input from the Train Controller
        "leftDoorCommand"       : False,     # Left Door Command from the Train Controller, False if closed, True if open
        "rightDoorCommand"      : False,     # Right Door Command from the Train Controller, False if closed, True if open
        "serviceBrakeCommand"   : False,     # Service Brake Command from the Train Controller, True if engaged, False is disengaged
        "emergencyBrakeCommand" : False,     # Emergency Brake Command from the Train Controller, True if engaged, False is isengaged
        "externalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
        "InternalLightCommand"  : False,     # External Light Command from the Train Controller, True if on, False if off
        "stationAnnouncement"   : "The Yard" # Station Announcement from the Train Controller
    }

    # Dictionary for outputs to the Train Controller
    trainModelToTrainController = {
        "id"                    : 0,                                   # ID number for the train
        "commandedSpeed"        : 0.0,                                 # Commanded Speed in m/s
        "currentSpeed"          : 0.0,                                 # Current Speed in m/s
        "authority"             : 0,                                   # Authority in Blocks
        "inputTime"             : "2023-02-22T11:00:00.0000000-05:00", # RTC Clock in ISO 8601
        "undergroundState"      : False,                               # Underground State
        "speedLimit"            : 0.0,                                 # Speed Limit in m/s
        "temperature"           : 0.0,                                 # Temperature inside the Train in degrees Fahrenheit
        "engineState"           : True,                                # State of the Engine, True if on, False if off
        "stationName"           : "The Yard",                          # Station Name, from the beacon
        "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both, from the beacon
        "nextStationName"       : "",                                  # Name of the next station, from the beacon
        "isBeacon"              : False,                               # Whether or not a beacon is active
        "externalLightsState"   : False,                               # State of the External Lights, True if on, False if off
        "internalLightsState"   : False,                               # State of the Internal Lights, True if on, False if off
        "leftDoorState"         : False,                               # State of the Left Doors, True if open, False if closed
        "rightDoorState"        : False,                               # State of the Right Doors, True if open, False if closed
        "serviceBrakeState"     : False,                               # State of the Service Brake, True if engaged, False if disengaged
        "emergencyBrakeState"   : False,                               # State of the Emergency Brake, True if engaged, Flase if disengaged
        "serviceBrakeStatus"    : True,                                # Status of the Service Brake, True if operational, False if offline
        "engineStatus"          : True,                                # Status of the Engine, True if operational, False if offline
        "communicationsStatus"  : True                                 # Status of the Communications with the Track, True if operational, False if offline
    }

    # Dictionary for inputs from the Track Model
    trackModelToTrainModel = {
        "rtc"                : "2023-02-22T11:00:00.0000000-05:00",    # Real Time Clock in ISO 8601 Format
        "authority"          : 0,                                      # Authority of the train to be passed to the train controller in blocks
        "commandedSpeed"     : 0.0,                                    # Commanded speed of the train in m/s
        "passengersEntering" : 0,                                      # Number of passengers entering the train
        "speedLimit"         : 0.0,                                    # Speed limit of the current block that the train is on in m/s
        "undergroundState"   : False,                                  # State of whether the train is underground or not
        "beacon"             : ["", 0, "", False],                     # Array to store the beacon inputs [stationName, platformSide, nextStationName, isBeacon]
        "switch"             : True,                                   # True if the block the train is currently on is a switch, false otherwise                      
        "switchState"        : 1                                       # 0 if the switch is in a default position, 1 otherwise
    }

    # Dictionary for outputs to the Track Model
    trainModelToTrackModel = {
        "currBlock"     : 0, # Current Block of the train
        "prevBlock"     : 0, # Block the train is exiting
        "passengersOff" : 0  # Passengers getting off of the train
    }

    def __init__(self):
        # Signals from the Main UI
        trainSignals.commButtonPressedSignal.connect(self.communicationsFailure)
        trainSignals.engineButtonPressedSignal.connect(self.engineFailure)
        trainSignals.brakeButtonPressedSignal.connect(self.serviceBrakeFailure)
        trainSignals.eBrakePressedSignal.connect(self.emergencyBrakeDeceleration)
        trainSignals.tempChangedSignal.connect(self.tempChangeHandler)

        self.data["length"] = self.constants["length"] * self.data["numCars"]

    # JSON function to write outputs to a JSON file for the Train Controller
    def writeTrainModelToTrainController(self):

        # Loading the output data dictionary
        self.trainModelToTrainController["id"]                   = self.data["id"]
        self.trainModelToTrainController["commandedSpeed"]       = self.passThroughData["commandedSpeed"]
        self.trainModelToTrainController["currentSpeed"]         = self.data["velocity"]
        self.trainModelToTrainController["authority"]            = self.passThroughData["authority"]
        self.trainModelToTrainController["inputTime"]            = self.data["rtc"]
        self.trainModelToTrainController["undergroundState"]     = self.data["underground"]
        self.trainModelToTrainController["speedLimit"]           = self.passThroughData["speedLimit"]
        self.trainModelToTrainController["temperature"]          = self.data["currTemp"]
        self.trainModelToTrainController["engineState"]          = True if self.data["power"] > 0 else False
        self.trainModelToTrainController["stationName"]          = self.passThroughData["beacon"][0]
        self.trainModelToTrainController["platformSide"]         = self.passThroughData["beacon"][1]
        self.trainModelToTrainController["nextStationName"]      = self.passThroughData["beacon"][2]
        self.trainModelToTrainController["isBeacon"]             = self.passThroughData["beacon"][3]
        self.trainModelToTrainController["externalLightsState"]  = self.data["eLights"]
        self.trainModelToTrainController["internalLightsState"]  = self.data["iLights"]
        self.trainModelToTrainController["leftDoorState"]        = self.data["lDoors"]
        self.trainModelToTrainController["rightDoorState"]       = self.data["rDoors"]
        self.trainModelToTrainController["serviceBrakeState"]    = self.data["sBrakeState"]
        self.trainModelToTrainController["emergencyBrakeState"]  = self.data["eBrakeState"]
        self.trainModelToTrainController["serviceBrakeStatus"]   = self.data["brakeStatus"]
        self.trainModelToTrainController["engineStatus"]         = self.data["engineStatus"]
        self.trainModelToTrainController["communicationsStatus"] = self.data["commStatus"]

        with open(os.path.join(sys.path[0], "TrainModelToTrainControllerSW.json"), "w") as filename:
            (json.dump(self.trainModelToTrainController, filename, indent = 4))

    # JSON function to read inputs from a JSON file from the Train Controller
    def readTrainControllerToTrainModel(self):
        with open(os.path.join(sys.path[0], "TrainControllerToTrainModel.json"), "r") as filename:
            self.trainControllerToTrainModel = json.loads(filename.read())

        # Loading internal inputs data variable
        self.data["id"]                 = self.trainControllerToTrainModel["id"]
        self.data["power"]              = self.trainControllerToTrainModel["power"]
        self.data["lDoors"]             = self.trainControllerToTrainModel["leftDoorCommand"]
        self.data["rDoors"]             = self.trainControllerToTrainModel["rightDoorCommand"]
        self.data["sBrakeState"]        = self.trainControllerToTrainModel["serviceBrakeCommand"]
        self.eBrakes["trainController"] = self.trainControllerToTrainModel["emergencyBrakeCommand"]
        self.data["eLights"]            = self.trainControllerToTrainModel["externalLightCommand"]
        self.data["iLights"]            = self.trainControllerToTrainModel["internalLightCommand"]
        self.data["station"]            = self.trainControllerToTrainModel["stationAnnouncement"]

    # JSON function to write outputs to a JSON file for the Track Model
    def writeTrainModelToTrackModel(self):

        self.trainModelToTrackModel["currBlock"]     = self.trackData["currBlock"]
        self.trainModelToTrackModel["prevBlock"]     = self.trackData["prevBlock"]
        self.trainModelToTrackModel["passengersOff"] = self.data["passengersOff"]

        with open(os.path.join(sys.path[0], "TrainModelToTrackModel.json"), "w") as filename:
            (json.dump(self.trainModelToTrackModel, filename, indent = 4))

    # JSON function to read inputs from a JSON file from the Track Model
    def readTrackModelToTrainModel(self):
        with open(os.path.join(sys.path[0], "TrackModelToTrainModel.json"), "r") as filename:
            self.trackModelToTrainModel = json.loads(filename.read())

        self.data["rtc"]                       = self.trackModelToTrainModel["rtc"]
        self.passThroughData["authority"]      = self.trackModelToTrainModel["authority"]
        self.passThroughData["commandedSpeed"] = self.trackModelToTrainModel["commandedSpeed"]
        self.data["passengersOn"]              = self.trackModelToTrainModel["passengersEntering"]
        self.passThroughData["speedLimit"]     = self.trackModelToTrainModel["speedLimit"]
        self.data["underground"]               = self.trackModelToTrainModel["undergroundState"]
        self.passThroughData["beacon"]         = self.trackModelToTrainModel["beacon"]
        self.data["atStation"]                 = self.trackModelToTrainModel["beacon"][3]
        self.trackData["switch"]               = self.trackModelToTrainModel["switch"]
        self.trackData["switchState"]          = self.trackModelToTrainModel["switchState"]

    # Function to run all internal methods when the method is called by the updater in the UI
    def runFunctions(self):
        self.readTrainControllerToTrainModel()
        self.readTrackModelToTrainModel()
        tempTimeDiff = self.findTimeDifference()
        self.failureStates()
        self.brakeCaclulator()
        self.findCurrentBlockInfo()
        self.findCurrentAcceleration()
        self.findCurrentVelocity(tempTimeDiff)
        self.findCurrentDistance(tempTimeDiff)
        self.findBlockExiting()
        self.airConditioningControl()
        if self.data["atStation"]:
            self.passengersGettingOff()
            self.passengersGettingOn()
        self.findCurrentMass()
        if tempTimeDiff != 0:
            self.moveToPrevious()
        self.writeTrainModelToTrackModel()
        self.writeTrainModelToTrainController()
        
    # Function to move the current velocity and acceleration to previous in order to calculate next time periods values
    def moveToPrevious(self):
        self.data["prevVelocity"] = self.data["velocity"]
        self.data["prevAcceleration"] = self.data["acceleration"]
        self.data["prevRTC"] = self.data["rtc"]

    # Finds the current acceleration of a train
    def findCurrentAcceleration(self) :
        # Limits the power of the engine
        #if self.data["power"] > 120000:
        #    self.data["power"] = 120000

        # Find the force of friction and the force of mass on the train
        #frictionalForce = -(self.data["mass"] * self.constants["gravity"] * self.constants["friction"] * cos(asin(self.trackData["elevation"] / self.trackData["blockLength"])))
        #gravitationalForce = -(self.data["mass"] * self.constants["gravity"] * (self.trackData["elevation"] / self.trackData["blockLength"]))
        #powerForce = 0
        #brakeForce = 0

        # Deal with finding the force from the power input

        # If the train is not moving, but has power input, set the medium acceleration to 0.5 m/s^2 regardless of
        #if (self.data["prevVelocity"] == 0.0) & (self.data["power"] > 0.0):
        #    self.data["acceleration"] = self.constants["mediumAcceleration"]
        #    return
        
        # If the train is moving and has power input
        #elif (self.data["power"] > 0.0):
        #    powerForce = self.data["power"] / self.data["prevVelocity"]
        #    frictionalForce = 0.0

        # Deal with the force from brakes, if any
        #if (self.data["eBrakeState"] | self.data["sBrakeState"]):
        #    brakeForce = self.data["acceleration"] * self.data["mass"]

        # Calculate the sum of the forces and current Acceleration
        #print("powerForce: ", powerForce, " brakeForce: ", brakeForce, " frictionalForce: ", frictionalForce, " gravitationalForce: ", gravitationalForce)
        #forces = powerForce + brakeForce + frictionalForce + gravitationalForce
        #tempAcceleration = forces / self.data["mass"]

        # Limit the acceleration to follow F = ma
        #self.data["acceleration"] = tempAcceleration if tempAcceleration <= (forces / self.data["mass"]) else (forces / self.data["mass"])
        #print(self.data["acceleration"])

        # Limits the power of the engine
        if self.data["power"] > 120000:
            self.data["power"] = 120000

        # If Emergency or service brakes are enabled, do not change acceleration
        if (self.data["eBrakeState"] | self.data["sBrakeState"]):
            return
        
        # If the train is not moving and has no power input
        if ((self.data["prevVelocity"] == 0.0) & (self.data["power"] == 0.0)):
            force = 0.0

        # If the train is not moving but has a power input
        elif (self.data["prevVelocity"] == 0.0):
            force = self.data["mass"] * self.constants["mediumAcceleration"]

        # All other cases
        else:
            force = self.data["power"] / self.data["prevVelocity"]

        # If the train is not on an incline or decline, use this calculation
        if (self.trackData["elevation"] == 0.0):
            tempAcceleration = force / self.data["mass"]

        # If the train is on an incline or decline, use this calculation
        else:
            # Calculating the effect of mass * gravity when on an incline
            tempAcceleration = (force - (self.data["mass"] * self.constants["gravity"] * (self.trackData["elevation"] / self.trackData["blockLength"]))) / self.data["mass"]

        # Limit the acceleration to something that is possible for the train according to F = ma
        self.data["acceleration"] = tempAcceleration if tempAcceleration <= (force / self.data["mass"]) else (force / self.data["mass"])

    # Finds the current velocity of a train given 7 inputs
    def findCurrentVelocity(self, time = 1):
        currVelocity = self.data["prevVelocity"] + ((time / 2) * (self.data["acceleration"] + self.data["prevAcceleration"]))
        currVelocity = currVelocity if currVelocity >= 0 else 0.0
        self.data["velocity"] = currVelocity

    # Get distance since the last state update of the system
    def findCurrentDistance(self, time = 1):
        self.trackData["distance"] = ((time / 2) * (self.data["prevVelocity"] + self.data["velocity"]))

    # Find the difference in time between current iteration and previous iteration of data in seconds from ISO 8601 Format
    def findTimeDifference(self):
        if (self.data["prevRTC"] == "") & (self.data["rtc"] != ""):
            return 1
        currTime = datetime.fromisoformat(self.data["rtc"])
        prevTime = datetime.fromisoformat(self.data["prevRTC"])
        return int((currTime - prevTime).seconds)


    # NEEDS TO BE REMOVED. MUST GET BLOCK LENGTH AND ELEVATION FROM THE TRAIN MODEL
    # Finds the elevation and block length of the block the train is currently on
    def findCurrentBlockInfo(self):
        # Case if the train is in the yard
        if (self.trackData["currBlock"] == 0):
            return
        
        # Case otherwise
        os.chdir("src/TrainModel")
        with open("greenLineBlocks.txt", newline = '') as csvFile:
            csvReader = csv.reader(csvFile, delimiter = ',')
            for row in csvReader:
                if (row[0] == "Number"):
                    continue
                if (int(row[0])) == self.trackData["currBlock"]:
                    self.trackData["blockLength"] = float(row[3])
                    self.trackData["elevation"] = float(row[12])
                    break
        os.chdir("../../")

    # Finds the Block the train is on and the Block the train is exiting
    def findBlockExiting(self):
        # If the train is derailed (Block 333)
        if (self.trackData["currBlock"] == 333):
            return
        # Case if the distance traveled leaves you somewhere in the block you started in
        elif self.trackData["distance"] < self.trackData["remDistance"]:
            self.trackData["remDistance"] -= self.trackData["distance"]
            self.trackData["prevBlock"] = self.trackData["currBlock"]
        # Case otherwise
        else:
            # Find total overflow distance into the next block
            tempDistance = self.trackData["distance"] - self.trackData["remDistance"]
            self.trackData["currBlock"] = self.findNextBlock()
            self.findCurrentBlockInfo()
            self.trackData["remDistance"] = self.trackData["blockLength"] - tempDistance
            
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
                elif (self.trackData["currBlock"] == 77) | (self.trackData["currBlock"] == 100) | (self.trackData["currBlock"] == 150) | (self.trackData["currBlock"] == 1):
                    print("Derailment")
                    return 333
                
            # If the train is on a switch block and the switch state is 1
            elif (self.trackData["switch"] == True) & (self.trackData["switchState"] == 1):

                # Cases for derailment
                if (self.trackData["currBlock"] == 76) | (self.trackData["currBlock"] == 85) | (self.trackData["currBlock"] == 13) | (self.trackData["currBlock"] == 29) | (self.trackData["currBlock"] == 62):
                    print("Derailment")
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
                print("regular block")
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
                            print("Derailment")
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
                    print("Derailment")
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
                    print("Derailment")
                    return 333
                        # Case where the train needs to just increase block by 1
            else:
                print("regular block")
                if self.trackData["trackSection"][0] < self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] + 1)
                elif self.trackData["trackSection"][0] > self.trackData["trackSection"][1]:
                    self.trackData["prevBlock"] = self.trackData["currBlock"]
                    return (self.trackData["currBlock"] - 1)
        else:
            print("IDK How I even got here")


    # Air Conditioning System that changes based on user input
    def airConditioningControl(self):
        if self.data["currTemp"] < self.data["goalTemp"]:
            self.data["currTemp"] += 0.5
        elif self.data["currTemp"] == self.data["goalTemp"]:
            self.data["currTemp"] += 0
        else:
            self.data["currTemp"] -= 0.5

    # Find the current mass of the entire train including passengers 
    def findCurrentMass(self):
        self.data["mass"] = (self.constants["massOfTrain"] * self.data["numCars"]) + (self.constants["massOfHuman"] * (self.data["passengers"] + self.data["crew"]))

    # Handle Emergency Brake being pulled by the Passenger
    def emergencyBrakeDeceleration(self):
        if (self.eBrakes["user"] == False):
            self.eBrakes["user"] = True
        else:
            self.eBrakes["user"] = False

    # Function to be called when updating the values to set the emergency brake state
    def brakeCaclulator(self):
        self.data["eBrakeState"] = self.eBrakes["user"] | self.eBrakes["trainController"]
        if (self.data["eBrakeState"] == True):
            self.data["acceleration"] = self.constants["emergencyBrake"]
        elif (self.data["sBrakeState"] == True):
            self.data["acceleration"] = self.constants["serviceBrake"]

    # Handle change in input from the user about temperature
    def tempChangeHandler(self, temp):
        self.data["goalTemp"] = temp

    # Determines how many passengers get off at each station
    def passengersGettingOff(self):
        if self.data["atStation"]:
            self.data["passengersOff"] = randint(0, self.data["passengers"])

            self.data["passengers"] -= self.data["passengersOff"]

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
            self.passThroughData["speedLimit"] = 0.0
            self.passThroughData["authority"] = 0
            self.passThroughData["beacon"] = ["", 0, "", False]
        if self.data["engineStatus"] == False:
            self.data["power"] = 0.0
        if self.data["brakeStatus"] == False:
            self.data["sBrakeState"] = False

    # Handle loss of communications
    def communicationsFailure(self):
        if self.data["commStatus"] == False:
            self.data["commStatus"] = True
        else:
            self.data["commStatus"] = False

    # Handle engine failure
    def engineFailure(self):
        if self.data["engineStatus"] == False:
            self.data["engineStatus"] = True
        else:
            self.data["engineStatus"] = False
        self.data["power"] = 0.0

    # Handle service brake failure
    def serviceBrakeFailure(self):
        if self.data["brakeStatus"] == False:
            self.data["brakeStatus"] = True
        else:
            self.data["brakeStatus"] = False
        self.data["sBrakeState"] = False