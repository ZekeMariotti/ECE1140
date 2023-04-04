# Train Model Back End

import sys
import os
sys.path.append(__file__.replace("\TrackModel\TrackModelBackEnd.py", ""))

from random import randint
from TrackModel.TrackModelSignals import *
from Integration.TMTkMSignals import *
from PyQt6.QtCore import *
from dynamicArray import *


class backEndCalculations():

    runOnce = False
    # Private data variable to store all the data needed for the back end
    data = {
        "line" : 0,                          # Selected line
        "blockNo" : 0,                       # Selected Block Number
        "switchPos" : DynamicArray(),        # Position of switches
        "sigState" : DynamicArray(),         # States of signals on each block next to a switch
        "gatePos" : DynamicArray(),          # Position of crossing gates
        "temp" : 70.0,                       # Outdoor temperature
        "numPassengers" : [0, 222, 0, 0, 0, 0,
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
        "trainBlock" : [0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],
        "trainLine" : [0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],
        "trackHeater" : 0,                   # State of track heater (on/off)
        "blockTrainNoRed" : DynamicArray(),  # Train number on each block   
        "blockTrainNoGreen" : DynamicArray(),             
        "stationOccupancy" : DynamicArray(), # Number of people at each station
        "rtc"              : "12:00:00 pm",  # Real Time Clock,
        "powerStatus": 0,                    # Power failure state
        "circuitStatusRed" : DynamicArray(),     # Track circuit failure states
        "circuitStatusGreen" : DynamicArray(),
        "railStatusRed" : DynamicArray(),        # Broken rail failure states
        "railStatusGreen" : DynamicArray(),
        "moves" : [[0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None],
                   [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None],
                   [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None],
                   [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None],
                   [0, 9, None], [0, 9, None], [0, 9, None], [0, 9, None]]
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
        "beaconRed" : DynamicArray(),
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
        "beaconGreen" : DynamicArray(),
        "stationName" : DynamicArray(),
        "stationSide" : DynamicArray(),
        "stationLine" : DynamicArray(),
        "switchBlockA" : DynamicArray(),
        "switchBlockB" : DynamicArray(),
        "switchBlockC" : DynamicArray()
    }

    def __init__(self):
        trackSignals.getSwitchPositionInput.connect(self.getSwitchPositionInput)
        trackSignals.getGatePositionInput.connect(self.getGatePositionInput)
        trackSignals.getSignalStateInput.connect(self.getSignalStateInput)
        trackSignals.getTempInput.connect(self.getTempInput)
        trackSignals.getTrackHeaterInput.connect(self.getTrackHeaterInput)
        trackSignals.getStationOccInput.connect(self.getStationOccInput)
        trackSignals.getTrainBlockInputSignal.connect(self.getTrainBlockInputFunction)
        trackSignals.getTrainLnInput.connect(self.getTrainLnInput)
        trackSignals.getOffInput.connect(self.getOffInput)
        trackSignals.getOnInput.connect(self.getOnInput)
        trackSignals.getAuthInput.connect(self.getAuthInput)
        trackSignals.getCSpeedInput.connect(self.getCSpeedInput)
        trackSignals.getRealTimeClockInput.connect(self.getRealTimeClockInput)

        TMTkMSignals.passengersExitingSignal.connect(self.passengersExiting)
        TMTkMSignals.currBlockSignal.connect(self.currBlockHandler)

    # Handler for when a new train is made
    def newTrainMade(self, id, line):
        if (line == "Green"):
            self.data["trainLine"][id - 1] = 1
            self.data["moves"][id - 1] = [0, 63, None]
        elif(line == "Red"):
            self.data["trainLine"][id - 1] = 0
            self.data["moves"][id - 1] = [0, 9, None]
        else:
            print("Something")

    # Handler PassengersExiting signal from the train model
    def passengersExiting(self, id, num):
        if (num > 0) & ~self.runOnce:
            print(f'TrainID: {id}, Passengers Off: {num}')
            self.passengersGettingOff(id, num)
            self.passengersGettingOn(id)
            print("Track Model - Return From Track Model Function")
            if (self.csvConstants["stationGreen"].__getitem__(int(self.data["trainBlock"][id - 1]) - 1) == 0):
                self.runOnce = False

    # Hander for the current block from the Train Model
    def currBlockHandler(self, id, currBlock, prevBlock, transition):
        if (transition):
            TMTkMSignals.blockLengthSignal.emit(id, float(self.csvConstants["lengthGreen"].__getitem__(currBlock - 1)))
            TMTkMSignals.elevationSignal.emit(id, float(self.csvConstants["elevationGreen"].__getitem__(currBlock - 1)))
            TMTkMSignals.undergroundStateSignal.emit(id, bool(int(self.csvConstants["undergroundGreen"].__getitem__(currBlock - 1))))
            #TMTkMSignals.beaconSignal.emit(id, self.csvConstants["beaconGreen"][0], int(self.csvConstants["beaconGreen"][1]), self.csvConstants["beaconGreen"][2], bool(self.csvConstants["beaconGreen"][3]), -1, 0)
            if (prevBlock == 0):
                TMTkMSignals.switchSignal.emit(id, 0)
                TMTkMSignals.switchStateSignal.emit(id, 1)
            elif (int(self.csvConstants["switchGreen"].__getitem__(currBlock - 1)) > 0) & (int(self.csvConstants["switchGreen"].__getitem__(prevBlock - 1)) > 0):
                TMTkMSignals.switchSignal.emit(id, 0)
                TMTkMSignals.switchStateSignal.emit(id, bool(self.data["switchPos"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(currBlock - 1)) - 1)))
            elif (int(self.csvConstants["switchGreen"].__getitem__(currBlock - 1)) > 0):
                TMTkMSignals.switchSignal.emit(id, 1)
                TMTkMSignals.switchStateSignal.emit(id, bool(self.data["switchPos"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(currBlock - 1)) - 1)))
            else:
                TMTkMSignals.switchSignal.emit(id, 0)
                TMTkMSignals.switchStateSignal.emit(id, 0)
            if (currBlock == self.data["moves"][id - 1][0]):
                index = 0
            elif (currBlock == self.data["moves"][id - 1][1]):
                index = 1
            elif (currBlock == self.data["moves"][id - 1][2]):
                index = 2
            if (index != 0):
                self.getTrainBlockInputFunction(index, id - 1)
        else:
            TMTkMSignals.beaconSignal.emit(id, "", 0, "", 0, -1, 0)

    # Gets the Switch Position from the UI
    def getSwitchPositionInput(self, index, line, blockNo):
        if line == 0:
            self.data["switchPos"].removeAt(int(self.csvConstants["switchRed"].__getitem__(blockNo)) - 1)
            self.data["switchPos"].insertAt(index, int(self.csvConstants["switchRed"].__getitem__(blockNo)) - 1)
        elif line == 1:
            self.data["switchPos"].removeAt(int(self.csvConstants["switchGreen"].__getitem__(blockNo)) - 1)
            self.data["switchPos"].insertAt(index, int(self.csvConstants["switchGreen"].__getitem__(blockNo)) - 1)

        for i in range(35):
            self.updateVector(i) # Can be put in if statement to increace efficiency

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Gate Position state from the UI
    def getGatePositionInput(self, index, line, blockNo):
        if line == 0:
            self.data["gatePos"].removeAt(int(self.csvConstants["crossingRed"].__getitem__(blockNo)) - 1)
            self.data["gatePos"].insertAt(index, int(self.csvConstants["crossingRed"].__getitem__(blockNo)) - 1)
        elif line == 1:
            self.data["gatePos"].removeAt(int(self.csvConstants["crossingGreen"].__getitem__(blockNo)) - 1)
            self.data["gatePos"].insertAt(index, int(self.csvConstants["crossingGreen"].__getitem__(blockNo)) - 1)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Signal State from the UI
    def getSignalStateInput(self, index, line, blockNo):
        if line == 0 and blockNo != -1:
            self.data["sigState"].removeAt(int(self.csvConstants["signalRed"].__getitem__(blockNo)) - 1)
            self.data["sigState"].insertAt(index, int(self.csvConstants["signalRed"].__getitem__(blockNo)) - 1)
        elif line == 1 and blockNo != -1:
            self.data["sigState"].removeAt(int(self.csvConstants["signalGreen"].__getitem__(blockNo)) - 1)
            self.data["sigState"].insertAt(index, int(self.csvConstants["signalGreen"].__getitem__(blockNo)) - 1)

        # Refresh Main UI
        trackSignals.updateSignal.emit()      

    # Gets the Temperature from the UI
    def getTempInput(self, temperature):
        self.data["temp"] = temperature

        # Configure Track Heaters
        if self.data["temp"] > 32:
            self.data["trackHeater"] = 0
        elif self.data["temp"] < 32:
            self.data["trackHeater"] = 1

        # Refresh Main UI
        trackSignals.updateSignal.emit()
    
    # Gets the Track Heater state from the UI
    def getTrackHeaterInput(self, index):
        self.data["trackHeater"] = index

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Station Occupancy from the UI
    def getStationOccInput(self, occ):
        self.data["stationOccupancy"].removeAt(self.data["stationName"])
        self.data["stationOccupancy"].insertAt(occ, self.data["stationName"])
        if self.data["stationOccupancy"].__getitem__(self.data["stationName"]) == 1:
            self.occOutput.setText("1 person")
        else:
            self.occOutput.setText(str(self.data["stationOccupancy"].__getitem__(self.data["stationName"])) + " people")

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Train Block from the UI
    def getTrainBlockInputFunction(self, index, trainNo):
        
        # Update block train number
        # Sets last block train was at to 0
        if self.data["trainLine"][trainNo] == 0 and self.data["moves"][trainNo][0] != 0:
            self.data["blockTrainNoRed"].removeAt(self.data["moves"][trainNo][0] - 1)
            self.data["blockTrainNoRed"].insertAt(0, self.data["moves"][trainNo][0] - 1)
        elif self.data["trainLine"][trainNo] == 1 and self.data["moves"][trainNo][0] != 0:
            self.data["blockTrainNoGreen"].removeAt(self.data["moves"][trainNo][0] - 1)
            self.data["blockTrainNoGreen"].insertAt(0, self.data["moves"][trainNo][0] - 1)

        # Sets train number to new block
        if self.data["trainLine"][trainNo] == 0:
            self.data["blockTrainNoRed"].removeAt(self.data["moves"][trainNo][index] - 1)
            self.data["blockTrainNoRed"].insertAt(trainNo + 1, self.data["moves"][trainNo][index] - 1)
        elif self.data["trainLine"][trainNo] == 1:
            self.data["blockTrainNoGreen"].removeAt(self.data["moves"][trainNo][index] - 1)
            self.data["blockTrainNoGreen"].insertAt(trainNo + 1, self.data["moves"][trainNo][index] - 1)

        # Update Authority
        self.data["authority"][trainNo] -= 1

        # Send Beacon
        if self.data["trainLine"][trainNo] == 0:
            if self.csvConstants["stationRed"].__getitem__(self.data["moves"][trainNo][index] - 1) > 0:
                beaconArr = self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][0] - 1)
                TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), -1, 0)
            elif self.csvConstants["stationRed"].__getitem__(self.data["moves"][trainNo][0] - 1) > 0:
                beaconArr = self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][index] - 1)
                TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), -1, 0)
            else:
                TMTkMSignals.beaconSignal.emit(trainNo + 1, "", 0, "", 0, -1, 0)
        elif self.data["trainLine"][trainNo] == 1:
            if (int(self.data["moves"][trainNo][index] - 1) > 0) & (int(self.csvConstants["stationGreen"].__getitem__(self.data["moves"][trainNo][index] - 1)) > 0):
                beaconArr = self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)
                TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), -1, 0)
            elif (int(self.data["moves"][trainNo][0] - 1) > 0):
                if (int(self.csvConstants["stationGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) > 0):
                    beaconArr = self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][index] - 1)
                    TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), -1, 0)
            else:
                TMTkMSignals.beaconSignal.emit(trainNo + 1, "", 0, "", 0, -1, 0)

        # Update Block vector
        self.data["moves"][trainNo][0] = self.data["moves"][trainNo][index]
        self.updateVector(trainNo)
        
        # Update train block output
        self.data["trainBlock"][trainNo] = self.data["moves"][trainNo][0]

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets new data if train line changes
    def getTrainLnInput(self, index, trainNo):
        self.data["trainLine"][trainNo] = index
        self.updateVector(trainNo)

    # Gets the number of passengers off from the UI
    def getOffInput(self, trainNo, sName, passengers):
        if self.csvConstants["stationLine"].__getitem__(sName) == 0:
            for i in range(self.data["blockTrainNoRed"].__len__()):
                if int(self.csvConstants["stationRed"].__getitem__(i)) > 0 and self.data["trainBlock"][trainNo] == i + 1 and self.data["numPassengers"][trainNo] - passengers >= 0:
                    self.data["numPassengers"][trainNo] -= passengers
        elif self.csvConstants["stationLine"].__getitem__(sName) == 1:
            for i in range(self.data["blockTrainNoGreen"].__len__()):
                if int(self.csvConstants["stationGreen"].__getitem__(i)) > 0 and self.data["trainBlock"][trainNo] == i + 1 and self.data["numPassengers"][trainNo] - passengers >= 0:
                    self.data["numPassengers"][trainNo] -= passengers

        # Refresh Main UI
        self.runOnce = True
        trackSignals.updateSignal.emit()

    # Gets the number of passengers on from the UI
    def getOnInput(self, sName, passengers):
        if self.csvConstants["stationLine"].__getitem__(sName) == 0:
            for i in range(self.data["blockTrainNoRed"].__len__()):
                if int(self.data["blockTrainNoRed"].__getitem__(i)) > 0 and int(self.csvConstants["stationRed"].__getitem__(i)) > 0 and int(self.csvConstants["stationRed"].__getitem__(i)) - 1 == int(self.data["stationName"]) and int(self.data["stationOccupancy"].__getitem__(self.data["stationName"])) - passengers >= 0:
                    self.data["numPassengers"][self.data["blockTrainNoRed"].__getitem__(i) - 1] += passengers
                    currOcc = self.data["stationOccupancy"].__getitem__(sName)
                    self.data["stationOccupancy"].removeAt(sName)
                    self.data["stationOccupancy"].insertAt(currOcc - passengers, sName)
        elif self.csvConstants["stationLine"].__getitem__(sName) == 1:
            for i in range(self.data["blockTrainNoGreen"].__len__()):
                if int(self.data["blockTrainNoGreen"].__getitem__(i)) > 0 and int(self.csvConstants["stationGreen"].__getitem__(i)) > 0 and int(self.csvConstants["stationGreen"].__getitem__(i)) - 1 == sName and int(self.data["stationOccupancy"].__getitem__(sName)) - passengers >= 0:
                    self.data["numPassengers"][self.data["blockTrainNoGreen"].__getitem__(i) - 1] += passengers
                    currOcc = self.data["stationOccupancy"].__getitem__(sName)
                    self.data["stationOccupancy"].removeAt(sName)
                    self.data["stationOccupancy"].insertAt(currOcc - passengers, sName)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the authority input from the UI
    def getAuthInput(self, auth, trainNo):
        self.data["authority"][trainNo - 1] = auth
        TMTkMSignals.authoritySignal.emit(trainNo, auth)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the commanded speed input from the UI
    def getCSpeedInput(self, CSpeed, trainNo):
        self.data["commandedSpeed"][trainNo - 1] = CSpeed
        TMTkMSignals.commandedSpeedSignal.emit(trainNo, CSpeed)

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    # Gets the Real Time Clock state from the UI
    def getRealTimeClockInput(self, rtc):
        self.data["rtc"] = rtc

        # Refresh Main UI
        trackSignals.updateSignal.emit()

    def updateVector(self, trainNo):
        if self.data["moves"][trainNo][0] == 0 and self.data["trainLine"][trainNo] == 0:
            if int(self.data["switchPos"].__getitem__(1)) == 1:
                self.data["moves"][trainNo][1] = 9
            else:
                self.data["moves"][trainNo][1] = None
            self.data["moves"][trainNo][2] = None
        elif self.data["moves"][trainNo][0] == 0 and self.data["trainLine"][trainNo] == 1:
            if int(self.data["switchPos"].__getitem__(9)) == 1 and int(self.data["switchPos"].__getitem__(10)) == 1:
                self.data["moves"][trainNo][1] = 57
                self.data["moves"][trainNo][2] = 63
            else:
                if int(self.data["switchPos"].__getitem__(9)) == 1:
                    self.data["moves"][trainNo][1] = 57
                    self.data["moves"][trainNo][2] = None
                elif int(self.data["switchPos"].__getitem__(10)) == 1:
                    self.data["moves"][trainNo][1] = 63
                    self.data["moves"][trainNo][2] = None
                else:
                    self.data["moves"][trainNo][1] = None
                    self.data["moves"][trainNo][2] = None
        elif self.data["trainLine"][trainNo] == 0 and int(self.csvConstants["switchRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) > 0:
            sba = int(self.csvConstants["switchBlockA"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sbb = int(self.csvConstants["switchBlockB"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sbc = int(self.csvConstants["switchBlockC"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sPos = int(self.data["switchPos"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            noGo = self.csvConstants["noGoRed"].__getitem__(self.data["moves"][trainNo][0] - 1)
            if sba == self.data["moves"][trainNo][0] and sbc == sba - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = sbb
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] + 1
            elif sba == self.data["moves"][trainNo][0] and sbc == sba + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = sbb
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = sba
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] - 1
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = sba
            elif sbc == self.data["moves"][trainNo][0] and sba == sbc + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = None
            elif sbc == self.data["moves"][trainNo][0] and sba == sbc - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = None
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb + 1 and sPos == 0:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = None
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb - 1 and sPos == 0:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = None
            else:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] - 1
        elif self.data["trainLine"][trainNo] == 1 and int(self.csvConstants["switchGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) > 0:
            sba = int(self.csvConstants["switchBlockA"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sbb = int(self.csvConstants["switchBlockB"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sbc = int(self.csvConstants["switchBlockC"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            sPos = int(self.data["switchPos"].__getitem__(int(self.csvConstants["switchGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) - 1))
            noGo = self.csvConstants["noGoGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)
            if sba == self.data["moves"][trainNo][0] and sbc == sba - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = sbb
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] + 1
            elif sba == self.data["moves"][trainNo][0] and sbc == sba + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = sbb
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = sba
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] - 1
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = sba
            elif sbc == self.data["moves"][trainNo][0] and sba == sbc + 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = None
            elif sbc == self.data["moves"][trainNo][0] and sba == sbc - 1 and sPos == 1:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = None
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb + 1 and sPos == 0:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] - 1
                self.data["moves"][trainNo][2] = None
            elif sbb == self.data["moves"][trainNo][0] and int(noGo) == sbb - 1 and sPos == 0:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = None
            else:
                self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
                self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] - 1
        else:
            self.data["moves"][trainNo][1] = self.data["moves"][trainNo][0] + 1
            self.data["moves"][trainNo][2] = self.data["moves"][trainNo][0] - 1

    # Determines how many passengers get on at each station
    def passengersGettingOn(self, trainNo):
        # Generate number of passengers getting on the train at the station
        if self.data["trainLine"][trainNo - 1] == 0:
            passOn = randint(0, int(self.data["stationOccupancy"].__getitem__(int(self.csvConstants["stationRed"].__getitem__(self.data["trainBlock"][trainNo - 1])) - 1)))
            self.getOnInput(int(self.csvConstants["stationRed"].__getitem__(self.data["trainBlock"][trainNo - 1])) - 1, passOn)
        elif self.data["trainLine"][trainNo - 1] == 1:
            passOn = randint(0, int(self.data["stationOccupancy"].__getitem__(int(self.csvConstants["stationGreen"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1)))
            self.getOnInput(int(self.csvConstants["stationGreen"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1, passOn)
        TMTkMSignals.passengersEnteringSignal.emit(trainNo, passOn)

    # Determines how many passengers get off at each station
    def passengersGettingOff(self, trainNo, passOff):
        # Update number of passengers getting off the train at the station
        if self.data["trainLine"][trainNo - 1] == 0:
            self.getOffInput(trainNo - 1, int(self.csvConstants["stationRed"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1, passOff)
        elif self.data["trainLine"][trainNo - 1] == 1:
            self.getOffInput(trainNo - 1, int(self.csvConstants["stationGreen"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1, passOff)

    # Determines how many passengers get off at each station
    def passengersGettingOnB(self, index):
        passOff = randint(0, self.data["stationOccupancy"].__getitem__(self.data["stationRed"].__getitem__(index) - 1))
        self.data["numPassengers"][index] += passOff
        # curr = self.data["stationOccupancy"].__getitem__(self.data["stationRed"].__getitem__(index) - 1)
        # self.data["stationOccupancy"].removeAt(self.data["stationRed"].__getitem__(index) - 1)
        # -= passOff

import csv

with open(os.path.join(sys.path[0], "TrackModel", "RedLine.csv"), 'r') as redLn:
#with open(os.path.join(sys.path[0].replace("\src", "\src\TrackModel")), 'r') as redLn:
#with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/RedLine.csv", 'r') as redLn:
    redLine = csv.DictReader(redLn)

    for row in redLine:
        backEndCalculations.csvConstants["redBlocks"].append(row["BlockNo"])
        backEndCalculations.csvConstants["lengthRed"].append(row["BlockLength"])
        backEndCalculations.csvConstants["gradeRed"].append(row["Grade"])
        backEndCalculations.csvConstants["speedLimitRed"].append(row["SpeedLimit"])
        backEndCalculations.csvConstants["elevationRed"].append(row["Elevation"])
        backEndCalculations.csvConstants["undergroundRed"].append(row["Underground"])
        backEndCalculations.csvConstants["stationRed"].append(row["StationID"])
        backEndCalculations.csvConstants["switchRed"].append(row["Switch"])
        backEndCalculations.csvConstants["signalRed"].append(row["Signal"])
        backEndCalculations.csvConstants["crossingRed"].append(row["Crossing"])
        backEndCalculations.csvConstants["noGoRed"].append(row["NoGo"])
        backEndCalculations.csvConstants["beaconRed"].append([row["b0"], row["b1"], row["b2"], row["b3"]])
        backEndCalculations.data["blockTrainNoRed"].append(0)
        backEndCalculations.data["circuitStatusRed"].append(0)
        backEndCalculations.data["railStatusRed"].append(0)
        if int(row["Crossing"]) > 1:
            backEndCalculations.data["gatePos"].append(0)
        if int(row["Signal"]) > 1:
            backEndCalculations.data["sigState"].append(0)

with open(os.path.join(sys.path[0], "TrackModel", "GreenLine.csv"), 'r') as greenLn:
#with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/GreenLine.csv", 'r') as greenLn:
    greenLine = csv.DictReader(greenLn)

    for row in greenLine:
        backEndCalculations.csvConstants["greenBlocks"].append(row["BlockNo"])
        backEndCalculations.csvConstants["lengthGreen"].append(row["BlockLength"])
        backEndCalculations.csvConstants["gradeGreen"].append(row["Grade"])
        backEndCalculations.csvConstants["speedLimitGreen"].append(row["SpeedLimit"])
        backEndCalculations.csvConstants["elevationGreen"].append(row["Elevation"])
        backEndCalculations.csvConstants["undergroundGreen"].append(row["Underground"])
        backEndCalculations.csvConstants["stationGreen"].append(row["StationID"])
        backEndCalculations.csvConstants["switchGreen"].append(row["Switch"])
        backEndCalculations.csvConstants["signalGreen"].append(row["Signal"])
        backEndCalculations.csvConstants["crossingGreen"].append(row["Crossing"])
        backEndCalculations.csvConstants["noGoGreen"].append(row["NoGo"])
        backEndCalculations.csvConstants["beaconGreen"].append([row["b0"], row["b1"], row["b2"], row["b3"]])
        backEndCalculations.data["blockTrainNoGreen"].append(0)
        backEndCalculations.data["circuitStatusGreen"].append(0)
        backEndCalculations.data["railStatusGreen"].append(0)
        if int(row["Crossing"]) > 1:
            backEndCalculations.data["gatePos"].append(0)
        if int(row["Signal"]) > 1:
            backEndCalculations.data["sigState"].append(0)

with open(os.path.join(sys.path[0], "TrackModel", "Stations.csv"), 'r') as sta:
#with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/Stations.csv", 'r') as sta:
    stations = csv.DictReader(sta)

    for row in stations:
        backEndCalculations.csvConstants["stationName"].append(row["StationName"])
        backEndCalculations.csvConstants["stationSide"].append(row["StationSide"])
        backEndCalculations.data["stationOccupancy"].append(5)
        if row["Line"] == "RED":
            backEndCalculations.csvConstants["stationLine"].append(0)
        elif row["Line"] == "GREEN":
            backEndCalculations.csvConstants["stationLine"].append(1)

with open(os.path.join(sys.path[0], "TrackModel", "Switches.csv"), 'r') as swi:
#with open("C:/Systems and Project Engineering/ECE1140/src/TrackModel/Switches.csv", 'r') as swi:
    switches = csv.DictReader(swi)

    for row in switches:
        backEndCalculations.csvConstants["switchBlockA"].append(row["BlockA"])
        backEndCalculations.csvConstants["switchBlockB"].append(row["BlockB"])
        backEndCalculations.csvConstants["switchBlockC"].append(row["BlockC"])
        backEndCalculations.data["switchPos"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)