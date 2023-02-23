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
        "blockTrainNo" : [0, 0, 0, 0, 0, 0,  # Train number on each block
        0, 0, 0, 0, 0, 0, 0, 0, 0],          
        "underground" : [0, 0, 0, 0, 0, 0,   # Is train block underground
        0, 0, 0, 0, 0, 0, 0, 0, 0],            
        "stationOccupancy" : [0, 0],         # Number of people at each station
        "rtc"              : "12:00:00 pm",  # Real Time Clock,
        "powerStatus": 0,                    # Power failure state
        "circuitStatus" : [0, 0, 0, 0, 0, 0, # Track circuit failure states
        0, 0, 0, 0, 0, 0, 0, 0, 0],
        "railStatus" : [0, 0, 0, 0, 0, 0,    # Broken rail failure states
        0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    # Dictionary of constants to be used througout the file
    csvConstants = {
        "elevation" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "grade" : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "length" : [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        "speedLimit" : [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
        "stationSide" : [1, 1]
    }

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