# UI for the Train Model

# QTimer for Simulation

# TEMPERATURE INPUTS AND SIZES OF FONTS
# STATION AND TRAIN ID TO TOP, POWER AS 2 COLUMNS INSTEAD OF ONE
# REWORK SIGNALS IN THE TRAIN MODEL AS WELL AS THE MAIN
# WORK ON JSON OUTPUTS AND INPUTS FOR THIS MODULE
# ISO 8601 FORMAT FOR TIME

# Imports needed for the UI
from sys import argv
from TrainModel import TrainModel
from TrainModelSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Conversions import *

# Class for the Main UI of the Train Model
class TrainModelUI(QWidget):

    # Instantiating the Back End
    TrainModel = TrainModel()

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

        # Initializing and setting the layout of the UI
        super().__init__()
        self.TrainModel.data["id"] = id
        self.TrainModel.trackData["trainLine"] = line
        self.TrainModel.setFirstSection()
        self.setWindowTitle("Train Model " + str(TrainModel.data["id"]))
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        orientation = self.frameGeometry()
        self.move(orientation.center())

        # Real Time Clock Label and Output
        #realTimeClockLabel = QLabel("Real Time Clock")
        #realTimeClockLabel.setFont(self.timesNewRoman18)
        self.realTimeClockOutput = QLabel("")
        #self.realTimeClockOutput = QLineEdit()
        #self.realTimeClockOutput.setReadOnly(True)
        self.realTimeClockOutput.setFont(self.timesNewRoman24)
        self.realTimeClockOutput.setAlignment(self.alignCenter)
        #self.realTimeClockOutput.setFixedWidth(140)

        #layout.addWidget(realTimeClockLabel, 0, 0, self.alignCenter)
        layout.addWidget(self.realTimeClockOutput, 0, 0, 1, 2, self.alignCenter)

        # Passengers Label and Output
        passengersLabel = QLabel("Passengers")
        passengersLabel.setFont(self.timesNewRoman18)
        self.passengersOutput = QLineEdit()
        self.passengersOutput.setStyleSheet("background-color: rgb(65, 105, 255); border: rgb(65, 105, 255)")
        self.passengersOutput.setReadOnly(True)
        self.passengersOutput.setFont(self.timesNewRoman18)
        self.passengersOutput.setAlignment(self.alignCenter)
        self.passengersOutput.setFixedWidth(140)

        layout.addWidget(passengersLabel, 1, 0, self.alignCenter)
        layout.addWidget(self.passengersOutput, 2, 0, self.alignCenter)

        # Crew Label and Output
        crewLabel = QLabel("Crew")
        crewLabel.setFont(self.timesNewRoman18)
        self.crewOutput = QLineEdit()
        self.crewOutput.setStyleSheet("background-color: rgb(65, 105, 255); border: rgb(65, 105, 255)")
        self.crewOutput.setReadOnly(True)
        self.crewOutput.setFont(self.timesNewRoman18)
        self.crewOutput.setAlignment(self.alignCenter)
        self.crewOutput.setFixedWidth(140)

        layout.addWidget(crewLabel, 1, 1, self.alignCenter)
        layout.addWidget(self.crewOutput, 2, 1, self.alignCenter)

        # Left Doors Label and Output
        lDoorsLabel = QLabel("Left Doors")
        lDoorsLabel.setFont(self.timesNewRoman18)
        self.lDoorsOutput = QLineEdit()
        self.lDoorsOutput.setReadOnly(True)
        self.lDoorsOutput.setFont(self.timesNewRoman18)
        self.lDoorsOutput.setAlignment(self.alignCenter)

        layout.addWidget(lDoorsLabel, 3, 0, self.alignCenter)
        layout.addWidget(self.lDoorsOutput, 4, 0, self.alignCenter)

        # Right Doors Label and Output
        rDoorsLabel = QLabel("Right Doors")
        rDoorsLabel.setFont(self.timesNewRoman18)
        self.rDoorsOutput = QLineEdit()
        self.rDoorsOutput.setReadOnly(True)
        self.rDoorsOutput.setFont(self.timesNewRoman18)
        self.rDoorsOutput.setAlignment(self.alignCenter)

        layout.addWidget(rDoorsLabel, 3, 1, self.alignCenter)
        layout.addWidget(self.rDoorsOutput, 4, 1, self.alignCenter)

        # Internal Lights Label and Output
        iLightsLabel = QLabel("Internal Lights")
        iLightsLabel.setFont(self.timesNewRoman18)
        self.iLightsOutput = QLineEdit()
        self.iLightsOutput.setReadOnly(True)
        self.iLightsOutput.setFont(self.timesNewRoman18)
        self.iLightsOutput.setAlignment(self.alignCenter)

        layout.addWidget(iLightsLabel, 5, 0, self.alignCenter)
        layout.addWidget(self.iLightsOutput, 6, 0, self.alignCenter)

        # External Lights Label and Output
        eLightsLabel = QLabel("External Lights")
        eLightsLabel.setFont(self.timesNewRoman18)
        self.eLightsOutput = QLineEdit()
        self.eLightsOutput.setReadOnly(True)
        self.eLightsOutput.setFont(self.timesNewRoman18)
        self.eLightsOutput.setAlignment(self.alignCenter)

        layout.addWidget(eLightsLabel, 5, 1, self.alignCenter)
        layout.addWidget(self.eLightsOutput, 6, 1, self.alignCenter)

        # Mass Label and Output
        massLabel = QLabel("Mass")
        massLabel.setFont(self.timesNewRoman24)
        self.massOutput = QLineEdit()
        self.massOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.massOutput.setReadOnly(True)
        self.massOutput.setFont(self.timesNewRoman24)
        self.massOutput.setAlignment(self.alignCenter)
        self.massOutput.setFixedWidth(200)

        layout.addWidget(massLabel, 7, 0, self.alignCenter)
        layout.addWidget(self.massOutput, 8, 0, self.alignCenter)

        # Underground Label and Output
        undergroundLabel = QLabel("Underground")
        undergroundLabel.setFont(self.timesNewRoman24)
        self.undergroundOutput = QLineEdit()
        self.undergroundOutput.setReadOnly(True)
        self.undergroundOutput.setFont(self.timesNewRoman24)
        self.undergroundOutput.setAlignment(self.alignCenter)

        layout.addWidget(undergroundLabel, 7, 1, self.alignCenter)
        layout.addWidget(self.undergroundOutput, 8, 1, self.alignCenter)

        # Velocity Label and Output
        velocityLabel = QLabel("Velocity")
        velocityLabel.setFont(self.timesNewRoman18)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setAlignment(self.alignCenter)
        self.velocityOutput.setFont(self.timesNewRoman36)
        self.velocityOutput.setFixedWidth(280)

        layout.addWidget(velocityLabel, 0, 2, self.alignCenter)
        layout.addWidget(self.velocityOutput, 1, 2, self.alignCenter)

        # Acceleration Label and Output
        accelerationLabel = QLabel("Acceleration")
        accelerationLabel.setFont(self.timesNewRoman18)
        self.accelerationOutput = QLineEdit()
        self.accelerationOutput.setReadOnly(True)
        self.accelerationOutput.setFont(self.timesNewRoman36)
        self.accelerationOutput.setAlignment(self.alignCenter)
        self.accelerationOutput.setFixedWidth(250)

        layout.addWidget(accelerationLabel, 0, 3, self.alignCenter)
        layout.addWidget(self.accelerationOutput, 1, 3, self.alignCenter)

        # Power Label and Output
        powerLabel = QLabel("Power")
        powerLabel.setFont(self.timesNewRoman18)
        self.powerOutput = QLineEdit()
        self.powerOutput.setReadOnly(True)
        self.powerOutput.setFont(self.timesNewRoman36)
        self.powerOutput.setAlignment(self.alignCenter)

        layout.addWidget(powerLabel, 2, 2, self.alignCenter)
        layout.addWidget(self.powerOutput, 3, 2, self.alignCenter)

        # Station Label and Output
        stationLabel = QLabel("Station")
        stationLabel.setFont(self.timesNewRoman18)
        self.stationOutput = QLineEdit()
        self.stationOutput.setReadOnly(True)
        self.stationOutput.setFont(self.timesNewRoman36)
        self.stationOutput.setAlignment(self.alignCenter)
        self.stationOutput.setText("Shadyside")

        layout.addWidget(stationLabel, 2, 3, self.alignCenter)
        layout.addWidget(self.stationOutput, 3, 3, self.alignCenter)

        # Emergency Brake Label and Button
        #emergencyBrakeLabel = QLabel("Emergency Brake")
        #emergencyBrakeLabel.setFont(self.timesNewRoman24)
        emergencyBrakeButton = QPushButton("Pull Emergency Brake")
        emergencyBrakeButton.setStyleSheet("background-color: red")
        #emergencyBrakeButton.setFixedSize(400, 100)
        emergencyBrakeButton.setFixedHeight(100)
        emergencyBrakeButton.setFont(self.timesNewRoman24)
        emergencyBrakeButton.pressed.connect(self.emergencyBrakeButtonPressed)

        #layout.addWidget(emergencyBrakeLabel, 6, 4, 1, 2, self.alignCenter)
        layout.addWidget(emergencyBrakeButton, 5, 2, 2, 2)

        # Emergency Brake State Label and Output
        emergencyBrakeStateLabel = QLabel("Emergency Brake")
        emergencyBrakeStateLabel.setFont(self.timesNewRoman24)
        emergencyBrakeStateLabel.setAlignment(self.alignCenter)
        emergencyBrakeStateLabel.setWordWrap(True)
        self.emergencyBrakeStateOutput = QLineEdit()
        self.emergencyBrakeStateOutput.setReadOnly(True)
        self.emergencyBrakeStateOutput.setFont(self.timesNewRoman24)
        self.emergencyBrakeStateOutput.setAlignment(self.alignCenter)

        layout.addWidget(emergencyBrakeStateLabel, 7, 2)
        layout.addWidget(self.emergencyBrakeStateOutput, 8, 2)

        # Service Brake State Label and Output
        serviceBrakeStateLabel = QLabel("Service Brake")
        serviceBrakeStateLabel.setFont(self.timesNewRoman24)
        serviceBrakeStateLabel.setAlignment(self.alignCenter)
        serviceBrakeStateLabel.setWordWrap(True)
        self.serviceBrakeStateOutput = QLineEdit()
        self.serviceBrakeStateOutput.setReadOnly(True)
        self.serviceBrakeStateOutput.setFont(self.timesNewRoman24)
        self.serviceBrakeStateOutput.setAlignment(self.alignCenter)

        layout.addWidget(serviceBrakeStateLabel, 7, 3)
        layout.addWidget(self.serviceBrakeStateOutput, 8, 3)

        # Length Label and Output
        lengthLabel = QLabel("Length")
        lengthLabel.setFont(self.timesNewRoman12)
        self.lengthOutput = QLineEdit()
        self.lengthOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.lengthOutput.setReadOnly(True)
        self.lengthOutput.setFont(self.timesNewRoman18)
        self.lengthOutput.setAlignment(self.alignCenter)
        
        layout.addWidget(lengthLabel, 0, 4, self.alignCenter)
        layout.addWidget(self.lengthOutput, 1, 4, self.alignCenter)

        # Width Label and Output
        widthLabel = QLabel("Width")
        widthLabel.setFont(self.timesNewRoman12)
        self.widthOutput = QLineEdit()
        self.widthOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.widthOutput.setReadOnly(True)
        self.widthOutput.setFont(self.timesNewRoman18)
        self.widthOutput.setAlignment(self.alignCenter)
        self.widthOutput.setText("8.69 Feet")

        layout.addWidget(widthLabel, 0, 5, self.alignCenter)
        layout.addWidget(self.widthOutput, 1, 5, self.alignCenter)

        # Height Label and Output
        heightLabel = QLabel("Height")
        heightLabel.setFont(self.timesNewRoman12)
        self.heightOutput = QLineEdit()
        self.heightOutput.setStyleSheet("background-color: rgb(129, 133, 137); border: rgb(129, 133, 137)")
        self.heightOutput.setReadOnly(True)
        self.heightOutput.setFont(self.timesNewRoman18)
        self.heightOutput.setAlignment(self.alignCenter)
        self.heightOutput.setText("11.22 Feet")

        layout.addWidget(heightLabel, 0, 6, self.alignCenter)
        layout.addWidget(self.heightOutput, 1, 6, self.alignCenter)

        # Murphy Label
        murphyLabel = QLabel("Failure States")
        murphyLabel.setFont(self.timesNewRoman24)

        layout.addWidget(murphyLabel, 2, 5, self.alignCenter)

        # Communcations Label and Button
        communicationsButton = QPushButton("Lose\nCommunications")
        communicationsButton.setStyleSheet("background-color: orange")
        communicationsButton.setFont(self.timesNewRoman18)
        communicationsButton.pressed.connect(self.communicationsButtonPressed)

        layout.addWidget(communicationsButton, 3, 4)

        # Engine Label and Button
        engineButton = QPushButton("Disable\nEngine")
        engineButton.setStyleSheet("background-color: orange")
        engineButton.pressed.connect(self.engineButtonPressed)
        engineButton.setFont(self.timesNewRoman18)

        layout.addWidget(engineButton, 3, 5)

        # Service Brake Label and Button
        brakeButton = QPushButton("Disable Service\nBrakes")
        brakeButton.setStyleSheet("background-color: orange")
        brakeButton.pressed.connect(self.brakeButtonPressed)
        brakeButton.setFont(self.timesNewRoman18)

        layout.addWidget(brakeButton, 3, 6)

        # Communication State Label and Output
        communicationsLabel = QLabel("Communication Status")
        communicationsLabel.setFont(self.timesNewRoman12)
        self.communicationsOutput = QLineEdit()
        self.communicationsOutput.setReadOnly(True)
        self.communicationsOutput.setFont(self.timesNewRoman18)
        self.communicationsOutput.setAlignment(self.alignCenter)

        layout.addWidget(communicationsLabel, 5, 4, self.alignCenter)
        layout.addWidget(self.communicationsOutput, 6, 4, self.alignCenter)

        # Engine State Label and Output
        engineLabel = QLabel("Engine Status")
        engineLabel.setFont(self.timesNewRoman12)
        self.engineOutput = QLineEdit()
        self.engineOutput.setReadOnly(True)
        self.engineOutput.setFont(self.timesNewRoman18)
        self.engineOutput.setAlignment(self.alignCenter)

        layout.addWidget(engineLabel, 5, 5, self.alignCenter)
        layout.addWidget(self.engineOutput, 6, 5, self.alignCenter)

        # Service Brake State Label and Output
        brakeLabel = QLabel("Service Brake Status")
        brakeLabel.setFont(self.timesNewRoman12)
        self.brakeOutput = QLineEdit()
        self.brakeOutput.setReadOnly(True)
        self.brakeOutput.setFont(self.timesNewRoman18)
        self.brakeOutput.setAlignment(self.alignCenter)
        self.brakeOutput.setFixedWidth(170)

        layout.addWidget(brakeLabel, 5, 6, self.alignCenter)
        layout.addWidget(self.brakeOutput, 6, 6, self.alignCenter)

        # Temperature Labels, Input, and Output
        temperatureLabel = QLabel("Temperature Setpoint")
        temperatureLabel.setFont(self.timesNewRoman24)
        temperatureLabel.setWordWrap(True)
        self.temperatureInput = QLineEdit()
        self.temperatureInput.setFont(self.timesNewRoman24)
        self.temperatureInput.setAlignment(self.alignCenter)
        self.temperatureInput.editingFinished.connect(self.tempInputChanged)
        #currentTemperatureLabel = QLabel("Current Temperature")
        #currentTemperatureLabel.setFont(self.timesNewRoman24)
        self.currentTemperatureOutput = QLineEdit()
        self.currentTemperatureOutput.setReadOnly(True)
        self.currentTemperatureOutput.setFont(self.timesNewRoman24)
        self.currentTemperatureOutput.setAlignment(self.alignCenter)
        self.currentTemperatureOutput.setFixedHeight(100)

        layout.addWidget(temperatureLabel, 7, 4, 1, 2, self.alignCenter)
        layout.addWidget(self.temperatureInput, 8, 4, 1, 2)
        #layout.addWidget(currentTemperatureLabel, 8, 4, 1, 2, self.alignCenter)
        layout.addWidget(self.currentTemperatureOutput, 7, 6, 2, 1, self.alignCenter)

        self.updateOutputs()

        if __name__ == "__main__":
            # UPDATE BUTTON FOR TESTING TO BE REMOVED
            updateButton = QPushButton("Update Values")
            updateButton.setFont(self.timesNewRoman24)
            updateButton.pressed.connect(self.updateOutputs)
            layout.addWidget(updateButton, 9, 2, 1, 2, self.alignCenter)


    # Handler for when Communcations Failure State button is pressed
    def communicationsButtonPressed(self):
        trainSignals.commButtonPressedSignal.emit()
        
    # Handler for when Engine Failure State button is pressed
    def engineButtonPressed(self):
        trainSignals.engineButtonPressedSignal.emit()

    # Handler for when Brake Failure State button is pressed
    def brakeButtonPressed(self):
        trainSignals.brakeButtonPressedSignal.emit()

    # Handler for when the Emergency Brake is pulled
    def emergencyBrakeButtonPressed(self):
        trainSignals.eBrakePressedSignal.emit()
    
    # Handler for when the temperature from the user is set
    def tempInputChanged(self):
        if (self.temperatureInput.text() == ""):
            temperature = 68
        else:
            temperature = round(float(self.temperatureInput.text()) * 2) / 2
        trainSignals.tempChangedSignal.emit(temperature)

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
        
    # Updates outputs every time period
    def updateOutputs(self):

        # Run back end function updating
        self.TrainModel.runFunctions()

        # Update Left Column of data outputs
        self.realTimeClockOutput.setText(str(ISO8601ToHumanTime(self.TrainModel.data["rtc"]))[:-6])
        self.passengersOutput.setText(str(self.TrainModel.data["passengers"]))
        self.crewOutput.setText(str(self.TrainModel.data["crew"]))
        self.undergroundOutput.setText(str(self.TrainModel.data["underground"]))
        self.lengthOutput.setText(str(metersToFeet(self.TrainModel.data["length"])) + " Feet")
        self.massOutput.setText(str(kilogramsToTons(self.TrainModel.data["mass"])) + " Tons")
    
        # Update Middle Column of data outputs
        self.velocityOutput.setText(str(metersPerSecondToMilesPerHour(self.TrainModel.data["velocity"])) + " mph")
        self.accelerationOutput.setText(str(metersPerSecondSquaredToFeetPerSecondSquared(self.TrainModel.data["acceleration"])) + " ft/s^2")
        self.powerOutput.setText(str(wattsToHorsepower(self.TrainModel.data["power"])) + " hp")
        self.stationOutput.setText(self.TrainModel.data["station"])

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
            self.iLightsOutput.setStyleSheet("background-color: white")

        # Setting external lights output as well as color
        self.eLightsOutput.setText(self.lightState(self.TrainModel.data["eLights"]))
        if (self.TrainModel.data["eLights"] == 1):
            self.eLightsOutput.setStyleSheet("background-color: rgb(255, 215, 0); border: rgb(255, 215, 0)")
        else:
            self.eLightsOutput.setStyleSheet("background-color: white")

        # Setting the temperature output as well as color
        self.currentTemperatureOutput.setText(str(self.TrainModel.data["currTemp"]) + " F")
        if (self.TrainModel.data["currTemp"] > 32.0):
            self.currentTemperatureOutput.setStyleSheet("background-color: rgb(220, 20, 60); border: rgb(220, 20, 60)")
        else:
            self.currentTemperatureOutput.setStyleSheet("background-color: blue; border: blue")

        # Move curr values to previous
        self.TrainModel.moveToPrevious()

def main():
    app = QApplication(argv)
    UI = TrainModelUI(2, "Green")
    UI.show()
    app.exec()

if (__name__ == "__main__"):
    main()