# UI for the Train Model

# QTimer for Simulation

# Imports needed for the UI
from sys import argv
from TrainModelBackEnd import *
from TrainModelSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Conversions import *

# Class for the Main UI of the Train Model
class TrainModelMainUI(QWidget):

    # Instantiating the Back End
    backEnd = backEndCalculations()

    # Fonts and Alignments to make coding easier
    timesNewRoman12 = QFont("Times New Roman", 12)
    timesNewRoman18 = QFont("Times New Roman", 18)
    timesNewRoman24 = QFont("Times New Roman", 24)
    timesNewRoman30 = QFont("Times New Roman", 30)
    timesNewRoman36 = QFont("Times New Roman", 36)
    timesNewRoman42 = QFont("Times New Roman", 42)
    alignCenter = Qt.AlignmentFlag.AlignCenter
    alignLeft = Qt.AlignmentFlag.AlignLeft
    alignRight = Qt.AlignmentFlag.AlignRight

    # Initialization of the UI
    def __init__(self):

        # SIGNAL USED FOR TEST UI
        trainSignals.updateOutputs.connect(self.updateOutputs)

        # Initializing and setting the layout of the UI
        super().__init__()
        self.setWindowTitle("Train Model")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        orientation = self.frameGeometry()
        self.move(orientation.center())

        # Real Time Clock Label and Output
        realTimeClockLabel = QLabel("Real Time Clock")
        realTimeClockLabel.setFont(self.timesNewRoman18)
        self.realTimeClockOutput = QLineEdit()
        self.realTimeClockOutput.setReadOnly(True)
        self.realTimeClockOutput.setFont(self.timesNewRoman18)
        self.realTimeClockOutput.setAlignment(self.alignCenter)
        self.realTimeClockOutput.setFixedWidth(140)

        layout.addWidget(realTimeClockLabel, 0, 0, self.alignCenter)
        layout.addWidget(self.realTimeClockOutput, 0, 1, self.alignCenter)

        # Passengers Label and Output
        passengersLabel = QLabel("Passengers")
        passengersLabel.setStyleSheet("color: purple")
        passengersLabel.setFont(self.timesNewRoman18)
        self.passengersOutput = QLineEdit()
        self.passengersOutput.setStyleSheet("background-color: purple; border: purple")
        self.passengersOutput.setReadOnly(True)
        self.passengersOutput.setFont(self.timesNewRoman18)
        self.passengersOutput.setAlignment(self.alignCenter)

        layout.addWidget(passengersLabel, 1, 0, self.alignCenter)
        layout.addWidget(self.passengersOutput, 1, 1, self.alignCenter)

        # Crew Label and Output
        crewLabel = QLabel("Crew")
        crewLabel.setStyleSheet("color: rgb(65, 105, 255)")
        crewLabel.setFont(self.timesNewRoman18)
        self.crewOutput = QLineEdit()
        self.crewOutput.setStyleSheet("background-color: rgb(65, 105, 255); border: rgb(65, 105, 255)")
        self.crewOutput.setReadOnly(True)
        self.crewOutput.setFont(self.timesNewRoman18)
        self.crewOutput.setAlignment(self.alignCenter)

        layout.addWidget(crewLabel, 2, 0, self.alignCenter)
        layout.addWidget(self.crewOutput, 2, 1, self.alignCenter)

        # Underground Label and Output
        undergroundLabel = QLabel("Underground")
        undergroundLabel.setStyleSheet("color: rgb(101, 67, 33)")
        undergroundLabel.setFont(self.timesNewRoman18)
        self.undergroundOutput = QLineEdit()
        self.undergroundOutput.setStyleSheet("background-color: rgb(101, 67, 33); border: rgb(101, 67, 33)")
        self.undergroundOutput.setReadOnly(True)
        self.undergroundOutput.setFont(self.timesNewRoman18)
        self.undergroundOutput.setAlignment(self.alignCenter)

        layout.addWidget(undergroundLabel, 3, 0, self.alignCenter)
        layout.addWidget(self.undergroundOutput, 3, 1, self.alignCenter)

        # Length Label and Output
        lengthLabel = QLabel("Length")
        lengthLabel.setStyleSheet("color: rgb(105, 105, 105)")
        lengthLabel.setFont(self.timesNewRoman12)
        self.lengthOutput = QLineEdit()
        self.lengthOutput.setStyleSheet("background-color: rgb(105, 105, 105); border: rgb(105, 105, 105)")
        self.lengthOutput.setReadOnly(True)
        self.lengthOutput.setFont(self.timesNewRoman12)
        self.lengthOutput.setAlignment(self.alignCenter)
        
        layout.addWidget(lengthLabel, 4, 0, self.alignCenter)
        layout.addWidget(self.lengthOutput, 4, 1, self.alignCenter)

        # Width Label and Output
        widthLabel = QLabel("Width")
        widthLabel.setStyleSheet("color: rgb(105, 105, 105)")
        widthLabel.setFont(self.timesNewRoman12)
        self.widthOutput = QLineEdit()
        self.widthOutput.setStyleSheet("background-color: rgb(105, 105, 105); border: rgb(105, 105, 105)")
        self.widthOutput.setReadOnly(True)
        self.widthOutput.setFont(self.timesNewRoman12)
        self.widthOutput.setAlignment(self.alignCenter)
        self.widthOutput.setText("8.69 Feet")

        layout.addWidget(widthLabel, 5, 0, self.alignCenter)
        layout.addWidget(self.widthOutput, 5, 1, self.alignCenter)

        # Height Label and Output
        heightLabel = QLabel("Height")
        heightLabel.setStyleSheet("color: rgb(105, 105, 105)")
        heightLabel.setFont(self.timesNewRoman12)
        self.heightOutput = QLineEdit()
        self.heightOutput.setStyleSheet("background-color: rgb(105, 105, 105); border: rgb(105, 105, 105)")
        self.heightOutput.setReadOnly(True)
        self.heightOutput.setFont(self.timesNewRoman12)
        self.heightOutput.setAlignment(self.alignCenter)
        self.heightOutput.setText("11.22 Feet")

        layout.addWidget(heightLabel, 6, 0, self.alignCenter)
        layout.addWidget(self.heightOutput, 6, 1, self.alignCenter)

        # Mass Label and Output
        massLabel = QLabel("Mass")
        massLabel.setStyleSheet("color: rgb(47, 79, 79)")
        massLabel.setFont(self.timesNewRoman24)
        self.massOutput = QLineEdit()
        self.massOutput.setStyleSheet("background-color: rgb(47, 79, 79); border: rgb(47, 79, 79)")
        self.massOutput.setReadOnly(True)
        self.massOutput.setFont(self.timesNewRoman24)
        self.massOutput.setAlignment(self.alignCenter)

        layout.addWidget(massLabel, 7, 0, 1, 2, self.alignCenter)
        layout.addWidget(self.massOutput, 8, 0, 1, 2, self.alignCenter)

        # Velocity Label and Output
        velocityLabel = QLabel("Velocity")
        velocityLabel.setFont(self.timesNewRoman36)
        self.velocityOutput = QLineEdit()
        self.velocityOutput.setReadOnly(True)
        self.velocityOutput.setAlignment(self.alignCenter)
        self.velocityOutput.setFont(self.timesNewRoman36)
        self.velocityOutput.setFixedWidth(280)

        layout.addWidget(velocityLabel, 0, 2, self.alignCenter)
        layout.addWidget(self.velocityOutput, 0, 3, self.alignCenter)

        # Acceleration Label and Output
        accelerationLabel = QLabel("Acceleration")
        accelerationLabel.setFont(self.timesNewRoman36)
        self.accelerationOutput = QLineEdit()
        self.accelerationOutput.setReadOnly(True)
        self.accelerationOutput.setFont(self.timesNewRoman36)
        self.accelerationOutput.setAlignment(self.alignCenter)

        layout.addWidget(accelerationLabel, 1, 2, self.alignCenter)
        layout.addWidget(self.accelerationOutput, 1, 3, self.alignCenter)

        # Power Label and Output
        powerLabel = QLabel("Power")
        powerLabel.setFont(self.timesNewRoman36)
        self.powerOutput = QLineEdit()
        self.powerOutput.setReadOnly(True)
        self.powerOutput.setFont(self.timesNewRoman36)
        self.powerOutput.setAlignment(self.alignCenter)

        layout.addWidget(powerLabel, 2, 2, self.alignCenter)
        layout.addWidget(self.powerOutput, 2, 3, self.alignCenter)

        # Station Label and Output
        stationLabel = QLabel("Station")
        stationLabel.setFont(self.timesNewRoman36)
        self.stationOutput = QLineEdit()
        self.stationOutput.setReadOnly(True)
        self.stationOutput.setFont(self.timesNewRoman36)
        self.stationOutput.setAlignment(self.alignCenter)
        self.stationOutput.setText("Shadyside")

        layout.addWidget(stationLabel, 3, 2, self.alignCenter)
        layout.addWidget(self.stationOutput, 3, 3, self.alignCenter)

        # Communication State Label and Output
        communicationsLabel = QLabel("Communication Status")
        communicationsLabel.setFont(self.timesNewRoman18)
        self.communicationsOutput = QLineEdit()
        self.communicationsOutput.setReadOnly(True)
        self.communicationsOutput.setFont(self.timesNewRoman18)
        self.communicationsOutput.setAlignment(self.alignCenter)

        layout.addWidget(communicationsLabel, 4, 2, self.alignCenter)
        layout.addWidget(self.communicationsOutput, 4, 3, self.alignCenter)

        # Engine State Label and Output
        engineLabel = QLabel("Engine Status")
        engineLabel.setFont(self.timesNewRoman18)
        self.engineOutput = QLineEdit()
        self.engineOutput.setReadOnly(True)
        self.engineOutput.setFont(self.timesNewRoman18)
        self.engineOutput.setAlignment(self.alignCenter)

        layout.addWidget(engineLabel, 5, 2, self.alignCenter)
        layout.addWidget(self.engineOutput, 5, 3, self.alignCenter)

        # Service Brake State Label and Output
        brakeLabel = QLabel("Service Brake Status")
        brakeLabel.setFont(self.timesNewRoman18)
        self.brakeOutput = QLineEdit()
        self.brakeOutput.setReadOnly(True)
        self.brakeOutput.setFont(self.timesNewRoman18)
        self.brakeOutput.setAlignment(self.alignCenter)

        layout.addWidget(brakeLabel, 6, 2, self.alignCenter)
        layout.addWidget(self.brakeOutput, 6, 3, self.alignCenter)

        # Emergency Brake State Label and Output
        emergencyBrakeStateLabel = QLabel("Emergency Brake State")
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
        serviceBrakeStateLabel = QLabel("Service Brake State")
        serviceBrakeStateLabel.setFont(self.timesNewRoman24)
        serviceBrakeStateLabel.setAlignment(self.alignCenter)
        serviceBrakeStateLabel.setWordWrap(True)
        self.serviceBrakeStateOutput = QLineEdit()
        self.serviceBrakeStateOutput.setReadOnly(True)
        self.serviceBrakeStateOutput.setFont(self.timesNewRoman24)
        self.serviceBrakeStateOutput.setAlignment(self.alignCenter)

        layout.addWidget(serviceBrakeStateLabel, 7, 3)
        layout.addWidget(self.serviceBrakeStateOutput, 8, 3)

        # Left Doors Label and Output
        lDoorsLabel = QLabel("Left Doors")
        lDoorsLabel.setFont(self.timesNewRoman18)
        self.lDoorsOutput = QLineEdit()
        self.lDoorsOutput.setReadOnly(True)
        self.lDoorsOutput.setFont(self.timesNewRoman18)
        self.lDoorsOutput.setAlignment(self.alignCenter)

        layout.addWidget(lDoorsLabel, 0, 4, self.alignCenter)
        layout.addWidget(self.lDoorsOutput, 0, 5, 1, 2, self.alignCenter)

        # Right Doors Label and Output
        rDoorsLabel = QLabel("Right Doors")
        rDoorsLabel.setFont(self.timesNewRoman18)
        self.rDoorsOutput = QLineEdit()
        self.rDoorsOutput.setReadOnly(True)
        self.rDoorsOutput.setFont(self.timesNewRoman18)
        self.rDoorsOutput.setAlignment(self.alignCenter)

        layout.addWidget(rDoorsLabel, 1, 4, self.alignCenter)
        layout.addWidget(self.rDoorsOutput, 1, 5, 1, 2, self.alignCenter)

        # Internal Lights Label and Output
        iLightsLabel = QLabel("Internal Lights")
        iLightsLabel.setFont(self.timesNewRoman18)
        self.iLightsOutput = QLineEdit()
        self.iLightsOutput.setReadOnly(True)
        self.iLightsOutput.setFont(self.timesNewRoman18)
        self.iLightsOutput.setAlignment(self.alignCenter)

        layout.addWidget(iLightsLabel, 2, 4, self.alignCenter)
        layout.addWidget(self.iLightsOutput, 2, 5, 1, 2, self.alignCenter)

        # External Lights Label and Output
        eLightsLabel = QLabel("External Lights")
        eLightsLabel.setFont(self.timesNewRoman18)
        self.eLightsOutput = QLineEdit()
        self.eLightsOutput.setReadOnly(True)
        self.eLightsOutput.setFont(self.timesNewRoman18)
        self.eLightsOutput.setAlignment(self.alignCenter)

        layout.addWidget(eLightsLabel, 3, 4, self.alignCenter)
        layout.addWidget(self.eLightsOutput, 3, 5, 1, 2, self.alignCenter)

        # Murphy Label
        murphyLabel = QLabel("Failure States")
        murphyLabel.setFont(self.timesNewRoman24)

        layout.addWidget(murphyLabel, 4, 5, self.alignCenter)

        # Communcations Label and Button
        communicationsButton = QPushButton("Lose\nCommunications")
        communicationsButton.setStyleSheet("background-color: orange")
        communicationsButton.setFont(self.timesNewRoman18)
        communicationsButton.pressed.connect(self.communicationsButtonPressed)

        layout.addWidget(communicationsButton, 5, 4)

        # Engine Label and Button
        engineButton = QPushButton("Disable\nEngine")
        engineButton.setStyleSheet("background-color: orange")
        engineButton.pressed.connect(self.engineButtonPressed)
        engineButton.setFont(self.timesNewRoman18)

        layout.addWidget(engineButton, 5, 5)

        # Service Brake Label and Button
        brakeButton = QPushButton("Disable Service\nBrakes")
        brakeButton.setStyleSheet("background-color: orange")
        brakeButton.pressed.connect(self.brakeButtonPressed)
        brakeButton.setFont(self.timesNewRoman18)

        layout.addWidget(brakeButton, 5, 6)
        
        # Emergency Brake Label and Button
        emergencyBrakeLabel = QLabel("Emergency Brake")
        emergencyBrakeLabel.setFont(self.timesNewRoman24)
        emergencyBrakeButton = QPushButton("Emergency Brake")
        emergencyBrakeButton.setStyleSheet("background-color: red")
        emergencyBrakeButton.setFixedSize(400, 100)
        emergencyBrakeButton.setFont(self.timesNewRoman24)
        emergencyBrakeButton.pressed.connect(self.emergencyBrakeButtonPressed)

        #layout.addWidget(emergencyBrakeLabel, 6, 4, 1, 2, self.alignCenter)
        layout.addWidget(emergencyBrakeButton, 6, 4, 2, 2)

        # Temperature Labels, Input, and Output
        temperatureLabel = QLabel("Temperature Setpoint (F)")
        temperatureLabel.setFont(self.timesNewRoman24)
        temperatureLabel.setWordWrap(True)
        self.temperatureInput = QLineEdit()
        self.temperatureInput.setFont(self.timesNewRoman24)
        self.temperatureInput.setAlignment(self.alignCenter)
        self.temperatureInput.editingFinished.connect(self.tempInputChanged)
        currentTemperatureLabel = QLabel("Current Temperature")
        currentTemperatureLabel.setFont(self.timesNewRoman24)
        self.currentTemperatureOutput = QLineEdit()
        self.currentTemperatureOutput.setReadOnly(True)
        self.currentTemperatureOutput.setFont(self.timesNewRoman24)
        self.currentTemperatureOutput.setAlignment(self.alignCenter)

        layout.addWidget(temperatureLabel, 6, 6, self.alignCenter)
        layout.addWidget(self.temperatureInput, 7, 6)
        layout.addWidget(currentTemperatureLabel, 8, 4, 1, 2, self.alignCenter)
        layout.addWidget(self.currentTemperatureOutput, 8, 6)

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
        self.backEnd.runFunctions()

        # Update Left Column of data outputs
        self.realTimeClockOutput.setText(str(self.backEnd.data["rtc"]))
        self.passengersOutput.setText(str(self.backEnd.data["passengers"]))
        self.crewOutput.setText(str(self.backEnd.data["crew"]))
        self.undergroundOutput.setText(str(self.backEnd.data["underground"]))
        self.lengthOutput.setText(str(metersToFeet(self.backEnd.data["length"])) + " Feet")
        self.massOutput.setText(str(kilogramsToTons(self.backEnd.data["mass"])) + " Tons")
    
        # Update Middle Column of data outputs
        self.velocityOutput.setText(str(metersPerSecondToMilesPerHour(self.backEnd.data["velocity"])) + " mph")
        self.accelerationOutput.setText(str(metersPerSecondSquaredToFeetPerSecondSquared(self.backEnd.data["acceleration"])) + " ft/s^2")
        self.powerOutput.setText(str(wattsToHorsepower(self.backEnd.data["power"])) + " hp")
        self.stationOutput.setText(self.backEnd.data["station"])

        # Setting communication status output and color
        self.communicationsOutput.setText(self.failureBoolean(self.backEnd.data["commStatus"]))
        if (self.backEnd.data["commStatus"] == 1):
            self.communicationsOutput.setStyleSheet("background-color: green; border: green")
        else:
            self.communicationsOutput.setStyleSheet("background-color: red; border: red")

        # Setting the engine status output and color
        self.engineOutput.setText(self.failureBoolean(self.backEnd.data["engineStatus"]))
        if (self.backEnd.data["engineStatus"] == 1):
            self.engineOutput.setStyleSheet("background-color: green; border: green")
        else:
            self.engineOutput.setStyleSheet("background-color: red; border: red")

        # Setting the service brake status output and color
        self.brakeOutput.setText(self.failureBoolean(self.backEnd.data["brakeStatus"]))
        if (self.backEnd.data["brakeStatus"] == 1):
            self.brakeOutput.setStyleSheet("background-color: green; border: green")
        else:
            self.brakeOutput.setStyleSheet("background-color: red; border: red")

        # Setting emergency break output and color
        self.emergencyBrakeStateOutput.setText(self.brakeState(self.backEnd.data["eBrakeState"]))
        if (self.backEnd.data["eBrakeState"] == 1):
            self.emergencyBrakeStateOutput.setStyleSheet("background-color: red; border: red")
        else:
            self.emergencyBrakeStateOutput.setStyleSheet("background-color: green; border: green")

        # Setting service break output and color
        self.serviceBrakeStateOutput.setText(self.brakeState(self.backEnd.data["sBrakeState"]))
        if (self.backEnd.data["sBrakeState"] == 1):
            self.serviceBrakeStateOutput.setStyleSheet("background-color: red; border: red")
        else:
            self.serviceBrakeStateOutput.setStyleSheet("background-color: green; border: green")

        # Setting the left door output as well as color
        self.lDoorsOutput.setText(self.doorState(self.backEnd.data["lDoors"]))
        if (self.backEnd.data["lDoors"] == 0):
            self.lDoorsOutput.setStyleSheet("color: white; background-color: black; border: black")
        else:
            self.lDoorsOutput.setStyleSheet("background-color: white")

        # Setting the right door output as well as color
        self.rDoorsOutput.setText(self.doorState(self.backEnd.data["rDoors"]))
        if (self.backEnd.data["rDoors"] == 0):
            self.rDoorsOutput.setStyleSheet("color: white; background-color: black; border: black")
        else:
            self.rDoorsOutput.setStyleSheet("background-color: white")

        # Setting internal lights output as well as color
        self.iLightsOutput.setText(self.lightState(self.backEnd.data["iLights"]))
        if (self.backEnd.data["iLights"] == 1):
            self.iLightsOutput.setStyleSheet("background-color: rgb(255, 215, 0); border: rgb(255, 215, 0)")
        else:
            self.iLightsOutput.setStyleSheet("background-color: white")

        # Setting external lights output as well as color
        self.eLightsOutput.setText(self.lightState(self.backEnd.data["eLights"]))
        if (self.backEnd.data["eLights"] == 1):
            self.eLightsOutput.setStyleSheet("background-color: rgb(255, 215, 0); border: rgb(255, 215, 0)")
        else:
            self.eLightsOutput.setStyleSheet("background-color: white")

        # Setting the temperature output as well as color
        self.currentTemperatureOutput.setText(str(self.backEnd.data["currTemp"]) + " F")
        if (self.backEnd.data["currTemp"] > 32.0):
            self.currentTemperatureOutput.setStyleSheet("background-color: rgb(220, 20, 60); border: rgb(220, 20, 60)")
        else:
            self.currentTemperatureOutput.setStyleSheet("background-color: blue; border: blue")

        # Move curr values to previous
        self.backEnd.moveToPrevious()

def main():
    app = QApplication(argv)
    UI = TrainModelMainUI()
    UI.show()
    app.exec()

if (__name__ == "__main__"):
    main()