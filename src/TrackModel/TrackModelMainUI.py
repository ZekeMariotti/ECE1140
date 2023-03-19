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

        self.blockNumLabel = QLabel(self.spaceString + self.spaceString + self.spaceString + self.spaceString + self.spaceString + "  ")
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
            trackBlock1.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock1.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock1, 3, 1, 1, 1)

        trackBlock2 = QPushButton("2")
        trackBlock2.setFont(self.timesNewRoman8)
        trackBlock2.pressed.connect(self.showTrackData2)
        if self.backEnd.data["blockTrainNo"][1] > 0:
            trackBlock2.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock2.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock2, 3, 2, 1, 1)

        trackBlock3 = QPushButton("3")
        trackBlock3.setFont(self.timesNewRoman8)
        trackBlock3.pressed.connect(self.showTrackData3)
        if self.backEnd.data["blockTrainNo"][2] > 0:
            trackBlock3.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock3.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock3, 3, 3, 1, 1)

        trackBlock4 = QPushButton("4")
        trackBlock4.setFont(self.timesNewRoman8)
        trackBlock4.pressed.connect(self.showTrackData4)
        if self.backEnd.data["blockTrainNo"][3] > 0:
            trackBlock4.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock4.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock4, 3, 4, 1, 1)

        trackBlock5 = QPushButton("5")
        trackBlock5.setFont(self.timesNewRoman8)
        trackBlock5.pressed.connect(self.showTrackData5)
        if self.backEnd.data["blockTrainNo"][4] > 0:
            trackBlock5.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock5.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock5, 3, 5, 1, 1)

        trackBlock6 = QPushButton("6")
        trackBlock6.setFont(self.timesNewRoman8)
        trackBlock6.pressed.connect(self.showTrackData6)
        if self.backEnd.data["blockTrainNo"][5] > 0:
            trackBlock6.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock6.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock6, 2, 6, 1, 1)

        trackBlock7 = QPushButton("7")
        trackBlock7.setFont(self.timesNewRoman8)
        trackBlock7.pressed.connect(self.showTrackData7)
        if self.backEnd.data["blockTrainNo"][6] > 0:
            trackBlock7.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock7.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock7, 2, 7, 1, 1)

        trackBlock8 = QPushButton("8")
        trackBlock8.setFont(self.timesNewRoman8)
        trackBlock8.pressed.connect(self.showTrackData8)
        if self.backEnd.data["blockTrainNo"][7] > 0:
            trackBlock8.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock8.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock8, 2, 8, 1, 1)

        trackBlock9 = QPushButton("9")
        trackBlock9.setFont(self.timesNewRoman8)
        trackBlock9.pressed.connect(self.showTrackData9)
        if self.backEnd.data["blockTrainNo"][8] > 0:
            trackBlock9.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock9.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock9, 2, 9, 1, 1)

        trackBlock10 = QPushButton("10")
        trackBlock10.setFont(self.timesNewRoman8)
        trackBlock10.pressed.connect(self.showTrackData10)
        if self.backEnd.data["blockTrainNo"][9] > 0:
            trackBlock10.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock10.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock10, 2, 10, 1, 1)

        trackBlock11 = QPushButton("11")
        trackBlock11.setFont(self.timesNewRoman8)
        trackBlock11.pressed.connect(self.showTrackData11)
        if self.backEnd.data["blockTrainNo"][10] > 0:
            trackBlock11.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock11.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock11, 4, 6, 1, 1)

        trackBlock12 = QPushButton("12")
        trackBlock12.setFont(self.timesNewRoman8)
        trackBlock12.pressed.connect(self.showTrackData12)
        if self.backEnd.data["blockTrainNo"][11] > 0:
            trackBlock12.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock12.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock12, 4, 7, 1, 1)

        trackBlock13 = QPushButton("13")
        trackBlock13.setFont(self.timesNewRoman8)
        trackBlock13.pressed.connect(self.showTrackData13)
        if self.backEnd.data["blockTrainNo"][12] > 0:
            trackBlock13.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock13.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock13, 4, 8, 1, 1)

        trackBlock14 = QPushButton("14")
        trackBlock14.setFont(self.timesNewRoman8)
        trackBlock14.pressed.connect(self.showTrackData14)
        if self.backEnd.data["blockTrainNo"][13] > 0:
            trackBlock14.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock14.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock14, 4, 9, 1, 1)

        trackBlock15 = QPushButton("15")
        trackBlock15.setFont(self.timesNewRoman8)
        trackBlock15.pressed.connect(self.showTrackData15)
        if self.backEnd.data["blockTrainNo"][14] > 0:
            trackBlock15.setStyleSheet("background-color : Blue; color: white ")
        else:
            trackBlock15.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(trackBlock15, 4, 10, 1, 1)

        stationB = QPushButton("Station B")
        stationB.setFont(self.timesNewRoman8)
        stationB.pressed.connect(self.showStationDataB)
        if self.backEnd.data["blockTrainNo"][9] > 0:
            stationB.setStyleSheet("background-color : green; color: white ")
        else:
            stationB.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(stationB, 1, 10, 1, 1)

        stationC = QPushButton("Station C")
        stationC.setFont(self.timesNewRoman8)
        stationC.pressed.connect(self.showStationDataC)
        if self.backEnd.data["blockTrainNo"][14] > 0:
            stationC.setStyleSheet("background-color : green; color: white ")
        else:
            stationC.setStyleSheet("background-color : light grey; color: black ")
        layout.addWidget(stationC, 5, 10, 1, 1)

    # Shows track block stats if track block is clicked
    def showTrackData1(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 1  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][0] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][0]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][0] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][0] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][0] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][0] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][0] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][0] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][0] - 1]) + " blocks")

    def showTrackData2(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 2  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][1] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][1]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][1] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][1] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][1] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][1] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][1] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][1] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][1] - 1]) + " blocks")

    def showTrackData3(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 3  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][2] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][2]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][2] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][2] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][2] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][2] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][2] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][2] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][2] - 1]) + " blocks")

    def showTrackData4(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 4  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][3] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][3]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][3] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][3] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][3] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][3] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][3] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][3] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][3] - 1]) + " blocks")

    def showTrackData5(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 5  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][4] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][4]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][4] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][4] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][4] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][4] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][4] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][4] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][4] - 1]) + " blocks")

    def showTrackData6(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 6  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][5] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][5]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][5] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][5] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][5] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][5] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][5] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][5] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][5] - 1]) + " blocks")

    def showTrackData7(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 7  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][6] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][6]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][6] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][6] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][6] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][6] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][6] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][6] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][6] - 1]) + " blocks")

    def showTrackData8(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 8  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][7] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][7]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][7] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][7] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][7] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][7] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][7] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][7] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][7] - 1]) + " blocks")

    def showTrackData9(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 9  ")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][8] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][8]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][8] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][8] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][8] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][8] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][8] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][8] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][8] - 1]) + " blocks")

    def showTrackData10(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString +"Block # Selected: 10")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][9] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][9]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][9] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][9] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][9] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][9] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][9] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][9] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][9] - 1]) + " blocks")

    def showTrackData11(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString +"Block # Selected: 11")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][10] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][10]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][10] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][10] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][10] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][10] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][10] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][10] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][10] - 1]) + " blocks")

    def showTrackData12(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 12")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][11] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][11]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][11] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][11] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][11] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][11] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][11] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][11] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][11] - 1]) + " blocks")

    def showTrackData13(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 13")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][12] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][12]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][12] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][12] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][12] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][12] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][12] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][12] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][12] - 1]) + " blocks")

    def showTrackData14(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 14")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][13] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][13]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][13] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][13] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][13] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][13] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][13] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][13] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][13] - 1]) + " blocks")

    def showTrackData15(self):
        self.lineLabel.setText(self.spaceString + "Line: Blue")
        self.blockNumLabel.setText(self.spaceString + "Block # Selected: 15")
        self.elevationLabel.setText(self.spaceString + "Elevation: " + str(round(self.backEnd.csvConstants["elevation"][14] * 3.28084, 1)) + " ft")
        self.gradeLabel.setText(self.spaceString + "Grade: " + str(self.backEnd.csvConstants["grade"][14]) + "%")
        self.lengthLabel.setText(self.spaceString + "Length: " + str(round(self.backEnd.csvConstants["length"][14] * 3.28084, 1)) + " ft")
        self.limitLabel.setText(self.spaceString + "Speed Limit: " + str(round(self.backEnd.csvConstants["speedLimit"][14] * 0.621371, 1)) + " MPH")
        outLbl = "Westbound" if self.backEnd.data["direction"][14] == 1 else "Eastbound"
        self.directionLabel.setText(self.spaceString + "Direction: " + outLbl)

        # Show train data if block has train
        if self.backEnd.data["blockTrainNo"][14] > 0:
            self.numPassengersLbl.setText("# of Passengers: " + str(self.backEnd.data["numPassengers"][self.backEnd.data["blockTrainNo"][14] - 1]) + " people")
            self.cSpeedLbl.setText("Commanded Speed: " + str(self.backEnd.data["commandedSpeed"][self.backEnd.data["blockTrainNo"][14] - 1]) + " MPH")
            self.authLbl.setText("Authority: " + str(self.backEnd.data["authority"][self.backEnd.data["blockTrainNo"][14] - 1]) + " blocks")

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
        if self.backEnd.data["blockTrainNo"][9] > 0:
            self.stationB.setStyleSheet("background-color : green; color: white ")
        else:
            self.stationB.setStyleSheet("background-color : light grey; color: black ")

        if self.backEnd.data["blockTrainNo"][14] > 0:
            self.stationC.setStyleSheet("background-color : green; color: white ")
        else:
            self.stationC.setStyleSheet("background-color : light grey; color: black ")
        
        outLbl = "Right" if (self.backEnd.csvConstants["stationSide"][0] == 1 and self.backEnd.data["direction"][9] == 0) or (self.backEnd.csvConstants["stationSide"][0] == 0 and self.backEnd.data["direction"][9] == 1) else "Left"
        self.stationSideLabel.setText("Doors Open: " + outLbl)

        outLbl1 = "Right" if (self.backEnd.csvConstants["stationSide"][1] == 1 and self.backEnd.data["direction"][14] == 0) or (self.backEnd.csvConstants["stationSide"][1] == 0 and self.backEnd.data["direction"][14] == 1) else "Left"
        self.stationSideLabel.setText("Doors Open: " + outLbl1)

def main():
    mainApp = QApplication(argv)
    UI = TrackModelMainUI()
    UI.show()
    mainApp.exec()

if (__name__ == "__main__"):
    main()
