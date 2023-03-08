# Train Model Back End

from random import randint
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
        "rtc"              : "12:00:00 am",  # Real Time Clock in ISO 8601 Format
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
        "elevation"        : 0,              # Relative elevation increase of the block, provided by the Track Model / CSV File in meters
        "blockLength"      : 0,              # Length of the current block, provided by the Track Model / CSV File in meters
        "numCars"          : 1,              # Length of the train based on number of cars attached to the train
        "currBlock"        : 0,              # Current block that the train is on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
        "prevBlock"        : 0,              # Previous block that the train was on, ONLY USED BY TRAIN MODEL AND TRACK MODEL
        "distance"         : 0.0             # Distance the train has traveled since the last time period in meters
    }

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
        "beacon"          : [False, "The Yard", 0] # Beacon Inputs from the most recent Beacon
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
        "stationState"          : False,                               # Station State, True if at a station, False otherwise
        "stationName"           : "The Yard",                          # Station Name
        "platformSide"          : 0,                                   # Platform Side, 0 if left, 1 if right, 2 if both
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
        "beacon"             : [False, "The Yard", 0]                  # Array to store the beacon inputs [Station State, Station Name, Platform Side]
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
        self.trainModelToTrainController["engineState"]          = True
        self.trainModelToTrainController["stationState"]         = self.passThroughData["beacon"][0]
        self.trainModelToTrainController["stationName"]          = self.passThroughData["beacon"][1]
        self.trainModelToTrainController["platformSide"]         = self.passThroughData["beacon"][2]
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
        with open(os.path.join(sys.path[0], "TrainControllerSWToTrainModel.json"), "r") as filename:
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

        self.trainModelToTrackModel["currBlock"]     = 0
        self.trainModelToTrackModel["prevBlock"]     = 0
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
        self.data["atStation"]                 = self.trackModelToTrainModel["beacon"][0]

    # Function to run all internal methods when the method is called by the updater in the UI
    def runFunctions(self):
        self.readTrainControllerToTrainModel()
        self.readTrackModelToTrainModel()
        self.failureStates()
        self.brakeCaclulator()
        self.findCurrentBlockInfo()
        self.findCurrentAcceleration()
        self.findCurrentVelocity()
        self.findCurrentDistance()
        self.airConditioningControl()
        if self.data["atStation"]:
            self.passengersGettingOff()
            self.passengersGettingOn()
        self.findCurrentMass()
        self.moveToPrevious()
        self.writeTrainModelToTrackModel()
        self.writeTrainModelToTrainController()
        
    # Function to move the current velocity and acceleration to previous in order to calculate next time periods values
    def moveToPrevious(self):
        self.data["prevVelocity"] = self.data["velocity"]
        self.data["prevAcceleration"] = self.data["acceleration"]

    # Finds the current acceleration of a train
    def findCurrentAcceleration(self) :
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
        if (self.data["elevation"] == 0.0):
            self.data["acceleration"] = force / self.data["mass"]

        # If the train is on an incline or decline, use this calculation
        else:
            # Calculating the effect of mass * gravity wen on an incline
            self.data["acceleration"] = (force - (self.data["mass"] * self.constants["gravity"] * (self.data["elevation"] / self.data["blockLength"]))) / self.data["mass"]

    # Finds the current velocity of a train given 7 inputs
    def findCurrentVelocity(self, time = 1):
        currVelocity = self.data["prevVelocity"] + ((time / 2) * (self.data["acceleration"] + self.data["prevAcceleration"]))
        self.data["velocity"] = currVelocity if currVelocity >= 0 else 0.0

    # Get distance since the last state update of the system
    def findCurrentDistance(self, time = 1):
        self.data["distance"] = ((time / 2) * (self.data["prevVelocity"] + self.data["velocity"]))

    # Finds the elevation and block length of the block the train is currently on
    def findCurrentBlockInfo(self):
        os.chdir("src/TrainModel")
        with open("greenLineBlocks.txt", newline = '') as csvFile:
            csvReader = csv.reader(csvFile, delimiter = ',')
            for row in csvReader:
                if (row[0]) == self.data["currBlock"]:
                    self.data["blockLength"] = row[3]
                    self.data["elevation"] = row[12]
        os.chdir("../../")

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
            self.passThroughData["beacon"] = [False, "", 0]
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
    
if __name__ == "__main__":
    class1 = TrainModel()
    class1.runFunctions()

# Main function to run if this file is the file being ran as main
#def main():
#    test = backEndCalculations()
#    a = test.findCurrentAcceleration()
#    print("A:", a)
#    v = test.findCurrentVelocity()
#    print("V:", v)
    #test.airConditioningControl(100)
    #v = test.findCurrentVelocity(12000, 0, 40823, 3, 1, 100)
    #print("V2: ", v)
    #v = test.findCurrentVelocity(12000, 0, 40823, 3, -3, 100)
    #print("V3: ", v)

#if __name__ == "__main__":
    #main()
