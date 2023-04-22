# UI for the Train Model

# UI Layout

# Sections are in Roman Numerals
######################################
#                 I                  #
######################################
#       II        #       III        #
######################################
#    IV     #     V     #     VI     #
######################################
#   VII     #   VIII    #     IX     #
######################################

# Imports needed for the UI
from sys import argv

import sys
sys.path.append(__file__.replace("\TrainModelFolder\TrainModelMainUI.py", ""))

from TrainModelFolder.TrainModel import TrainModel
from TrainModelFolder.TrainModelSignals import *
from Integration.TMTkMSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Integration.Conversions import *

# Class for the Main UI of the Train Model
class TrainModelUI(QWidget):

    # Instantiating the Back End
    UIId = 0

    # Fonts and Alignments to make coding easier
    timesNewRoman12 = QFont("Times New Roman", 12)
    timesNewRoman18 = QFont("Times New Roman", 18)
    timesNewRoman24 = QFont("Times New Roman", 24)
    timesNewRoman30 = QFont("Times New Roman", 30)
    timesNewRoman36 = QFont("Times New Roman", 36)
    timesNewRoman42 = QFont("Times New Roman", 42)
    alignCenter     = Qt.AlignmentFlag.AlignCenter
    alignLeft       = Qt.AlignmentFlag.AlignLeft
    alignRight      = Qt.AlignmentFlag.AlignRight

    # Initialization of the UI
    def __init__(self, id, line):
        
        # SIGNAL USED FOR TEST UI
        trainSignals.updateOutputs.connect(self.updateOutputs)
        self.TrainModel = TrainModel(id, line)

        # Initializing and setting the layout of the UI
        super().__init__()
        self.mainTimer = self.mainTimerSetup()
        self.UIId = id
        self.TrainModel.setFirstSection()
        self.setWindowTitle("Train Model " + str(self.UIId))
        self.setFixedSize(QSize(750, 550))
        self.setMinimumSize(850, 600)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        orientation = self.frameGeometry()
        self.move(orientation.center())

        #####################
        # Section I Widgets #
        #####################

        # Real Time Clock Label and Output
        self.realTimeClockOutput = QLabel("12:25:19")
        self.realTimeClockOutput.setFont(self.timesNewRoman30)
        self.realTimeClockOutput.setAlignment(self.alignCenter)
    
        layout.addWidget(self.realTimeClockOutput, 0, 0, 1, 3, self.alignCenter)

        # Station Label and Output
        self.stationLabel = QLabel("Station:")
        self.stationLabel.setFont(self.timesNewRoman18)
        self.stationLabel.setAlignment(self.alignCenter)
        self.stationLabel.setFixedWidth(150)
        self.stationOutput = QLineEdit()
        self.stationOutput.setReadOnly(True)
        self.stationOutput.setFont(self.timesNewRoman24)
        self.stationOutput.setAlignment(self.alignCenter)
        self.stationOutput.setText("Shadyside")
        self.stationOutput.setFixedHeight(40)

        layout.addWidget(self.stationLabel, 0, 5, 1, 1, self.alignCenter)
        layout.addWidget(self.stationOutput, 0, 6, 1, 2, self.alignCenter)

        # SPLITTING ROW 1
        splittingRow1 = QLabel("")
        splittingRow1.setFixedHeight(20)
        layout.addWidget(splittingRow1, 1, 0)

        ######################
        # Section II Widgets #
        ######################

        # Velocity Label and Output
        velocityLabel = QLabel("Velocity:")
        velocityLabel.setFont(self.timesNewRoman18)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setAlignment(self.alignCenter)
        self.velocityOutput.setFont(self.timesNewRoman30)

        layout.addWidget(velocityLabel, 2, 0, self.alignCenter)
        layout.addWidget(self.velocityOutput, 2, 1, 1, 3, self.alignCenter)

        # Acceleration Label and Output
        accelerationLabel = QLabel("Acceleration:")
        accelerationLabel.setFont(self.timesNewRoman18)
        self.accelerationOutput = QLineEdit()
        self.accelerationOutput.setReadOnly(True)
        self.accelerationOutput.setFont(self.timesNewRoman30)
        self.accelerationOutput.setAlignment(self.alignCenter)

        layout.addWidget(accelerationLabel, 3, 0, self.alignCenter)
        layout.addWidget(self.accelerationOutput, 3, 1, 1, 3, self.alignCenter)
        
        # Power Label and Output
        powerLabel = QLabel("Power:")
        powerLabel.setFont(self.timesNewRoman18)
        self.powerOutput = QLineEdit()
        self.powerOutput.setReadOnly(True)
        self.powerOutput.setFont(self.timesNewRoman30)
        self.powerOutput.setAlignment(self.alignCenter)

        layout.addWidget(powerLabel, 4, 0, self.alignCenter)
        layout.addWidget(self.powerOutput, 4, 1, 1, 3, self.alignCenter)

        # SPLITTING COLUMN 1
        splittingColumn1 = QLabel("")
        splittingColumn1.setFixedWidth(20)
        layout.addWidget(splittingColumn1, 0, 4)

        #######################
        # Section III Widgets #
        #######################

        # Communcations Label and Button
        communicationsButton = QPushButton("Signal Pickup\nFailure")
        communicationsButton.setStyleSheet("background-color: orange")
        communicationsButton.setFont(self.timesNewRoman18)
        communicationsButton.pressed.connect(self.communicationsButtonPressed)

        layout.addWidget(communicationsButton, 2, 5)

        # Engine Label and Button
        engineButton = QPushButton("Engine\nFailure")
        engineButton.setStyleSheet("background-color: orange")
        engineButton.pressed.connect(self.engineButtonPressed)
        engineButton.setFont(self.timesNewRoman18)

        layout.addWidget(engineButton, 2, 6)

        # Service Brake Label and Button
        brakeButton = QPushButton("Service Brake\nFailure")
        brakeButton.setStyleSheet("background-color: orange")
        brakeButton.pressed.connect(self.brakeButtonPressed)
        brakeButton.setFont(self.timesNewRoman18)

        layout.addWidget(brakeButton, 2, 7)

        # Communication State Label and Output
        communicationsLabel = QLabel("Signal Pickup\nStatus")
        communicationsLabel.setFont(self.timesNewRoman12)
        communicationsLabel.setAlignment(self.alignCenter)
        self.communicationsOutput = QLabel()
        self.communicationsOutput.setFixedSize(120, 55)
        self.communicationsOutput.setFont(self.timesNewRoman18)
        self.communicationsOutput.setAlignment(self.alignCenter)
        self.communicationsOutput.setWordWrap(True)

        layout.addWidget(communicationsLabel, 3, 5, self.alignCenter)
        layout.addWidget(self.communicationsOutput, 4, 5, self.alignCenter)

        # Engine State Label and Output
        engineLabel = QLabel("Engine Status")
        engineLabel.setFont(self.timesNewRoman12)
        engineLabel.setAlignment(self.alignCenter)
        self.engineOutput = QLabel()
        self.engineOutput.setFixedSize(120, 55)
        self.engineOutput.setFont(self.timesNewRoman18)
        self.engineOutput.setAlignment(self.alignCenter)
        self.engineOutput.setWordWrap(True)

        layout.addWidget(engineLabel, 3, 6, self.alignCenter)
        layout.addWidget(self.engineOutput, 4, 6, self.alignCenter)

        # Service Brake State Label and Output
        brakeLabel = QLabel("Service Brake\nStatus")
        brakeLabel.setFont(self.timesNewRoman12)
        brakeLabel.setAlignment(self.alignCenter)
        self.brakeOutput = QLabel()
        self.brakeOutput.setFixedSize(120, 55)
        self.brakeOutput.setFont(self.timesNewRoman18)
        self.brakeOutput.setAlignment(self.alignCenter)
        self.brakeOutput.setWordWrap(True)

        layout.addWidget(brakeLabel, 3, 7, self.alignCenter)
        layout.addWidget(self.brakeOutput, 4, 7, self.alignCenter)
        
        # SPLITTING ROW 2
        splittingRow2 = QLabel("")
        splittingRow2.setFixedHeight(20)
        layout.addWidget(splittingRow2, 5, 0)

        ######################
        # Section IV Widgets #
        ######################

        # Left Doors Label and Output
        lDoorsLabel = QLabel("Left Doors:")
        lDoorsLabel.setFont(self.timesNewRoman18)
        self.lDoorsOutput = QLineEdit()
        self.lDoorsOutput.setReadOnly(True)
        self.lDoorsOutput.setFont(self.timesNewRoman18)
        self.lDoorsOutput.setAlignment(self.alignCenter)
        self.lDoorsOutput.setFixedSize(120, 25)

        layout.addWidget(lDoorsLabel, 6, 0, self.alignCenter)
        layout.addWidget(self.lDoorsOutput, 6, 1, self.alignCenter)

        # Right Doors Label and Output
        rDoorsLabel = QLabel("Right Doors:")
        rDoorsLabel.setFont(self.timesNewRoman18)
        self.rDoorsOutput = QLineEdit()
        self.rDoorsOutput.setReadOnly(True)
        self.rDoorsOutput.setFont(self.timesNewRoman18)
        self.rDoorsOutput.setAlignment(self.alignCenter)
        self.rDoorsOutput.setFixedSize(120, 25)

        layout.addWidget(rDoorsLabel, 7, 0, self.alignCenter)
        layout.addWidget(self.rDoorsOutput, 7, 1, self.alignCenter)

        # Internal Lights Label and Output
        iLightsLabel = QLabel("Internal Lights:")
        iLightsLabel.setFont(self.timesNewRoman18)
        self.iLightsOutput = QLabel()
        self.iLightsOutput.setFont(self.timesNewRoman18)
        self.iLightsOutput.setAlignment(self.alignCenter)
        self.iLightsOutput.setFixedSize(120, 25)

        layout.addWidget(iLightsLabel, 8, 0, self.alignCenter)
        layout.addWidget(self.iLightsOutput, 8, 1, self.alignCenter)

        # External Lights Label and Output
        eLightsLabel = QLabel("External Lights:")
        eLightsLabel.setFont(self.timesNewRoman18)
        self.eLightsOutput = QLabel()
        self.eLightsOutput.setFont(self.timesNewRoman18)
        self.eLightsOutput.setAlignment(self.alignCenter)
        self.eLightsOutput.setFixedSize(120, 25)

        layout.addWidget(eLightsLabel, 9, 0, self.alignCenter)
        layout.addWidget(self.eLightsOutput, 9, 1, self.alignCenter)

        # SPLITTING COLUMN 2
        splittingColumn2 = QLabel("")
        splittingColumn2.setFixedWidth(20)
        layout.addWidget(splittingColumn2, 0, 2)

        #####################
        # Section V Widgets #
        #####################

        # Emergency Brake State Label and Output
        emergencyBrakeStateLabel = QLabel("Emergency Brake:")
        emergencyBrakeStateLabel.setFont(self.timesNewRoman18)
        emergencyBrakeStateLabel.setAlignment(self.alignCenter)
        emergencyBrakeStateLabel.setWordWrap(True)
        self.emergencyBrakeStateOutput = QLineEdit()
        self.emergencyBrakeStateOutput.setReadOnly(True)
        self.emergencyBrakeStateOutput.setFont(self.timesNewRoman18)
        self.emergencyBrakeStateOutput.setAlignment(self.alignCenter)

        layout.addWidget(emergencyBrakeStateLabel, 6, 3, 1, 3)
        layout.addWidget(self.emergencyBrakeStateOutput, 7, 3, 1, 3)

        # Service Brake State Label and Output
        serviceBrakeStateLabel = QLabel("Service Brake:")
        serviceBrakeStateLabel.setFont(self.timesNewRoman18)
        serviceBrakeStateLabel.setAlignment(self.alignCenter)
        serviceBrakeStateLabel.setWordWrap(True)
        self.serviceBrakeStateOutput = QLineEdit()
        self.serviceBrakeStateOutput.setReadOnly(True)
        self.serviceBrakeStateOutput.setFont(self.timesNewRoman18)
        self.serviceBrakeStateOutput.setAlignment(self.alignCenter)

        layout.addWidget(serviceBrakeStateLabel, 8, 3, 1, 3)
        layout.addWidget(self.serviceBrakeStateOutput, 9, 3, 1, 3)

        ######################
        # Section VI Widgets #
        ######################

        # Mass Label and Output
        massLabel = QLabel("Mass:")
        massLabel.setFont(self.timesNewRoman12)
        self.massOutput = QLineEdit()
        self.massOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.massOutput.setReadOnly(True)
        self.massOutput.setFont(self.timesNewRoman18)
        self.massOutput.setAlignment(self.alignCenter)

        layout.addWidget(massLabel, 6, 6, self.alignCenter)
        layout.addWidget(self.massOutput, 6, 7, self.alignCenter)

        # Length Label and Output
        lengthLabel = QLabel("Length:")
        lengthLabel.setFont(self.timesNewRoman12)
        self.lengthOutput = QLineEdit()
        self.lengthOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.lengthOutput.setReadOnly(True)
        self.lengthOutput.setFont(self.timesNewRoman18)
        self.lengthOutput.setAlignment(self.alignCenter)

        
        layout.addWidget(lengthLabel, 7, 6, self.alignCenter)
        layout.addWidget(self.lengthOutput, 7, 7, self.alignCenter)

        # Width Label and Output
        widthLabel = QLabel("Width:")
        widthLabel.setFont(self.timesNewRoman12)
        self.widthOutput = QLineEdit()
        self.widthOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.widthOutput.setReadOnly(True)
        self.widthOutput.setFont(self.timesNewRoman18)
        self.widthOutput.setAlignment(self.alignCenter)
        self.widthOutput.setText("8.69 Feet")

        layout.addWidget(widthLabel, 8, 6, self.alignCenter)
        layout.addWidget(self.widthOutput, 8, 7, self.alignCenter)

        # Height Label and Output
        heightLabel = QLabel("Height:")
        heightLabel.setFont(self.timesNewRoman12)
        self.heightOutput = QLineEdit()
        self.heightOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.heightOutput.setReadOnly(True)
        self.heightOutput.setFont(self.timesNewRoman18)
        self.heightOutput.setAlignment(self.alignCenter)
        self.heightOutput.setText("11.22 Feet")

        layout.addWidget(heightLabel, 9, 6, self.alignCenter)
        layout.addWidget(self.heightOutput, 9, 7, self.alignCenter)

        # SPLITTING ROW 3
        splittingRow3 = QLabel("")
        splittingRow3.setFixedHeight(20)
        layout.addWidget(splittingRow3, 10, 0)

        #######################
        # Section VII Widgets #
        #######################

        # Temperature Labels, Input, and Output
        temperatureLabel = QLabel("Temperature Setpoint:")
        temperatureLabel.setFont(self.timesNewRoman18)
        temperatureLabel.setWordWrap(True)
        self.temperatureInput = QLineEdit()
        self.temperatureInput.setFont(self.timesNewRoman18)
        self.temperatureInput.setAlignment(self.alignCenter)
        self.temperatureInput.editingFinished.connect(self.tempInputChanged)
        self.currentTemperatureOutput = QLineEdit()
        self.currentTemperatureOutput.setReadOnly(True)
        self.currentTemperatureOutput.setFont(self.timesNewRoman24)
        self.currentTemperatureOutput.setAlignment(self.alignCenter)

        layout.addWidget(temperatureLabel, 11, 0, 1, 2, self.alignCenter)
        layout.addWidget(self.temperatureInput, 12, 0, 1, 2)
        layout.addWidget(self.currentTemperatureOutput, 13, 0, 1, 2, self.alignCenter)

        ########################
        # Section VIII Widgets #
        ########################

        # Emergency Brake Label and Button
        emergencyBrakeButton = QPushButton("Pull Emergency Brake")
        emergencyBrakeButton.setStyleSheet("background-color: red")
        emergencyBrakeButton.setFixedHeight(120)
        emergencyBrakeButton.setFont(self.timesNewRoman18)
        emergencyBrakeButton.pressed.connect(self.emergencyBrakeButtonPressed)

        layout.addWidget(emergencyBrakeButton, 11, 3, 3, 3)

        ######################
        # Section IX Widgets #
        ######################

        # Underground Label and Output
        undergroundLabel = QLabel("Underground:")
        undergroundLabel.setFont(self.timesNewRoman12)
        self.undergroundOutput = QLineEdit()
        self.undergroundOutput.setReadOnly(True)
        self.undergroundOutput.setFont(self.timesNewRoman18)
        self.undergroundOutput.setAlignment(self.alignCenter)

        layout.addWidget(undergroundLabel, 11, 6, self.alignCenter)
        layout.addWidget(self.undergroundOutput, 11, 7, self.alignCenter)

        # Passengers Label and Output
        passengersLabel = QLabel("Passengers:")
        passengersLabel.setFont(self.timesNewRoman12)
        self.passengersOutput = QLineEdit()
        self.passengersOutput.setStyleSheet("background-color: rgb(65, 105, 255); border: rgb(65, 105, 255)")
        self.passengersOutput.setReadOnly(True)
        self.passengersOutput.setFont(self.timesNewRoman18)
        self.passengersOutput.setAlignment(self.alignCenter)

        layout.addWidget(passengersLabel, 12, 6, self.alignCenter)
        layout.addWidget(self.passengersOutput, 12, 7, self.alignCenter)

        # Crew Label and Output
        crewLabel = QLabel("Crew:")
        crewLabel.setFont(self.timesNewRoman12)
        self.crewOutput = QLineEdit()
        self.crewOutput.setStyleSheet("background-color: rgb(65, 105, 255); border: rgb(65, 105, 255)")
        self.crewOutput.setReadOnly(True)
        self.crewOutput.setFont(self.timesNewRoman18)
        self.crewOutput.setAlignment(self.alignCenter)

        layout.addWidget(crewLabel, 13, 6, self.alignCenter)
        layout.addWidget(self.crewOutput, 13, 7, self.alignCenter)

        self.updateOutputs()

    def closeEvent(self, event):
        if __name__ == "__main__":
            self.close()
        else:
            self.setVisible(False)

    # Handler for when Communcations Failure State button is pressed
    def communicationsButtonPressed(self):
        trainSignals.commButtonPressedSignal.emit(self.UIId)
        
    # Handler for when Engine Failure State button is pressed
    def engineButtonPressed(self):
        trainSignals.engineButtonPressedSignal.emit(self.UIId)

    # Handler for when Brake Failure State button is pressed
    def brakeButtonPressed(self):
        trainSignals.brakeButtonPressedSignal.emit(self.UIId)

    # Handler for when the Emergency Brake is pulled
    def emergencyBrakeButtonPressed(self):
        trainSignals.eBrakePressedSignal.emit(self.UIId)
    
    # Handler for when the temperature from the user is set
    def tempInputChanged(self):
        if (self.temperatureInput.text() == ""):
            tempNum = 68
        else:
            try:
                tempNum = round(float(self.temperatureInput.text()) * 2) / 2
            except ValueError:
                tempNum = 68.0
        trainSignals.tempChangedSignal.emit(self.UIId, tempNum)

    # Function to convert boolean to string for the status messages of failure
    def failureBoolean(self, value):
        if (value == True):
            return "Fully Functional"
        else:
            return "FAILURE"
        
    # Function to convert boolean to status of a brake
    def brakeState(self, value):
        if (value == True):
            return "ENGAGED"
        else:
            return "Disengaged"
        
    # Function to convert boolean to status of doors
    def doorState(self, value):
        if (value == True):
            return "OPEN"
        else:
            return "Closed"

    # Function to convert boolean to status of lights
    def lightState(self, value):
        if (value == True):
            return "ON"
        else:
            return "Off"

    def mainThreadSetup(self):
        self.timerThread = QThread()
        self.timerThread.started.connect(self.mainTimerSetup)

    def mainTimerSetup(self):     
        mainTimer = QTimer()
        mainTimer.setInterval(100)
        mainTimer.timeout.connect(self.updateOutputs)
        mainTimer.setParent(self)
        mainTimer.start()
        return mainTimer

    # Updates outputs every time period
    def updateOutputs(self):

        # Run back end function updating
        tempTimeDiff = self.TrainModel.findTimeDifference()
        if (tempTimeDiff != 0):
            self.TrainModel.failureStates()
            self.TrainModel.brakeCaclulator()
            self.TrainModel.findCurrentAcceleration(tempTimeDiff)
            self.TrainModel.findCurrentVelocity(tempTimeDiff)
            self.TrainModel.findCurrentDistance(tempTimeDiff)
            self.TrainModel.findBlockExiting()
            self.TrainModel.airConditioningControl(tempTimeDiff)
            if (~self.TrainModel.data["runOnce"]) & (self.TrainModel.data["atStation"]) & (self.TrainModel.data["velocity"] == 0) & (self.TrainModel.data["lDoors"] | self.TrainModel.data["rDoors"]):
                self.TrainModel.passengersGettingOff()
                TMTkMSignals.passengersExitingSignal.emit(self.TrainModel.TrainID, self.TrainModel.data["passengersOff"])
                self.TrainModel.data["passengersOff"] = 0
            if (~self.TrainModel.data["atStation"]) & (self.TrainModel.data["velocity"] != 0):
                self.TrainModel.data["runOnce"] = False
            self.TrainModel.findCurrentMass()
            if tempTimeDiff != 0:
                self.TrainModel.moveToPrevious()
            self.TrainModel.writeTMtoTkM()
            self.TrainModel.writeTMtoTC()

            # Update Left Column of data outputs
            #-21 to -13
            self.realTimeClockOutput.setText(str(ISO8601ToHumanTime(self.TrainModel.data["rtc"]))[-21:-13])
            self.passengersOutput.setText(str(self.TrainModel.data["passengers"]))
            self.crewOutput.setText(str(self.TrainModel.data["crew"]))
            self.undergroundOutput.setText(str(self.TrainModel.data["underground"]))
            self.lengthOutput.setText(str(metersToFeet(self.TrainModel.data["length"])) + " Feet")
            self.massOutput.setText(str(kilogramsToTons(self.TrainModel.data["mass"])) + " Tons")
        
            # Update Middle Column of data outputs
            self.velocityOutput.setText(str(metersPerSecondToMilesPerHour(self.TrainModel.data["velocity"])) + " mph")
            self.accelerationOutput.setText(str(metersPerSecondSquaredToFeetPerSecondSquared(self.TrainModel.data["acceleration"])) + " ft/s^2")
            self.powerOutput.setText(str(round(self.TrainModel.data["power"], 2)) + " W")
            if (self.TrainModel.data["atStation"]):
                self.stationLabel.setText("Current Station:")
                self.stationLabel.setAlignment(self.alignCenter)
                self.stationOutput.setText(self.TrainModel.data["station"])
                self.stationOutput.setStyleSheet("background-color: yellow; border: yellow")

            else:
                self.stationLabel.setText("Next Station:")
                self.stationLabel.setAlignment(self.alignCenter)
                self.stationOutput.setText(self.TrainModel.data["station"])
                self.stationOutput.setStyleSheet("background-color: white")

            # Setting communication status output and color
            self.communicationsOutput.setText(self.failureBoolean(self.TrainModel.data["commStatus"]))
            if (self.TrainModel.data["commStatus"] == 1):
                self.communicationsOutput.setStyleSheet("background-color: green; border: green")
            else:
                self.communicationsOutput.setStyleSheet("background-color: red; border: red")

            # Setting the engine status output and color
            self.engineOutput.setText(self.failureBoolean(self.TrainModel.data["engineStatus"]))
            if (self.TrainModel.data["engineStatus"] == 1):
                self.engineOutput.setStyleSheet("background-color: green; border: green")
            else:
                self.engineOutput.setStyleSheet("background-color: red; border: red")

            # Setting the service brake status output and color
            self.brakeOutput.setText(self.failureBoolean(self.TrainModel.data["brakeStatus"]))
            if (self.TrainModel.data["brakeStatus"] == 1):
                self.brakeOutput.setStyleSheet("background-color: green; border: green")
            else:
                self.brakeOutput.setStyleSheet("background-color: red; border: red")

            # Setting emergency break output and color
            self.emergencyBrakeStateOutput.setText(self.brakeState(self.TrainModel.data["eBrakeState"]))
            if (self.TrainModel.data["eBrakeState"] == 1):
                self.emergencyBrakeStateOutput.setStyleSheet("background-color: red; border: red")
            else:
                self.emergencyBrakeStateOutput.setStyleSheet("background-color: green; border: green")

            # Setting service break output and color
            self.serviceBrakeStateOutput.setText(self.brakeState(self.TrainModel.data["sBrakeState"]))
            if (self.TrainModel.data["sBrakeState"] == 1):
                self.serviceBrakeStateOutput.setStyleSheet("background-color: red; border: red")
            else:
                self.serviceBrakeStateOutput.setStyleSheet("background-color: green; border: green")

            # Setting the left door output as well as color
            self.lDoorsOutput.setText(self.doorState(self.TrainModel.data["lDoors"]))
            if (self.TrainModel.data["lDoors"] == 0):
                self.lDoorsOutput.setStyleSheet("color: white; background-color: black; border: black")
            else:
                self.lDoorsOutput.setStyleSheet("background-color: white")

            # Setting the right door output as well as color
            self.rDoorsOutput.setText(self.doorState(self.TrainModel.data["rDoors"]))
            if (self.TrainModel.data["rDoors"] == 0):
                self.rDoorsOutput.setStyleSheet("color: white; background-color: black; border: black")
            else:
                self.rDoorsOutput.setStyleSheet("background-color: white")

            # Setting internal lights output as well as color
            self.iLightsOutput.setText(self.lightState(self.TrainModel.data["iLights"]))
            if (self.TrainModel.data["iLights"] == 1):
                self.iLightsOutput.setStyleSheet("background-color: rgb(255, 215, 0); border: rgb(255, 215, 0)")
            else:
                self.iLightsOutput.setStyleSheet("color: white; background-color: black; border: black")

            # Setting external lights output as well as color
            self.eLightsOutput.setText(self.lightState(self.TrainModel.data["eLights"]))
            if (self.TrainModel.data["eLights"] == 1):
                self.eLightsOutput.setStyleSheet("background-color: rgb(255, 215, 0); border: rgb(255, 215, 0)")
            else:
                self.eLightsOutput.setStyleSheet("color: white; background-color: black; border: black")

            # Setting the temperature output as well as color
            self.currentTemperatureOutput.setText(str(round(self.TrainModel.data["currTemp"], 1)) + " F")
            if (self.TrainModel.data["currTemp"] > 32.0):
                self.currentTemperatureOutput.setStyleSheet("background-color: rgb(220, 20, 60); border: rgb(220, 20, 60)")
            else:
                self.currentTemperatureOutput.setStyleSheet("background-color: blue; border: blue")

            # Move curr values to previous
            self.TrainModel.moveToPrevious()

def main():
    app = QApplication(argv)
    UI = TrainModelUI(2, "Red")
    UI.show()
    #UI2 = TrainModelUI(3, "Green")
    #UI2.show()
    app.exec()

if (__name__ == "__main__"):
    main()