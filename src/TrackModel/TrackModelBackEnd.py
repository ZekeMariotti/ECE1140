# Train Model Back End

from random import randint
from TrackModelSignals import *
from PyQt6.QtCore import *


class backEndCalculations():

    # Private data variable to store all the data needed for the back end
    data = {
        "blockNo" : 0,                       # Selected Block Number
        "direction" : [0, 0, 0, 0, 0, 0, 0,  # Direction of each track block
         0, 0, 0, 0, 0, 0, 0, 0], 
        "switchPos" : 0,                     # Position of switches
        "sigState" : [0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0],            # States of signals on each block
        "gatePos" : 0,                       # Position of crossing gates
        "temp" : 70.0,                       # Outdoor temperature
        "numPassengers" : [0, 0, 0, 0, 0],   # number of passengers on each train
        "authority" : [0, 0, 0, 0, 0],       # authority of each train
        "commandedSpeed" : [0, 0, 0, 0, 0],  # commanded speed of each train
        "trackHeater" : 0,                   # State of track heater (on/off)
        "blockTrainNo" : [0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0],            # Train number on each block
        "stationOccupancy" : [0, 0],         # Number of people at each station
        "rtc"              : "12:00:00 pm",  # Real Time Clock
    }

    # Dictionary of constants to be used througout the file
    csvConstants = {
        "elevation" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "grade" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "length" : [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        "speedLimit" : [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        "stationSide" : [1, 1]
    }

    def __init__(self):
        trackSignals.powerPressedSignal.connect(self.powerFailure)
        trackSignals.trackCircuitPressedSignal.connect(self.trackCircuitFailure)
        trackSignals.brokenRailPressedSignal.connect(self.brokenRailFailure)

    ##################
    # FAILURE STATES #
    ##################

    # Handle power failure
    def powerFailure(self):
        if self.data["powerStatus"] == False:
            self.data["powerStatus"] = True
        else:
            self.data["powerStatus"] = False

    # Handle track circuit failure
    def trackCircuitFailure(self, index):
        if self.data["trackCircuitStatus"] == False:
            self.data["trackCircuitStatus"] = True
        else:
            self.data["trackCircuitStatus"] = False

    # Handle broken rail failure
    def brokenRailFailure(self, index):
        if self.data["brakeStatus"] == False:
            self.data["brakeStatus"] = True
        else:
            self.data["brakeStatus"] = False

    # Determines how many passengers get off at each station
    def passengersGettingOnB(self, index):
        if self.data["blockTrainNo"][9] > 0:
            self.data["blockTrainNo"][9] = index
            passOff = randint(0, self.data["stationOccupancy"][0])
            self.data["numPassengers"][index] += passOff
            self.data["stationOccupancy"][0] -= passOff

    def passengersGettingOnC(self, index):
        if self.data["blockTrainNo"][14] > 0:
            self.data["blockTrainNo"][14] = index
            passOff = randint(0, self.data["stationOccupancy"][1])
            self.data["numPassengers"][index] += passOff
            self.data["stationOccupancy"][1] -= passOff
