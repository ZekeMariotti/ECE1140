# UI for the Train Model

# QTimer for Simulation

# Imports needed for the UI
from sys import argv
from TrackModelBackEnd import *
from TrackModelSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Conversions import *

# Class for the Main UI of the Train Model
class TrackModelMainUI(QWidget):

    # Instantiating the Back End
    backEnd = backEndCalculations()

    # Fonts and Alignments to make coding easier
    timesNewRoman8 = QFont("Times New Roman", 8)
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
        self.lineLabel = QLabel("")
        layout.addWidget(self.lineLabel, 0, 11)

        self.blockNumLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString + self.spaceString + "     ")
        layout.addWidget(self.blockNumLabel, 1, 11)

        self.elevationLabel = QLabel("")
        layout.addWidget(self.elevationLabel, 2, 11)

        self.gradeLabel = QLabel("")
        layout.addWidget(self.gradeLabel, 3, 11)

        self.lengthLabel = QLabel("")
        layout.addWidget(self.lengthLabel, 4, 11)

        self.limitLabel = QLabel("")
        layout.addWidget(self.limitLabel, 5, 11)

        self.directionLabel = QLabel("")
        layout.addWidget(self.directionLabel, 6, 11)

        self.signal = QLineEdit()
        self.signal.setReadOnly(True)
        self.signal.setFixedWidth(20)
        self.signal.setVisible(False)
        layout.addWidget(self.signal, 3, 0)

        # Create Station data
        self.sNameLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString + self.spaceString + "   ")
        layout.addWidget(self.sNameLabel, 0, 0)

        self.sOccLbl = QLabel("")
        layout.addWidget(self.sOccLbl, 1, 0)

        self.stationSideLabel = QLabel("")
        layout.addWidget(self.stationSideLabel, 2, 0)

        # Create train data
        self.numPassengersLbl = QLabel("")
        layout.addWidget(self.numPassengersLbl, 4, 0)

        self.cSpeedLbl = QLabel("")
        layout.addWidget(self.cSpeedLbl, 5, 0)

        self.authLbl = QLabel("")
        layout.addWidget(self.authLbl, 6, 0)

        # Create track block buttons
        trackBlock1 = QPushButton("1")
        trackBlock1.setFont(self.timesNewRoman8)
        trackBlock1.pressed.connect(self.showTrackData1)
        if self.backEnd.data["blockTrainNo"][0] > 0:
            trackBlock1.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock1.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock1, 3, 1, 1, 1)

        trackBlock2 = QPushButton("2")
        trackBlock2.setFont(self.timesNewRoman8)
        trackBlock2.pressed.connect(self.showTrackData2)
        if self.backEnd.data["blockTrainNo"][1] > 0:
            trackBlock2.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock2.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock2, 3, 2, 1, 1)

        trackBlock3 = QPushButton("3")
        trackBlock3.setFont(self.timesNewRoman8)
        trackBlock3.pressed.connect(self.showTrackData3)
        if self.backEnd.data["blockTrainNo"][2] > 0:
            trackBlock3.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock3.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock3, 3, 3, 1, 1)

        trackBlock4 = QPushButton("4")
        trackBlock4.setFont(self.timesNewRoman8)
        trackBlock4.pressed.connect(self.showTrackData4)
        if self.backEnd.data["blockTrainNo"][3] > 0:
            trackBlock4.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock4.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock4, 3, 4, 1, 1)

        trackBlock5 = QPushButton("5")
        trackBlock5.setFont(self.timesNewRoman8)
        trackBlock5.pressed.connect(self.showTrackData5)
        if self.backEnd.data["blockTrainNo"][4] > 0:
            trackBlock5.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock5.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock5, 3, 5, 1, 1)

        trackBlock6 = QPushButton("6")
        trackBlock6.setFont(self.timesNewRoman8)
        trackBlock6.pressed.connect(self.showTrackData6)
        if self.backEnd.data["blockTrainNo"][5] > 0:
            trackBlock6.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock6.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock6, 2, 6, 1, 1)

        trackBlock7 = QPushButton("7")
        trackBlock7.setFont(self.timesNewRoman8)
        trackBlock7.pressed.connect(self.showTrackData7)
        if self.backEnd.data["blockTrainNo"][6] > 0:
            trackBlock7.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock7.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock7, 2, 7, 1, 1)

        trackBlock8 = QPushButton("8")
        trackBlock8.setFont(self.timesNewRoman8)
        trackBlock8.pressed.connect(self.showTrackData8)
        if self.backEnd.data["blockTrainNo"][7] > 0:
            trackBlock8.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock8.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock8, 2, 8, 1, 1)

        trackBlock9 = QPushButton("9")
        trackBlock9.setFont(self.timesNewRoman8)
        trackBlock9.pressed.connect(self.showTrackData9)
        if self.backEnd.data["blockTrainNo"][8] > 0:
            trackBlock9.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock9.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock9, 2, 9, 1, 1)

        trackBlock10 = QPushButton("10")
        trackBlock10.setFont(self.timesNewRoman8)
        trackBlock10.pressed.connect(self.showTrackData10)
        if self.backEnd.data["blockTrainNo"][9] > 0:
            trackBlock10.setStyleSheet("background-color : grey; color: black ")
        else:
            trackBlock10.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock10, 2, 10, 1, 1)

        trackBlock11 = QPushButton("11")
        trackBlock11.setFont(self.timesNewRoman8)
        trackBlock11.pressed.connect(self.showTrackData11)
        if self.backEnd.data["blockTrainNo"][10] > 0:
            trackBlock11.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock11.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock11, 4, 6, 1, 1)

        trackBlock12 = QPushButton("12")
        trackBlock12.setFont(self.timesNewRoman8)
        trackBlock12.pressed.connect(self.showTrackData12)
        if self.backEnd.data["blockTrainNo"][11] > 0:
            trackBlock12.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock12.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock12, 4, 7, 1, 1)

        trackBlock13 = QPushButton("13")
        trackBlock13.setFont(self.timesNewRoman8)
        trackBlock13.pressed.connect(self.showTrackData13)
        if self.backEnd.data["blockTrainNo"][12] > 0:
            trackBlock13.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock13.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock13, 4, 8, 1, 1)

        trackBlock14 = QPushButton("14")
        trackBlock14.setFont(self.timesNewRoman8)
        trackBlock14.pressed.connect(self.showTrackData14)
        if self.backEnd.data["blockTrainNo"][13] > 0:
            trackBlock14.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock14.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock14, 4, 9, 1, 1)

        trackBlock15 = QPushButton("15")
        trackBlock15.setFont(self.timesNewRoman8)
        trackBlock15.pressed.connect(self.showTrackData15)
        if self.backEnd.data["blockTrainNo"][14] > 0:
            trackBlock15.setStyleSheet("background-color : light grey; color: black ")
        else:
            trackBlock15.setStyleSheet("background-color : blue; color: white ")
        layout.addWidget(trackBlock15, 4, 10, 1, 1)

        stationB = QPushButton("Station B")
        stationB.setFont(self.timesNewRoman8)
        stationB.pressed.connect(self.showStationDataB)
        layout.addWidget(stationB, 1, 10, 1, 1)

        stationC = QPushButton("Station C")
        stationC.setFont(self.timesNewRoman8)
        stationC.pressed.connect(self.showStationDataC)
        layout.addWidget(stationC, 5, 10, 1, 1)

        # Murphy Label
        murphyLabel = QLabel("                    Failure States")
        murphyLabel.setFont(self.timesNewRoman8)
        layout.addWidget(murphyLabel, 7, 0)

        # Power Label and Button
        self.powerButton = QPushButton("Lose Power")
        self.powerButton.setStyleSheet("background-color: green; color: white")
        self.powerButton.setFont(self.timesNewRoman8)
        self.powerButton.pressed.connect(self.powerButtonPressed)

        layout.addWidget(self.powerButton, 7, 1)

        # Track circuit Label and Button
        self.circuitButton = QPushButton("Short Circuit")
        self.circuitButton.setStyleSheet("background-color: green; color: white")
        self.circuitButton.pressed.connect(self.trackCircuitButtonPressed)
        self.circuitButton.setFont(self.timesNewRoman8)

        layout.addWidget(self.circuitButton, 7, 2)

        # Broken Rail Label and Button
        self.brokenRailButton = QPushButton("Break Rail")
        self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        self.brokenRailButton.pressed.connect(self.brokenRailButtonPressed)
        self.brokenRailButton.setFont(self.timesNewRoman8)

        layout.addWidget(self.brokenRailButton, 7, 3)

        # Switch label
        self.switchLabel = QLabel("")
        self.switchLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.switchLabel, 7, 5)

        # Temperature Label
        self.tempLabel = QLabel("Temp: " + str(self.backEnd.data["temp"]) + " F")
        self.tempLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.tempLabel, 7, 7)

        # Heaters Label
        outputTxt = "On" if self.backEnd.data["trackHeater"] == 1 else "Off"
        self.heatersLabel = QLabel("Heaters: " + outputTxt)
        self.heatersLabel.setFont(self.timesNewRoman8)
        layout.addWidget(self.heatersLabel, 7, 8)

    # Shows track block stats if track block is clicked
    def showData(self, index):
        self.backEnd.data["blockNo"] = index
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: " + str(index + 1))
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][index] * 3.28084, 2)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][index]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][index] * 3.28084, 2)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][index] * 0.621371, 2)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][index] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)
        self.signal.setVisible(True)
        if self.backEnd.data["sigState"][index] == 2:
            self.signal.setStyleSheet("background-color : green")
        elif (self.backEnd.data["sigState"][index]) == 1:
            self.signal.setStyleSheet("background-color : yellow")
        else:
            self.signal.setStyleSheet("background-color : red")

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][index] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][index] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][index] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][index] - 1]) + " blocks")
        else:
            self.numPassengersLbl.setText("")
            self.cSpeedLbl.setText("")
            self.authLbl.setText("")

        # Update failure modes
        if (self.backEnd.data["circuitStatus"][self.backEnd.data["blockNo"]] == 0):
            self.circuitButton.setStyleSheet("background-color: green; color: white")
        else:
            self.circuitButton.setStyleSheet("background-color: red")

        if (self.backEnd.data["railStatus"][self.backEnd.data["blockNo"]] == 0):
            self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        else:
            self.brokenRailButton.setStyleSheet("background-color: red")

        # Get switch state
        if index == 4:
            outTxt = "5-11" if self.backEnd.data["switchPos"] == 1 else "5-6"
            self.switchLabel.setText("Switch Pos: " + outTxt)
        else:
            self.switchLabel.setText("")
        

    def showTrackData1(self):
        self.showData(0)

    def showTrackData2(self):
        self.showData(1)

    def showTrackData3(self):
        self.showData(2)

    def showTrackData4(self):
        self.showData(3)

    def showTrackData5(self):
        self.showData(4)

    def showTrackData6(self):
        self.showData(5)

    def showTrackData7(self):
        self.showData(6)

    def showTrackData8(self):
        self.showData(7)

    def showTrackData9(self):
        self.showData(8)

    def showTrackData10(self):
        self.showData(9)

    def showTrackData11(self):
        self.showData(10)

    def showTrackData12(self):
        self.showData(11)

    def showTrackData13(self):
        self.showData(12)

    def showTrackData14(self):
        self.showData(13)

    def showTrackData15(self):
        self.showData(14)

    # Shows station stats if track block is clicked
    def showStationDataB(self):
        self.sNameLabel.setText("Station Name: Station B" + self.spaceString)
        self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"][0]))
        outLbl = "Right" if (self.backEnd.csvConstants["stationSide"][0] == 1 and self.backEnd.data["direction"][9] == 0) or (self.backEnd.csvConstants["stationSide"][0] == 0 and self.backEnd.data["direction"][9] == 1) else "Left"
        self.stationSideLabel.setText("Station Side: " + outLbl)

    def showStationDataC(self):
        self.sNameLabel.setText("Station Name: Station C" + self.spaceString)
        self.sOccLbl.setText("Station Occupancy: " + str(self.backEnd.data["stationOccupancy"][1]))
        outLbl = "Right" if (self.backEnd.csvConstants["stationSide"][1] == 1 and self.backEnd.data["direction"][14] == 0) or (self.backEnd.csvConstants["stationSide"][1] == 0 and self.backEnd.data["direction"][14] == 1) else "Left"
        self.stationSideLabel.setText("Station Side: " + outLbl)
        

    # Updates outputs every time period
    def updateInterface(self):
        # Update track blocks
        if self.backEnd.data["blockTrainNo"][0] > 0:
            self.trackBlock1.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock1.setStyleSheet("background-color : light grey; color: black ")
      
        if self.backEnd.data["blockTrainNo"][1] > 0:
            self.trackBlock2.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock2.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][2] > 0:
            self.trackBlock3.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock3.setStyleSheet("background-color : light grey; color: black ")
   
        if self.backEnd.data["blockTrainNo"][3] > 0:
            self.trackBlock4.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock4.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][4] > 0:
            self.trackBlock5.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock5.setStyleSheet("background-color : light grey; color: black ")
    
        if self.backEnd.data["blockTrainNo"][5] > 0:
            self.trackBlock6.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock6.setStyleSheet("background-color : light grey; color: black ")
    
        if self.backEnd.data["blockTrainNo"][6] > 0:
            self.trackBlock7.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock7.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][7] > 0:
            self.trackBlock8.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock8.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][8] > 0:
            self.trackBlock9.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock9.setStyleSheet("background-color : light grey; color: black ")
     
        if self.backEnd.data["blockTrainNo"][9] > 0:
            self.trackBlock10.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock10.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][10] > 0:
            self.trackBlock11.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock11.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][11] > 0:
            self.trackBlock12.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock12.setStyleSheet("background-color : light grey; color: black ")

        if self.backEnd.data["blockTrainNo"][12] > 0:
            self.trackBlock13.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock13.setStyleSheet("background-color : light grey; color: black ")
  
        if self.backEnd.data["blockTrainNo"][13] > 0:
            self.trackBlock14.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock14.setStyleSheet("background-color : light grey; color: black ")

        if self.backEnd.data["blockTrainNo"][14] > 0:
            self.trackBlock15.setStyleSheet("background-color : Blue; color: white ")
        else:
            self.trackBlock15.setStyleSheet("background-color : light grey; color: black ")

        # Update Stations  
        outLbl = "Right" if (self.backEnd.csvConstants["stationSide"][0] == 1 and self.backEnd.data["direction"][9] == 0) or (self.backEnd.csvConstants["stationSide"][0] == 0 and self.backEnd.data["direction"][9] == 1) else "Left"
        self.stationSideLabel.setText("Doors Open: " + outLbl)

        outLbl1 = "Right" if (self.backEnd.csvConstants["stationSide"][1] == 1 and self.backEnd.data["direction"][14] == 0) or (self.backEnd.csvConstants["stationSide"][1] == 0 and self.backEnd.data["direction"][14] == 1) else "Left"
        self.stationSideLabel.setText("Doors Open: " + outLbl1)

        # Update Labels
        if self.backEnd.data["blockNo"] == 4:
            outTxt = "5-11" if self.backEnd.data["switchPos"] == 1 else "5-6"
            self.switchLabel.setText("Switch Pos: " + outTxt)
        self.tempLabel.setText("Temp: " + str(self.backEnd.data["temp"]) + " F")

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
        self.backEnd.data["circuitStatus"][self.backEnd.data["blockNo"]] = 1 if self.backEnd.data["circuitStatus"][self.backEnd.data["blockNo"]] == 0 else 0
        if (self.backEnd.data["circuitStatus"][self.backEnd.data["blockNo"]] == 0):
            self.circuitButton.setStyleSheet("background-color: green; color: white")
        else:
            self.circuitButton.setStyleSheet("background-color: red")

    # Handler for when Brake Failure State button is pressed
    def brokenRailButtonPressed(self):
        trackSignals.brokenRailPressedSignal.emit()
        self.backEnd.data["railStatus"][self.backEnd.data["blockNo"]] = 1 if self.backEnd.data["railStatus"][self.backEnd.data["blockNo"]] == 0 else 0
        if (self.backEnd.data["railStatus"][self.backEnd.data["blockNo"]] == 0):
            self.brokenRailButton.setStyleSheet("background-color: green; color: white")
        else:
            self.brokenRailButton.setStyleSheet("background-color: red")

def main():
    mainApp = QApplication(argv)
    UI = TrackModelMainUI()
    UI.show()
    mainApp.exec()

if (__name__ == "__main__"):
    main()