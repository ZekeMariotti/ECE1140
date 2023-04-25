# Train Model Back End

import sys
import os
import requests, json
sys.path.append(__file__.replace("\TrackModel\TrackModelBackEnd.py", ""))

from random import randint
from datetime import *
from TrackModel.TrackModelSignals import *
from Integration.TMTkMSignals import *
from Integration.TkMWCSignals import *
from Integration.TimeSignals import *
from PyQt6.QtCore import *
from dynamicArray import *


class backEndCalculations():

    runOnce = False
    # Get temperature in Pittsburgh using HTTP request
    api_key = "953d0d2dbcbd81b1e91ccb899240145d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Pittsburgh"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    try :
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = round((y["temp"] - 273.15) * 1.8 + 32, 2)
            if current_temperature <= 32:
                tHeater = 1
            else:
                tHeater = 0
    except:
        tHeater = 0
        current_temperatre = 70

    # Private data variable to store all the data needed for the back end
    data = {
        "line" : 0,                          # Selected line
        "blockNo" : 0,                       # Selected Block Number
        "switchPos" : DynamicArray(),        # Position of switches
        "sigState" : DynamicArray(),         # States of signals on each block next to a switch
        "gatePos" : DynamicArray(),          # Position of crossing gates
        "temp" : current_temperature,        # Outdoor temperature
        "numPassengers" : [222, 222, 0, 0, 0, 0,
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
        0, 0, 0, 0, 0, 0],                   # block of the front of the train
        "trainLine" : [0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0],                   # train line
        "trackHeater" : tHeater,             # State of track heater (on/off)
        "blockTrainNoRed" : DynamicArray(),  # Train number on each block   
        "blockTrainNoGreen" : DynamicArray(),             
        "stationOccupancy" : DynamicArray(), # Number of people at each station
        "rtc"              : "",
        "prevRTC"          : "",
        "powerStatus": 0,                    # Power failure state
        "circuitStatusRed" : DynamicArray(),     # Track circuit failure states
        "circuitStatusGreen" : DynamicArray(),
        "railStatusRed" : DynamicArray(),        # Broken rail failure states
        "railStatusGreen" : DynamicArray(),
        "redAuthority" : DynamicArray(),         # authority of each block
        "redCommandedSpeed" : DynamicArray(),    # commanded speed of each block
        "greenAuthority" : DynamicArray(),
        "greenCommandedSpeed" : DynamicArray(),
        "val" : 0,
        "nextBlock" : 0,
        "blockDel" : 0,
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

        TkMWCSignals.authoritySignal.connect(self.authHandler)
        TkMWCSignals.commandedSpeedSignal.connect(self.cSpeedHandler)
        TkMWCSignals.switchStateSignal.connect(self.getSwitchPositionInput)
        TkMWCSignals.signalStateSignal.connect(self.getSignalStateInput)

        rtcSignals.rtcSignal.connect(self.realTimeHandler)

        self.data["rtc"] = datetime.now().isoformat() + "0-05:00"
        self.data["prevRTC"] = datetime.now().isoformat() + "0-05:00"

    # Handler for RTC
    def realTimeHandler(self, rtc):
        self.data["rtc"] = rtc
        # Random number of passengers arrive every n = 20 seconds
        if int(self.findTimeDifference()) % 20 == 0 and int(self.findTimeDifference()) == self.data["val"]:
            for i in range(self.data["stationOccupancy"].__len__()):
                self.generatePassengers(i)
            self.data["val"] += 20

    # Get time
    def findTimeDifference(self):
        if (self.data["prevRTC"] == "") & (self.data["rtc"] == ""):
            return 0
        if (self.data["prevRTC"] == "") & (self.data["rtc"] != ""):
            return 1
        currTime = datetime.fromisoformat(self.data["rtc"])
        prevTime = datetime.fromisoformat(self.data["prevRTC"])
        newTime = currTime - prevTime
        return float(newTime.total_seconds())

    # Handler for when a new train is made
    def newTrainMade(self, id, line):
        if (line == "Green"):
            self.data["trainLine"][id - 1] = 1
            self.data["moves"][id - 1] = [0, 63, None]
            TMTkMSignals.authoritySignal.emit(id, 1)
            TMTkMSignals.commandedSpeedSignal.emit(id, 1)
        elif(line == "Red"):
            self.data["trainLine"][id - 1] = 0
            self.data["moves"][id - 1] = [0, 9, None]
            TMTkMSignals.authoritySignal.emit(id, 0)
            TMTkMSignals.commandedSpeedSignal.emit(id, 0)
        else:
            print("Something")

    # Handler PassengersExiting signal from the train model
    def passengersExiting(self, id, num):
        if (num > 0) & ~self.runOnce:
            self.passengersGettingOff(id, num)
            self.passengersGettingOn(id)
            if self.data["trainLine"][id - 1] == 1 and self.csvConstants["stationGreen"].__getitem__(int(self.data["trainBlock"][id - 1]) - 1) == 0:
                self.runOnce = False
            elif self.data["trainLine"][id - 1] == 0 and self.csvConstants["stationRed"].__getitem__(int(self.data["trainBlock"][id - 1]) - 1) == 0:
                self.runOnce = False

    # Hander for the current block from the Train Model
    def currBlockHandler(self, id, currBlock, prevBlock, transition, backTrain):
        if (backTrain):
            self.data["nextBlock"] = 0
        else:
            self.data["nextBlock"] = 1
        
        # Setting CMD Speed and Authority during real time operations
        if (currBlock != 0):
            if self.data["trainLine"][id - 1] == 0:
                self.data["authority"][id - 1] = int(self.data["redAuthority"].__getitem(currBlock - 1))
                self.data["commandedSpeed"][id - 1] = float(self.data["redCommandedSpeed"].__getitem(currBlock - 1))
                TMTkMSignals.authoritySignal.emit(id, self.data["authority"][id - 1])
                TMTkMSignals.commandedSpeedSignal.emit(id, self.data["commandedSpeed"][id - 1])
            elif self.data["trainLine"][id - 1] == 1:
                self.data["authority"][id - 1] = int(self.data["greenAuthority"].__getitem(currBlock - 1))
                self.data["commandedSpeed"][id - 1] = float(self.data["greenCommandedSpeed"].__getitem(currBlock - 1))
                TMTkMSignals.authoritySignal.emit(id, self.data["authority"][id - 1])
                TMTkMSignals.commandedSpeedSignal.emit(id, self.data["commandedSpeed"][id - 1])

        if self.data["trainLine"][id - 1] == 0 and transition:
            TMTkMSignals.blockLengthSignal.emit(id, float(self.csvConstants["lengthRed"].__getitem__(currBlock - 1)))
            TMTkMSignals.elevationSignal.emit(id, float(self.csvConstants["elevationRed"].__getitem__(currBlock - 1)))
            TMTkMSignals.undergroundStateSignal.emit(id, bool(int(self.csvConstants["undergroundRed"].__getitem__(currBlock - 1))))
            if (prevBlock == 0):
                TMTkMSignals.switchSignal.emit(id, 0)
                TMTkMSignals.switchStateSignal.emit(id, 1)
            elif (int(self.csvConstants["switchRed"].__getitem__(currBlock - 1)) > 0) & (int(self.csvConstants["switchRed"].__getitem__(prevBlock - 1)) > 0):
                TMTkMSignals.switchSignal.emit(id, 0)
                TMTkMSignals.switchStateSignal.emit(id, bool(self.data["switchPos"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(currBlock - 1)) - 1)))
            elif (int(self.csvConstants["switchRed"].__getitem__(currBlock - 1)) > 0):
                TMTkMSignals.switchSignal.emit(id, 1)
                TMTkMSignals.switchStateSignal.emit(id, bool(self.data["switchPos"].__getitem__(int(self.csvConstants["switchRed"].__getitem__(currBlock - 1)) - 1)))
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
                self.getTrainBlockInputFunction(index, id - 1, 0)
        elif self.data["trainLine"][id - 1] == 1 and transition:
            TMTkMSignals.blockLengthSignal.emit(id, float(self.csvConstants["lengthGreen"].__getitem__(currBlock - 1)))
            TMTkMSignals.elevationSignal.emit(id, float(self.csvConstants["elevationGreen"].__getitem__(currBlock - 1)))
            TMTkMSignals.undergroundStateSignal.emit(id, bool(int(self.csvConstants["undergroundGreen"].__getitem__(currBlock - 1))))
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
                self.getTrainBlockInputFunction(index, id - 1, 0)
            #self.data["nextBlock"] = 1
        elif self.data["nextBlock"] == 1:
            self.data["nextBlock"] = 0
            if (currBlock == self.data["moves"][id - 1][0]):
                index = 0
            elif (currBlock == self.data["moves"][id - 1][1]):
                index = 1
            elif (currBlock == self.data["moves"][id - 1][2]):
                index = 2
            if (index == 0):
                self.getTrainBlockInputFunction(index, id - 1, 1)
        else:
            TMTkMSignals.beaconSignal.emit(id, "", 0, "", 0, -1, 0, -1)

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
    def getTrainBlockInputFunction(self, index, trainNo, state):
        # Update block train number
        # Sets last block train was at to 0
        if state == 1:
            if self.data["trainLine"][trainNo] == 0 and self.data["blockDel"] != 0:
                self.data["blockTrainNoRed"].removeAt(self.data["blockDel"] - 1)
                self.data["blockTrainNoRed"].insertAt(0, self.data["blockDel"] - 1)
                TkMWCSignals.currBlockSignal.emit(0, False, self.data["blockDel"])
            elif self.data["trainLine"][trainNo] == 1 and self.data["blockDel"] != 0:
                self.data["blockTrainNoGreen"].removeAt(self.data["blockDel"] - 1)
                self.data["blockTrainNoGreen"].insertAt(0, self.data["blockDel"] - 1)
                TkMWCSignals.currBlockSignal.emit(1, False, self.data["blockDel"])

        # Sets train number to new block
        if state == 0:
            self.data["blockDel"] = self.data["moves"][trainNo][0]
            if self.data["trainLine"][trainNo] == 0 and self.data["moves"][trainNo][index] != 0:
                self.data["blockTrainNoRed"].removeAt(self.data["moves"][trainNo][index] - 1)
                self.data["blockTrainNoRed"].insertAt(trainNo + 1, self.data["moves"][trainNo][index] - 1)
                TkMWCSignals.currBlockSignal.emit(1, True, self.data["moves"][trainNo][index])
            elif self.data["trainLine"][trainNo] == 1 and self.data["moves"][trainNo][index] != 0:
                self.data["blockTrainNoGreen"].removeAt(self.data["moves"][trainNo][index] - 1)
                self.data["blockTrainNoGreen"].insertAt(trainNo + 1, self.data["moves"][trainNo][index] - 1)
                TkMWCSignals.currBlockSignal.emit(1, True, self.data["moves"][trainNo][index])

            # Update Authority
            #if (self.data["authority"][trainNo] != 0):  
            #    self.data["authority"][trainNo] -= 1
            #TMTkMSignals.authoritySignal.emit(trainNo + 1, self.data["authority"][trainNo])

            # Send Beacon
            # If train line is red
            if self.data["trainLine"][trainNo] == 0:
                # If next block is not the yard
                if (int(self.data["moves"][trainNo][index] - 1) > 0):
                    # If next block is a station or principal switch block
                    if (int(self.csvConstants["stationRed"].__getitem__(self.data["moves"][trainNo][index] - 1)) > 0 or int(self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][index] - 1)[4]) != -1):
                        # Emit beacon before station or switch
                        beaconArr = self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][0] - 1)
                        TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), int(beaconArr[4]), bool(beaconArr[5]), int(beaconArr[6]))
                # If current block is not the yard
                elif (int(self.data["moves"][trainNo][0] - 1) > 0):
                    # If current block is a station or a principal switch block
                    if (int(self.csvConstants["stationRed"].__getitem__(self.data["moves"][trainNo][0] - 1)) > 0 or int(self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][0] - 1)[4]) != -1):
                        # Emit beacon after station or switch
                        beaconArr = self.csvConstants["beaconRed"].__getitem__(self.data["moves"][trainNo][index] - 1)
                        TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), int(beaconArr[4]), bool(beaconArr[5]), int(beaconArr[6]))
                else:
                    # Emit empty beacon
                    TMTkMSignals.beaconSignal.emit(trainNo + 1, "", 0, "", 0, -1, 0, -1)
            elif self.data["trainLine"][trainNo] == 1:
                if (int(self.data["moves"][trainNo][index] - 1) > 0):
                    if (int(self.csvConstants["stationGreen"].__getitem__(self.data["moves"][trainNo][index] - 1)) > 0 or int(self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][index] - 1)[4]) != -1):
                        beaconArr = self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)
                        TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), int(beaconArr[4]), bool(beaconArr[5]), int(beaconArr[6]))
                elif (int(self.data["moves"][trainNo][0] - 1) > 0):
                    if (int(self.csvConstants["stationGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)) > 0 or int(self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][0] - 1)[4]) != -1):
                        beaconArr = self.csvConstants["beaconGreen"].__getitem__(self.data["moves"][trainNo][index] - 1)
                        TMTkMSignals.beaconSignal.emit(trainNo + 1, beaconArr[0], int(beaconArr[1]), beaconArr[2], bool(beaconArr[3]), int(beaconArr[4]), bool(beaconArr[5]), int(beaconArr[6]))
                else:
                    TMTkMSignals.beaconSignal.emit(trainNo + 1, "", 0, "", 0, -1, 0, -1)

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
                if int(self.data["blockTrainNoRed"].__getitem__(i)) > 0 and int(self.csvConstants["stationRed"].__getitem__(i)) > 0 and int(self.csvConstants["stationRed"].__getitem__(i)) - 1 == sName and int(self.data["stationOccupancy"].__getitem__(sName)) - passengers >= 0:
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
            passOn = randint(0, int(self.data["stationOccupancy"].__getitem__(int(self.csvConstants["stationRed"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1)))
            self.getOnInput(int(self.csvConstants["stationRed"].__getitem__(self.data["trainBlock"][trainNo - 1] - 1)) - 1, passOn)
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

    # Between 0 and 5 passengers buy tickets at station every n seconds
    def generatePassengers(self, stationID):
        currOcc = self.data["stationOccupancy"].__getitem__(stationID)
        self.data["stationOccupancy"].removeAt(stationID)
        self.data["stationOccupancy"].insertAt(currOcc + randint(0, 5), stationID)

        trackSignals.updateSignal.emit()

    # Wayside authority handler
    def authHandler(self, blockNo, auth, line):
        if line == 0:
            self.data["redAuthority"].removeAt(blockNo - 1) 
            self.data["redAuthority"].insertAt(auth, blockNo - 1)
        elif line == 1:
            self.data["greenAuthority"].removeAt(blockNo - 1) 
            self.data["greenAuthority"].insertAt(auth, blockNo - 1)

    # Wayside commanded speed handler
    def cSpeedHandler(self, blockNo, cSpeed, line):
        if line == 0:
            self.data["redCommandedSpeed"].removeAt(blockNo - 1)
            self.data["redCommandedSpeed"].removeAt(cSpeed, blockNo - 1)
        elif line == 1:
            self.data["greenCommandedSpeed"].removeAt(blockNo - 1)
            self.data["greenCommandedSpeed"].removeAt(cSpeed, blockNo - 1)


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
        backEndCalculations.csvConstants["beaconRed"].append([row["b0"], row["b1"], row["b2"], row["b3"], row["b4"], row["b5"], row["b6"]])
        backEndCalculations.data["blockTrainNoRed"].append(0)
        backEndCalculations.data["circuitStatusRed"].append(0)
        backEndCalculations.data["railStatusRed"].append(0)
        backEndCalculations.data["redAuthority"].append(0)
        backEndCalculations.data["redCommandedSpeed"].append(0)
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
        backEndCalculations.csvConstants["beaconGreen"].append([row["b0"], row["b1"], row["b2"], row["b3"], row["b4"], row["b5"], row["b6"]])
        backEndCalculations.data["blockTrainNoGreen"].append(0)
        backEndCalculations.data["circuitStatusGreen"].append(0)
        backEndCalculations.data["railStatusGreen"].append(0)
        backEndCalculations.data["greenAuthority"].append(0)
        backEndCalculations.data["greenCommandedSpeed"].append(0)
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
        if row == 9 or row == 10:
            backEndCalculations.data["switchPos"].append(1)
        else:
            backEndCalculations.data["switchPos"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)
        backEndCalculations.data["sigState"].append(0)