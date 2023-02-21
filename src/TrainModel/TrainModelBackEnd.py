# Train Model Back End

from math import sin, asin
from random import randint
from TrainModelSignals import *
from PyQt6.QtCore import *


class backEndCalculations():

    # Private data variable to store all the data needed for the back end
    data = {
        "rtc"              : "12:00:00 pm",  # Real Time Clock
        "simSpeed"         : 1,              # Simulation Speed of the system
        "passengersOn"     : 0,              # Number of passengers on the train
        "passengersOff"    : 0,              # Number of passengers getting off the train; only used in 1 function
        "crew"             : 2,              # Number of crew members on the train (Default of driver and conductor)
        "underground"      : True,           # State of whether the train is underground or not
        "length"           : 0.0,            # Length of the Train
        "mass"             : 37103.86,            # Mass of the Train, changes based on number of passengers
        "velocity"         : 0.0,            # Current Velocity of the Train
        "acceleration"     : 0.0,            # Current Acceleration of the Train
        "prevVelocity"     : 0.0,            # Previous Velocity of the Train
        "prevAcceleration" : 0.0,            # Previous Acceleration of the Train
        "power"            : 0.0,            # Power input from the Train Controller
        "station"          : "",             # Name of the next Station 
        "atStation"        : False,          # State of whether the train is at a station or not
        "commStatus"       : True,           # True if all communications are good, false is communications are disabled
        "engineStatus"     : True,           # True if engine is operational, false if it is disabled
        "brakeStatus"      : True,           # True is the service brake is operational, false if it is disabled
        "eBrakeState"      : False,          # State of the emergency brake, True if engaged, False if disengaged
        "sBrakeState"      : False,          # State of the service brake, True if engaged, False if disengaged
        "lDoors"           : False,          # State of the left doors, True if doors are open, False if they are closed
        "rDoors"           : False,          # State of the right doors, True if doors are open, False if they are closed
        "iLights"          : True,           # State of the internal lights, True if they are on, False if they are off
        "eLights"          : True,           # State of the external lights, True if they are on, False if they are off
        "currTemp"         : 68.0,           # Current temperature inside the train
        "goalTemp"         : 68.0,            # Temperature goal given by the user
        "elevation"        : 0,              # Relative elevation increase of the block, provided by the Track Model / CSV File
        "blockLength"      : 0,              # Length of the current block, provided by the Track Model / CSV File
    }

    # Dictionary of constants to be used througout the file
    constants = {
        "serviceBrake"       : -1.2,
        "emergencyBrake"     : -2.73,
        "mediumAcceleration" : 0.5,
        "maxSpeed"           : 70,
        "weightUnloaded"     : 40.9,
        "gravity"            : 9.81
    }


    def __init__(self):
        trainSignals.commButtonPressedSignal.connect(self.communicationsFailure)
        trainSignals.engineButtonPressedSignal.connect(self.engineFailure)
        trainSignals.brakeButtonPressedSignal.connect(self.serviceBrakeFailure)
        trainSignals.eBrakePressedSignal.connect(self.emergencyBrakeDeceleration)
        trainSignals.tempChangedSignal.connect(self.tempChangeHandler)

    # Function to run all internal methods when the method is called by the updater in the UI
    def runFunctions(self):
        self.findCurrentAcceleration()
        self.findCurrentVelocity()
        self.airConditioningControl()

    # Finds the current acceleration of a train
    def findCurrentAcceleration(self) :
        if (self.data["eBrakeState"] == True | self.data["sBrakeState"]):
            return self.data["acceleration"]
        
        if (self.data["prevVelocity"] == 0.0):
            force = self.data["mass"] * self.constants["mediumAcceleration"]
        else:
            force = self.data["power"] / self.data["prevVelocity"]
        # If the train is not on an incline or decline, use this calculation
        if (self.data["elevation"] == 0.0):
            self.data["acceleration"] = force / self.data["mass"]

        # If the train is on an incline or decline, use this calculation
        else:
            # Calculating the effect of weight on the train while it is on an incline
            self.data["acceleration"] = (force - (self.data["mass"] * self.constants["gravity"] * sin(asin(self.data["elevation"] / self.data["blockLength"])))) / self.data["mass"]

            # Calculate the force due to mg differently ?
            #currAcceleration = (force - (mass * 9.81 * sin(atan(elevation / blockLength(or elevation / grade))))


    # Finds the current velocity of a train given 7 inputs
    def findCurrentVelocity(self, time = 1):
        currVelocity = self.data["prevVelocity"] + ((time / 2) * (self.data["acceleration"] + self.data["prevAcceleration"]))
        self.data["velocity"] = currVelocity if currVelocity >= 0 else 0.0

    # Air Conditioning System that changes based on user input
    def airConditioningControl(self):
        if self.data["currTemp"] < self.data["goalTemp"]:
            self.data["currTemp"] += 0.5
        elif self.data["currTemp"] == self.data["goalTemp"]:
            self.data["currTemp"] += 0
        else:
            self.data["currTemp"] -= 0.5

    # Get distance since the last state update of the system
    def getDistance(self):
        print("Hello There")

    # Handle Emergency Brake being pulled
    def emergencyBrakeDeceleration(self):
        if (self.data["eBrakeState"] == False):
            self.data["eBrakeState"] = 1
            self.data["acceleration"] = self.constants["emergencyBrake"]
        else:
            self.data["eBrakeState"] = 0

    # Handle Service Brake being pulled
    def serviceBrakeDeceleration(self):
        if (self.data["sBrakeState"] == False) & self.data["brakeStatus"]:
            self.data["sBrakeState"] = 1
            self.data["acceleration"] = self.constants["serviceBrake"]
        elif self.data["sBrakeState"] & self.data["brakeStatus"]:
            self.data["sBrakeState"] = 0

    ##################
    # FAILURE STATES #
    ##################

    # Handle loss of communications
    def communicationsFailure(self):
        if self.data["commStatus"] == False:
            print("Communications Failure")
            self.data["commStatus"] = 1

    # Handle engine failure
    def engineFailure(self):
        print("Engine Failure")

    # Handle service brake failure
    def serviceBrakeFailure(self):
        print("Service Brake Failure")

    # Handle change in input from the user about temperature
    def tempChangeHandler(self, temp):
        self.data["goalTemp"] = temp

    # Determines how many passengers get off at each station
    def passengersGettingOff(self):
        if self.data["atStation"]:
            self.data["passengersOff"] = randint(0, self.data["passengersOn"])
            self.data["passengersOn"] -= self.data["passengersOff"]
            self.data["passengersOff"] = 0

    

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
