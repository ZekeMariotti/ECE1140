# Train Model Back End

from random import randint
from TrackModelSignals import *
from PyQt6.QtCore import *
from dynamicArray import *


class backEndCalculations():

    # Private data variable to store all the data needed for the back end
    data = {
        "line" : 0,                          # Selected line
        "blockNo" : 0,                       # Selected Block Number
        "switchPos" : DynamicArray(),        # Position of switches
        "sigState" : DynamicArray(),         # States of signals on each block next to a switch
        "gatePos" : DynamicArray(),          # Position of crossing gates
        "temp" : 70.0,                       # Outdoor temperature
        "numPassengers" : [0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],                   # number of passengers on each train
        "authority" : [0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],                   # authority of each train
        "commandedSpeed" : [0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],                   # commanded speed of each train
        "trackHeater" : 0,                   # State of track heater (on/off)
        "blockTrainNoRed" : DynamicArray(),  # Train number on each block   
        "blockTrainNoGreen" : DynamicArray(),             
        "stationOccupancy" : DynamicArray(), # Number of people at each station
        "rtc"              : "12:00:00 pm",  # Real Time Clock,
        "powerStatus": 0,                    # Power failure state
        "circuitStatusRed" : DynamicArray(),     # Track circuit failure states
        "circuitStatusGreen" : DynamicArray(),
        "railStatusRed" : DynamicArray(),        # Broken rail failure states
        "railStatusGreen" : DynamicArray()
    }

    # Dictionary of constants to be used througout the file
    csvConstants = {
        "redBlocks" : DynamicArray(),
        "greenBlocks" : DynamicArray(),
        "elevationRed" : DynamicArray(),
        "gradeRed" : DynamicArray(),
        "lengthRed" : DynamicArray(),
        "speedLimitRed" : DynamicArray(),
        "undergroundRed" : DynamicArray(),
        "stationRed" : DynamicArray(),
        "switchRed" : DynamicArray(),
        "signalRed" : DynamicArray(),
        "crossingRed" : DynamicArray(),
        "noGoRed" : DynamicArray(),
        "elevationGreen" : DynamicArray(),
        "gradeGreen" : DynamicArray(),
        "lengthGreen" : DynamicArray(),
        "speedLimitGreen" : DynamicArray(),
        "undergroundGreen" : DynamicArray(),
        "stationGreen" : DynamicArray(),
        "switchGreen" : DynamicArray(),
        "crossingGreen" : DynamicArray(),
        "signalGreen" : DynamicArray(),
        "noGoGreen" : DynamicArray(),
        "stationName" : DynamicArray(),
        "stationSide" : DynamicArray(),
        "switchLine" : DynamicArray(),
        "switchBlockA" : DynamicArray(),
        "switchBlockB" : DynamicArray(),
        "switchBlockC" : DynamicArray()
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

import csv

with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/RedLine.csv", 'r') as redLn:
    redLine = csv.DictReader(redLn)

    for row in redLine:
        backEndCalculations.csvConstants["redBlocks"].append(row["BlockNo"])
        backEndCalculations.csvConstants["lengthRed"].append(row["BlockLength"])
        backEndCalculations.csvConstants["gradeRed"].append(row["Grade"])
        backEndCalculations.csvConstants["speedLimitRed"].append(row["SpeedLimit"])
        backEndCalculations.csvConstants["elevationRed"].append(row["BlockLength"])
        backEndCalculations.csvConstants["undergroundRed"].append(row["Underground"])
        backEndCalculations.csvConstants["stationRed"].append(row["StationID"])
        backEndCalculations.csvConstants["switchRed"].append(row["Switch"])
        backEndCalculations.csvConstants["signalRed"].append(row["Signal"])
        backEndCalculations.csvConstants["crossingRed"].append(row["Crossing"])
        backEndCalculations.csvConstants["noGoRed"].append(row["NoGo"])
        backEndCalculations.data["blockTrainNoRed"].append(0)
        backEndCalculations.data["circuitStatusRed"].append(0)
        backEndCalculations.data["railStatusRed"].append(0)
        if int(row["Crossing"]) > 1:
            backEndCalculations.data["gatePos"].append(0)
        if int(row["Signal"]) > 1:
            backEndCalculations.data["sigState"].append(0)


with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/GreenLine.csv", 'r') as greenLn:
    greenLine = csv.DictReader(greenLn)

    for row in greenLine:
        backEndCalculations.csvConstants["greenBlocks"].append(row["BlockNo"])
        backEndCalculations.csvConstants["lengthGreen"].append(row["BlockLength"])
        backEndCalculations.csvConstants["gradeGreen"].append(row["Grade"])
        backEndCalculations.csvConstants["speedLimitGreen"].append(row["SpeedLimit"])
        backEndCalculations.csvConstants["elevationGreen"].append(row["BlockLength"])
        backEndCalculations.csvConstants["undergroundGreen"].append(row["Underground"])
        backEndCalculations.csvConstants["stationGreen"].append(row["StationID"])
        backEndCalculations.csvConstants["switchGreen"].append(row["Switch"])
        backEndCalculations.csvConstants["signalGreen"].append(row["Signal"])
        backEndCalculations.csvConstants["crossingGreen"].append(row["Crossing"])
        backEndCalculations.csvConstants["noGoGreen"].append(row["NoGo"])
        backEndCalculations.data["blockTrainNoGreen"].append(0)
        backEndCalculations.data["circuitStatusGreen"].append(0)
        backEndCalculations.data["railStatusGreen"].append(0)
        if int(row["Crossing"]) > 1:
            backEndCalculations.data["gatePos"].append(0)
        if int(row["Signal"]) > 1:
            backEndCalculations.data["sigState"].append(0)

with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/Stations.csv", 'r') as sta:
    stations = csv.DictReader(sta)

    for row in stations:
        backEndCalculations.csvConstants["stationName"].append(row["StationName"])
        backEndCalculations.csvConstants["stationSide"].append(row["StationSide"])
        backEndCalculations.data["stationOccupancy"].append(0)

with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/Switches.csv", 'r') as swi:
    switches = csv.DictReader(swi)

    for row in switches:
        if row["Line"] == "RED":
            backEndCalculations.csvConstants["switchLine"].append(0)
        elif row["Line"] == "GREEN":
            backEndCalculations.csvConstants["switchLine"].append(1)
        backEndCalculations.csvConstants["switchBlockA"].append(row["BlockA"])
        backEndCalculations.csvConstants["switchBlockB"].append(row["BlockB"])
        backEndCalculations.csvConstants["switchBlockC"].append(row["BlockC"])
        backEndCalculations.data["switchPos"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)