# UI for the Train Model

# QTimer for Simulation

# Imports needed for the UI
from sys import argv
from TrackModelBackEnd import *
from TrackModelSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

# Class for the Main UI of the Train Model
class TrackModelMainUI(QWidget):

    # Instantiating the Back End
    backEnd = backEndCalculations()

    # Fonts and Alignments to make coding easier
    timesNewRoman8 = QFont("Times New Roman", 10)
    spaceString = "         "

    # Initialization of the UI
    def __init__(self):

        # Initializing and setting the layout of the UI
        super().__init__()
        self.setWindowTitle("Track Model")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        orientation = self.frameGeometry()
        self.move(orientation.center())

        # Create track block data
        self.lineLabel = QLabel(self.spaceString + "Line: Red")
        self.lineLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.lineLabel, 0, 8)

        self.blockNumLabel = QLabel(self.spaceString + "Block # Selected: 1")
        self.blockNumLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.blockNumLabel, 1, 8)

        self.elevationLabel = QLabel(self.spaceString + "Elevation: 0.82 ft")
        self.elevationLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.elevationLabel, 2, 8)

        self.gradeLabel = QLabel(self.spaceString + "Grade: 0.5%")
        self.gradeLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.gradeLabel, 3, 8)

        self.lengthLabel = QLabel(self.spaceString + "Length : 164.04 ft")
        self.lengthLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.lengthLabel, 4, 8)

        self.limitLabel = QLabel(self.spaceString + "Speed Limit: 24.85 MPH")
        self.limitLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.limitLabel, 5, 8)

        self.undergroundLabel = QLabel(self.spaceString + "Underground: No")
        self.undergroundLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.undergroundLabel, 6, 8)

        self.signal = QLineEdit()
        self.signal.setReadOnly(True)
        self.signal.setFixedWidth(20)
        self.signal.setStyleSheet("background-color : green")
        layout.addWidget(self.signal, 3, 0)

        # Create Station data
        self.sNameLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString + self.spaceString + "   ")
        self.sNameLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.sNameLabel, 0, 0)

        self.sOccLbl = QLabel("")
        self.sOccLbl.setFont(self.timesNewRoman8)
        layout.addWidget(self.sOccLbl, 1, 0)

        self.stationSideLabel = QLabel("")
        self.stationSideLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.stationSideLabel, 2, 0)

        # Create train data
        self.numPassengersLbl = QLabel("")
        self.numPassengersLbl.setFont(self.timesNewRoman8)
        layout.addWidget(self.numPassengersLbl, 4, 0)

        self.cSpeedLbl = QLabel("")
        self.cSpeedLbl.setFont(self.timesNewRoman8)
        layout.addWidget(self.cSpeedLbl, 5, 0)

        self.authLbl = QLabel("")
        self.authLbl.setFont(self.timesNewRoman8)
        layout.addWidget(self.authLbl, 6, 0)

        # Create combo boxes
        # Add the Line
        self.lineInput = QComboBox()
        self.lineInput.addItems(["Red", "Green"])
        self.lineInput.currentIndexChanged.connect(self.getLineInput)
        layout.addWidget(self.lineInput, 3, 2)

        # Add the Block Number
        self.blockInput = QComboBox()
        i = 0
        while i < int(self.backEnd.csvConstants["redBlocks"].__len__()):
            self.blockInput.addItem(self.backEnd.csvConstants["redBlocks"].__getitem__(i))
            i += 1
        self.blockInput.currentIndexChanged.connect(self.getBlockInput)
        self.blockInput.currentIndexChanged.connect(self.showData)
        layout.addWidget(self.blockInput, 3, 4)

        # Create track block buttons
        # self.trackBlock1 = QPushButton("1")
        # self.trackBlock1.setFont(self.timesNewRoman8)
        # self.trackBlock1.pressed.connect(self.showTrackData1)
        # if self.backEnd.data["blockTrainNoGreen"][0] > 0:
        #     self.trackBlock1.setStyleSheet("background-color : light grey; color: black ")
        # else:
        #     self.trackBlock1.setStyleSheet("background-color : blue; color: white ")
        # layout.addWidget(self.trackBlock1, 3, 1, 1, 1)

        # stationB = QPushButton("Station B")
        # stationB.setFont(self.timesNewRoman8)
        # stationB.pressed.connect(self.showStationDataB)
        # stationB.setStyleSheet("background-color : white")
        # layout.addWidget(stationB, 1, 10, 1, 1)

        # Murphy Label
        murphyLabel = QLabel("Failure States")
        murphyLabel.setFont(self.timesNewRoman8)
        layout.addWidget(murphyLabel, 7, 1)

        # Power Label and Button
        self.powerButton = QPushButton("Lose Power")
        self.powerButton.setStyleSheet("background-color: green; color: white")
        self.powerButton.setFont(self.timesNewRoman8)
        self.powerButton.pressed.connect(self.powerButtonPressed)
        layout.addWidget(self.powerButton, 7, 2)

        # Track circuit Label and Button
        self.circuitButton = QPushButton("Short Circuit")
        self.circuitButton.setStyleSheet("background-color: green; color: white")
        self.circuitButton.pressed.connect(self.trackCircuitButtonPressed)
        self.circuitButton.setFont(self.timesNewRoman8)
        layout.addWidget(self.circuitButton, 7, 3)

        # Broken Rail Label and Button
        self.brokenRailButton = QPushButton("Break Rail")
        self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        self.brokenRailButton.pressed.connect(self.brokenRailButtonPressed)
        self.brokenRailButton.setFont(self.timesNewRoman8)
        layout.addWidget(self.brokenRailButton, 7, 4)

        # Switch label
        self.switchLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString)
        self.switchLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.switchLabel, 7, 5)

        # Temperature Label
        self.tempLabel = QLabel("Temp: " + str(self.backEnd.data["temp"]) + " F")
        self.tempLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.tempLabel, 7, 6)

        # Heaters Label
        outputTxt = "On" if self.backEnd.data["trackHeater"] == 1 else "Off"
        self.heatersLabel = QLabel("Heaters: " + outputTxt)
        self.heatersLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.heatersLabel, 7, 7)

        # Gate Label
        self.gateLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString)
        self.gateLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.gateLabel, 7, 8)

        # Bottom insurance labels
        layout.addWidget(QLabel("                                                                        "), 8, 0)
        layout.addWidget(QLabel("                          "), 8, 1)
        layout.addWidget(QLabel("                          "), 8, 2)
        layout.addWidget(QLabel("                          "), 8, 3)
        layout.addWidget(QLabel("                          "), 8, 4)
        layout.addWidget(QLabel("                                         "), 8, 5)
        layout.addWidget(QLabel("                          "), 8, 6)
        layout.addWidget(QLabel("                          "), 8, 7)
        layout.addWidget(QLabel("                                                        "), 8, 8)

        # Call function if signal is pressed
        trackSignals.updateSignal.connect(self.updateInterface)

    # Shows track block stats if track block is clicked
    def showData(self):
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] != -1 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__():
            self.lineLabel.setText(self.spaceString + "Line: Red")
            self.blockNumLabel.setText(self.spaceString + "Block # Selected: " + str(self.backEnd.data["blockNo"] + 1))
            self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(float(self.backEnd.csvConstants["elevationRed"].__getitem__(self.backEnd.data["blockNo"])) * 3.28084, 2)) + " ft")
            self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["gradeRed"].__getitem__(self.backEnd.data["blockNo"])) + "%")
            self.lengthLabel.setText(self.spaceString + "Length: " + str(round(float(self.backEnd.csvConstants["lengthRed"].__getitem__(self.backEnd.data["blockNo"])) * 3.28084, 2)) + " ft")
            self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(float(self.backEnd.csvConstants["speedLimitRed"].__getitem__(self.backEnd.data["blockNo"])) * 0.621371, 2)) + " MPH")
            outUnderground = "Yes" if int(self.backEnd.csvConstants["undergroundRed"].__getitem__(self.backEnd.data["blockNo"])) == 1 else "No"
            self.undergroundLabel.setText(self.spaceString + "Underground: " + outUnderground)
            self.signal.setVisible(True)
            if int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 0:
                self.signal.setStyleSheet("background-color : green")
            elif int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1:
                self.signal.setStyleSheet("background-color : yellow")
            elif int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 2:
                self.signal.setStyleSheet("background-color : red")
            else:
               self.signal.setVisible(False) 

        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1:
            self.lineLabel.setText(self.spaceString + "Line: Green")
            self.blockNumLabel.setText(self.spaceString + "Block # Selected: " + str(self.backEnd.data["blockNo"] + 1))
            self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(float(self.backEnd.csvConstants["elevationGreen"].__getitem__(self.backEnd.data["blockNo"])) * 3.28084, 2)) + " ft")
            self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["gradeGreen"].__getitem__(self.backEnd.data["blockNo"])) + "%")
            self.lengthLabel.setText(self.spaceString + "Length: " + str(round(float(self.backEnd.csvConstants["lengthGreen"].__getitem__(self.backEnd.data["blockNo"])) * 3.28084, 2)) + " ft")
            self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(float(self.backEnd.csvConstants["speedLimitGreen"].__getitem__(self.backEnd.data["blockNo"])) * 0.621371, 2)) + " MPH")
            outUnderground = "Yes" if int(self.backEnd.csvConstants["undergroundGreen"].__getitem__(self.backEnd.data["blockNo"])) == 1 else "No"
            self.undergroundLabel.setText(self.spaceString + "Underground: " + outUnderground)
            self.signal.setVisible(True)
            if int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 0:
                self.signal.setStyleSheet("background-color : green")
            elif int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1:
                self.signal.setStyleSheet("background-color : yellow")
            elif int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 2:
                self.signal.setStyleSheet("background-color : red")
            else:
                self.signal.setVisible(False) 

        # Show train data if block has train
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and self.backEnd.data["blockTrainNoRed"].__getitem__(self.backEnd.data["blockNo"]) > 0:
            self.numPassengersLbl.setVisible(True)
            self.cSpeedLbl.setVisible(True)
            self.authLbl.setVisible(True)
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNoRed"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNoRed"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNoRed"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " blocks")
        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and self.backEnd.data["blockTrainNoGreen"].__getitem__(self.backEnd.data["blockNo"]) > 0:
            self.numPassengersLbl.setVisible(True)
            self.cSpeedLbl.setVisible(True)
            self.authLbl.setVisible(True)
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNoGreen"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNoGreen"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNoGreen"].__getitem__(self.backEnd.data["blockNo"]) - 1]) + " blocks")
        else:
            self.numPassengersLbl.setVisible(False)
            self.cSpeedLbl.setVisible(False)
            self.authLbl.setVisible(False)

        # Show station data if block has station
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            if int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 2:
                outLbl = "Both"
            elif int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 1:
                outLbl = "Right"
            elif int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outLbl = "Left"

            self.sNameLabel.setVisible(True)
            self.sOccLbl.setVisible(True)
            self.stationSideLabel.setVisible(True)
            self.sNameLabel.setText("Station Name: " + self.backEnd.csvConstants["stationName"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)))
            self.stationSideLabel.setText("Station Side: " + outLbl)
        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            if int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 2:
                outLbl = "Both"
            elif int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 1:
                outLbl = "Right"
            elif int(self.backEnd.csvConstants["stationSide"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outLbl = "Left"

            self.sNameLabel.setVisible(True)
            self.sOccLbl.setVisible(True)
            self.stationSideLabel.setVisible(True)
            self.sNameLabel.setText("Station Name: " + self.backEnd.csvConstants["stationName"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)))
            self.stationSideLabel.setText("Station Side: " + outLbl)
        else:
            self.sNameLabel.setVisible(False)
            self.sOccLbl.setVisible(False)
            self.stationSideLabel.setVisible(False)

        # Update failure modes
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and (self.backEnd.data["circuitStatusRed"].__getitem__(self.backEnd.data["blockNo"]) == 0):
            self.circuitButton.setStyleSheet("background-color: green; color: white")
        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and (self.backEnd.data["circuitStatusGreen"].__getitem__(self.backEnd.data["blockNo"]) == 0):
            self.circuitButton.setStyleSheet("background-color: green; color: white")
        else:
            self.circuitButton.setStyleSheet("background-color: red")

        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and (self.backEnd.data["railStatusRed"].__getitem__(self.backEnd.data["blockNo"]) == 0):
            self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and (self.backEnd.data["railStatusGreen"].__getitem__(self.backEnd.data["blockNo"]) == 0):
            self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        else:
            self.brokenRailButton.setStyleSheet("background-color: red")

        if self.backEnd.data["powerStatus"] == 0:
            self.powerButton.setStyleSheet("background-color: green; color: white")
        else:
            self.powerButton.setStyleSheet("background-color: red")

        # Get switch state
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["blockNo"] + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.switchLabel.setText("   Switch Pos: " + outputText1)

        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["blockNo"] + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.switchLabel.setText("   Switch Pos: " + outputText1)
        else:
            self.switchLabel.setText("")

        # Get gate state
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockNo"] < self.backEnd.csvConstants["redBlocks"].__len__() and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["crossingRed"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            outputText2 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 else "Up"
            self.gateLabel.setText(self.spaceString + "Gate Pos: " + outputText2)

        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockNo"] != -1 and int(self.backEnd.csvConstants["crossingGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            outputText2 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 else "Up"
            self.gateLabel.setText(self.spaceString + "Gate Pos: " + outputText2)
        else:
            self.gateLabel.setText("")
        

    def showTrackData1(self):
        self.showData(0)

    # Updates outputs every time period
    def updateInterface(self):
        # Update track blocks
        # if self.backEnd.data["blockTrainNoGreen"][0] > 0:
        #     self.trackBlock1.setStyleSheet("background-color : light grey; color: black ")
        # else:
        #     self.trackBlock1.setStyleSheet("background-color : Blue; color: white ")

        # Update Stations  
        if self.backEnd.data["line"] == 0 and int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            self.sOccLbl.setVisible(True)
            self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"].__getitem__(int(self.backEnd.csvConstants["stationRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)))
        elif self.backEnd.data["line"] == 1 and int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            self.sOccLbl.setVisible(True)
            self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"].__getitem__(int(self.backEnd.csvConstants["stationGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)))
        else:
            self.sOccLbl.setVisible(False)

        # Update train labels
        if self.backEnd.data["line"] == 0 and self.backEnd.data["blockTrainNoRed"][self.backEnd.data["blockNo"]] == 0:
            self.numPassengersLbl.setVisible(False)
            self.cSpeedLbl.setVisible(False)
            self.authLbl.setVisible(False)
        elif self.backEnd.data["line"] == 1 and self.backEnd.data["blockTrainNoGreen"][self.backEnd.data["blockNo"]] == 0:
            self.numPassengersLbl.setVisible(False)
            self.cSpeedLbl.setVisible(False)
            self.authLbl.setVisible(False)
        else:
            self.numPassengersLbl.setVisible(True)
            self.cSpeedLbl.setVisible(True)
            self.authLbl.setVisible(True)
            if self.backEnd.data["line"] == 0:
                self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNoRed"][self.backEnd.data["blockNo"]] - 1]) + " people")
                self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNoRed"][self.backEnd.data["blockNo"]] - 1]) + " MPH")
                self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNoRed"][self.backEnd.data["blockNo"]] - 1]) + " blocks")
            else:
                self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNoGreen"][self.backEnd.data["blockNo"]] - 1]) + " people")
                self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNoGreen"][self.backEnd.data["blockNo"]] - 1]) + " MPH")
                self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNoGreen"][self.backEnd.data["blockNo"]] - 1]) + " blocks")

        # Update Track heater and temp
        self.tempLabel.setText("Temp: " + str(self.backEnd.data["temp"]) + " F")
        outputTxt = "On" if self.backEnd.data["trackHeater"] == 1 else "Off"
        self.heatersLabel.setText("Heaters: " + outputTxt)

        # Update Gate
        if self.backEnd.data["line"] == 0 and int(self.backEnd.csvConstants["crossingRed"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            outputText2 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 else "Up"
            self.gateLabel.setVisible(True)
            self.gateLabel.setText(self.spaceString + "Gate Pos: " + outputText2)

        elif self.backEnd.data["line"] == 1 and int(self.backEnd.csvConstants["crossingGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            outputText2 = "Down" if self.backEnd.data["gatePos"].__getitem__(int(self.backEnd.csvConstants["crossingGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 else "Up"
            self.gateLabel.setVisible(True)
            self.gateLabel.setText(self.spaceString + "Gate Pos: " + outputText2)

        # Update Switch
        if self.backEnd.data["line"] == 0 and int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["blockNo"] + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchRed"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.switchLabel.setVisible(True)
            self.switchLabel.setText("   Switch Pos: " + outputText1)

        elif self.backEnd.data["line"] == 1 and int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0 and self.backEnd.data["blockNo"] + 1 == int(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)):
            if self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) != 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            elif self.backEnd.data["switchPos"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1 and int(self.backEnd.csvConstants["switchBlockB"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) == 0:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-Yard"
            else:
                outputText1 = str(self.backEnd.csvConstants["switchBlockA"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1)) + "-" + str(self.backEnd.csvConstants["switchBlockC"].__getitem__(int(self.backEnd.csvConstants["switchGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1))
            self.switchLabel.setVisible(True)
            self.switchLabel.setText("   Switch Pos: " + outputText1)

        # Update Signal
        if self.backEnd.data["line"] == 0 and int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            self.signal.setVisible(True)
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 2:
                self.signal.setStyleSheet("background-color : red")
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalRed"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1:
                self.signal.setStyleSheet("background-color : yellow")
            else:
                self.signal.setStyleSheet("background-color : green")
        elif self.backEnd.data["line"] == 1 and int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) > 0:
            self.signal.setVisible(True)
            if self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 2:
                self.signal.setStyleSheet("background-color : red")
            elif self.backEnd.data["sigState"].__getitem__(int(self.backEnd.csvConstants["signalGreen"].__getitem__(self.backEnd.data["blockNo"])) - 1) == 1:
                self.signal.setStyleSheet("background-color : yellow")
            else:
                self.signal.setStyleSheet("background-color : green")
        else:
            self.signal.setVisible(False)

    # Handler for when Power Failure button is pressed
    def powerButtonPressed(self):
        trackSignals.powerPressedSignal.emit()
        self.backEnd.data["powerStatus"] = 1 if self.backEnd.data["powerStatus"] == 0 else 0
        if (self.backEnd.data["powerStatus"] == 0):
            self.powerButton.setStyleSheet("background-color: green; color: white")
        else:
            self.powerButton.setStyleSheet("background-color: red")
        
    # Handler for when Engine Failure State button is pressed
    def trackCircuitButtonPressed(self):
        trackSignals.trackCircuitPressedSignal.emit()
        if self.backEnd.data["line"] == 0:
            if self.backEnd.data["circuitStatusRed"][self.backEnd.data["blockNo"]] == 0:
                self.backEnd.data["circuitStatusRed"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["circuitStatusRed"].insertAt(1, self.backEnd.data["blockNo"])
                self.circuitButton.setStyleSheet("background-color: red")
            else:
                self.backEnd.data["circuitStatusRed"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["circuitStatusRed"].insertAt(0, self.backEnd.data["blockNo"])
                self.circuitButton.setStyleSheet("background-color: green; color: white")
        elif self.backEnd.data["line"] == 1:
            if self.backEnd.data["circuitStatusGreen"][self.backEnd.data["blockNo"]] == 0:
                self.backEnd.data["circuitStatusGreen"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["circuitStatusGreen"].insertAt(1, self.backEnd.data["blockNo"])
                self.circuitButton.setStyleSheet("background-color: red")
            else:
                self.backEnd.data["circuitStatusGreen"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["circuitStatusGreen"].insertAt(0, self.backEnd.data["blockNo"])
                self.circuitButton.setStyleSheet("background-color: green; color: white")

    # Handler for when Brake Failure State button is pressed
    def brokenRailButtonPressed(self):
        trackSignals.brokenRailPressedSignal.emit()
        if self.backEnd.data["line"] == 0:
            if self.backEnd.data["railStatusRed"][self.backEnd.data["blockNo"]] == 0:
                self.backEnd.data["railStatusRed"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["railStatusRed"].insertAt(1, self.backEnd.data["blockNo"])
                self.brokenRailButton.setStyleSheet("background-color: red")
            else:
                self.backEnd.data["railStatusRed"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["railStatusRed"].insertAt(0, self.backEnd.data["blockNo"])
                self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        elif self.backEnd.data["line"] == 1:
            if self.backEnd.data["railStatusGreen"][self.backEnd.data["blockNo"]] == 0:
                self.backEnd.data["railStatusGreen"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["railStatusGreen"].insertAt(1, self.backEnd.data["blockNo"])
                self.brokenRailButton.setStyleSheet("background-color: red")
            else:
                self.backEnd.data["railStatusGreen"].removeAt(self.backEnd.data["blockNo"])
                self.backEnd.data["railStatusGreen"].insertAt(0, self.backEnd.data["blockNo"])
                self.brokenRailButton.setStyleSheet("background-color: green; color: white")

    # Gets the Line from the UI
    def getLineInput(self, index):
        self.backEnd.data["line"] = index

        # Set new combo box values
        self.backEnd.data["blockNo"] = 0
        i = self.blockInput.count() - 1
        while i >= 0:
                self.blockInput.removeItem(i)
                i -= 1
        i = 0
        if index == 0:
            while i < int(self.backEnd.csvConstants["redBlocks"].__len__()):
                self.blockInput.addItem(self.backEnd.csvConstants["redBlocks"].__getitem__(i))
                i += 1
        elif index == 1:
            while i < int(self.backEnd.csvConstants["greenBlocks"].__len__()):
                self.blockInput.addItem(self.backEnd.csvConstants["greenBlocks"].__getitem__(i))
                i += 1

        # Set Block number equal to one
        self.blockInput.setCurrentText("1")
        self.showData()
    
    # Gets the Block Number from the UI
    def getBlockInput(self, index):
        self.backEnd.data["blockNo"] = index

def main():
    mainApp = QApplication(argv)
    UI = TrackModelMainUI()
    UI.show()
    mainApp.exec()

if (__name__ == "__main__"):
    main()