# UI for the Train Model

# QTimer for Simulation

# Imports needed for the UI
from sys import argv
from TrainModelBackEnd import *
from TrainModelSignals import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

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
        # Initializing and setting the layout of the UI
        super(TrainModelMainUI, self).__init__()
        self.setWindowTitle("Train Model")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        orientation = self.frameGeometry()
        self.move(orientation.center())

        # Real Time Clock Label and Output
        realTimeClockLabel = QLabel("Real Time Clock")
        realTimeClockLabel.setFont(self.timesNewRoman18)
        realTimeClockOutput = QLineEdit()
        realTimeClockOutput.setReadOnly(True)
        realTimeClockOutput.setFont(self.timesNewRoman18)
        realTimeClockOutput.setAlignment(self.alignCenter)
        realTimeClockOutput.setText("12:23:41 pm")
        realTimeClockOutput.setFixedWidth(140)

        layout.addWidget(realTimeClockLabel, 0, 0, self.alignCenter)
        layout.addWidget(realTimeClockOutput, 0, 1, self.alignCenter)

        # Passengers Label and Output
        passengersLabel = QLabel("Passengers")
        passengersLabel.setFont(self.timesNewRoman18)
        passengersOutput = QLineEdit()
        passengersOutput.setReadOnly(True)
        passengersOutput.setFont(self.timesNewRoman18)
        passengersOutput.setAlignment(self.alignCenter)
        passengersOutput.setText("15")

        layout.addWidget(passengersLabel, 1, 0, self.alignCenter)
        layout.addWidget(passengersOutput, 1, 1, self.alignCenter)

        # Crew Label and Output
        crewLabel = QLabel("Crew")
        crewLabel.setFont(self.timesNewRoman18)
        crewOutput = QLineEdit()
        crewOutput.setReadOnly(True)
        crewOutput.setFont(self.timesNewRoman18)
        crewOutput.setAlignment(self.alignCenter)
        crewOutput.setText("2")

        layout.addWidget(crewLabel, 2, 0, self.alignCenter)
        layout.addWidget(crewOutput, 2, 1, self.alignCenter)

        # Underground Label and Output
        undergroundLabel = QLabel("Underground")
        undergroundLabel.setFont(self.timesNewRoman18)
        undergroundOutput = QLineEdit()
        undergroundOutput.setReadOnly(True)
        undergroundOutput.setFont(self.timesNewRoman18)
        undergroundOutput.setAlignment(self.alignCenter)
        undergroundOutput.setText("True")

        layout.addWidget(undergroundLabel, 3, 0, self.alignCenter)
        layout.addWidget(undergroundOutput, 3, 1, self.alignCenter)

        # Length Label and Output
        lengthLabel = QLabel("Length")
        lengthLabel.setFont(self.timesNewRoman12)
        lengthOutput = QLineEdit()
        lengthOutput.setReadOnly(True)
        lengthOutput.setFont(self.timesNewRoman12)
        lengthOutput.setAlignment(self.alignCenter)
        
        layout.addWidget(lengthLabel, 4, 0, self.alignCenter)
        layout.addWidget(lengthOutput, 4, 1, self.alignCenter)

        # Width Label and Output
        widthLabel = QLabel("Width")
        widthLabel.setFont(self.timesNewRoman12)
        widthOutput = QLineEdit()
        widthOutput.setReadOnly(True)
        widthOutput.setFont(self.timesNewRoman12)
        widthOutput.setAlignment(self.alignCenter)
        widthOutput.setText("8.69 Feet")

        layout.addWidget(widthLabel, 5, 0, self.alignCenter)
        layout.addWidget(widthOutput, 5, 1, self.alignCenter)

        # Height Label and Output
        heightLabel = QLabel("Height")
        heightLabel.setFont(self.timesNewRoman12)
        heightOutput = QLineEdit()
        heightOutput.setReadOnly(True)
        heightOutput.setFont(self.timesNewRoman12)
        heightOutput.setAlignment(self.alignCenter)
        heightOutput.setText("11.22 Feet")

        layout.addWidget(heightLabel, 6, 0, self.alignCenter)
        layout.addWidget(heightOutput, 6, 1, self.alignCenter)

        # Mass Label and Output
        massLabel = QLabel("Mass")
        massLabel.setFont(self.timesNewRoman24)
        massOutput = QLineEdit()
        massOutput.setReadOnly(True)
        massOutput.setFont(self.timesNewRoman24)
        massOutput.setAlignment(self.alignCenter)
        massOutput.setText("40 Tons")

        layout.addWidget(massLabel, 7, 0, 1, 2, self.alignCenter)
        layout.addWidget(massOutput, 8, 0, 1, 2, self.alignCenter)

        # Velocity Label and Output
        velocityLabel = QLabel("Velocity")
        velocityLabel.setFont(self.timesNewRoman36)
        velocityOutput = QLineEdit()
        velocityOutput.setReadOnly(True)
        velocityOutput.setAlignment(self.alignCenter)
        velocityOutput.setFont(self.timesNewRoman36)
        velocityOutput.setFixedWidth(280)

        layout.addWidget(velocityLabel, 0, 2, self.alignCenter)
        layout.addWidget(velocityOutput, 0, 3, self.alignCenter)

        # Acceleration Label and Output
        accelerationLabel = QLabel("Acceleration")
        accelerationLabel.setFont(self.timesNewRoman36)
        accelerationOutput = QLineEdit()
        accelerationOutput.setReadOnly(True)
        accelerationOutput.setFont(self.timesNewRoman36)
        accelerationOutput.setAlignment(self.alignCenter)

        layout.addWidget(accelerationLabel, 1, 2, self.alignCenter)
        layout.addWidget(accelerationOutput, 1, 3, self.alignCenter)

        # Power Label and Output
        powerLabel = QLabel("Power")
        powerLabel.setFont(self.timesNewRoman36)
        powerOutput = QLineEdit()
        powerOutput.setReadOnly(True)
        powerOutput.setFont(self.timesNewRoman36)
        powerOutput.setAlignment(self.alignCenter)

        layout.addWidget(powerLabel, 2, 2, self.alignCenter)
        layout.addWidget(powerOutput, 2, 3, self.alignCenter)

        # Station Label and Output
        stationLabel = QLabel("Station")
        stationLabel.setFont(self.timesNewRoman36)
        stationOutput = QLineEdit()
        stationOutput.setReadOnly(True)
        stationOutput.setFont(self.timesNewRoman36)
        stationOutput.setAlignment(self.alignCenter)
        stationOutput.setText("Shadyside")

        layout.addWidget(stationLabel, 3, 2, self.alignCenter)
        layout.addWidget(stationOutput, 3, 3, self.alignCenter)

        # Communication State Label and Output
        communicationsLabel = QLabel("Communication Status")
        communicationsLabel.setFont(self.timesNewRoman18)
        communicationsOutput = QLineEdit()
        communicationsOutput.setReadOnly(True)
        communicationsOutput.setFont(self.timesNewRoman18)
        communicationsOutput.setAlignment(self.alignCenter)
        communicationsOutput.setText("Fully Functional")

        layout.addWidget(communicationsLabel, 4, 2, self.alignCenter)
        layout.addWidget(communicationsOutput, 4, 3, self.alignCenter)

        # Engine State Label and Output
        engineLabel = QLabel("Engine Status")
        engineLabel.setFont(self.timesNewRoman18)
        engineOutput = QLineEdit()
        engineOutput.setReadOnly(True)
        engineOutput.setFont(self.timesNewRoman18)
        engineOutput.setAlignment(self.alignCenter)
        engineOutput.setText("Fully Functional")

        layout.addWidget(engineLabel, 5, 2, self.alignCenter)
        layout.addWidget(engineOutput, 5, 3, self.alignCenter)

        # Service Brake State Label and Output
        brakeLabel = QLabel("Service Brake Status")
        brakeLabel.setFont(self.timesNewRoman18)
        brakeOutput = QLineEdit()
        brakeOutput.setReadOnly(True)
        brakeOutput.setFont(self.timesNewRoman18)
        brakeOutput.setAlignment(self.alignCenter)
        brakeOutput.setText("Fully Functional")

        layout.addWidget(brakeLabel, 6, 2, self.alignCenter)
        layout.addWidget(brakeOutput, 6, 3, self.alignCenter)

        # Emergency Brake State Label and Output
        emergencyBrakeStateLabel = QLabel("Emergency Brake State")
        emergencyBrakeStateLabel.setFont(self.timesNewRoman24)
        emergencyBrakeStateLabel.setAlignment(self.alignCenter)
        emergencyBrakeStateLabel.setWordWrap(True)
        emergencyBrakeStateOutput = QLineEdit()
        emergencyBrakeStateOutput.setReadOnly(True)
        emergencyBrakeStateOutput.setFont(self.timesNewRoman24)
        emergencyBrakeStateOutput.setAlignment(self.alignCenter)
        emergencyBrakeStateOutput.setText("Disengaged")

        layout.addWidget(emergencyBrakeStateLabel, 7, 2)
        layout.addWidget(emergencyBrakeStateOutput, 8, 2)

        # Service Brake State Label and Output
        serviceBrakeStateLabel = QLabel("Service Brake State")
        serviceBrakeStateLabel.setFont(self.timesNewRoman24)
        serviceBrakeStateLabel.setAlignment(self.alignCenter)
        serviceBrakeStateLabel.setWordWrap(True)
        serviceBrakeStateOutput = QLineEdit()
        serviceBrakeStateOutput.setReadOnly(True)
        serviceBrakeStateOutput.setFont(self.timesNewRoman24)
        serviceBrakeStateOutput.setAlignment(self.alignCenter)
        serviceBrakeStateOutput.setText("Disengaged")

        layout.addWidget(serviceBrakeStateLabel, 7, 3)
        layout.addWidget(serviceBrakeStateOutput, 8, 3)

        # Left Doors Label and Output
        lDoorsLabel = QLabel("Left Doors")
        lDoorsLabel.setFont(self.timesNewRoman18)
        lDoorsOutput = QLineEdit()
        lDoorsOutput.setReadOnly(True)
        lDoorsOutput.setFont(self.timesNewRoman18)
        lDoorsOutput.setAlignment(self.alignCenter)
        lDoorsOutput.setText("Closed")

        layout.addWidget(lDoorsLabel, 0, 4, self.alignCenter)
        layout.addWidget(lDoorsOutput, 0, 5, 1, 2, self.alignCenter)

        # Right Doors Label and Output
        rDoorsLabel = QLabel("Right Doors")
        rDoorsLabel.setFont(self.timesNewRoman18)
        rDoorsOutput = QLineEdit()
        rDoorsOutput.setReadOnly(True)
        rDoorsOutput.setFont(self.timesNewRoman18)
        rDoorsOutput.setAlignment(self.alignCenter)
        rDoorsOutput.setText("Closed")

        layout.addWidget(rDoorsLabel, 1, 4, self.alignCenter)
        layout.addWidget(rDoorsOutput, 1, 5, 1, 2, self.alignCenter)

        # Internal Lights Label and Output
        iLightsLabel = QLabel("Internal Lights")
        iLightsLabel.setFont(self.timesNewRoman18)
        iLightsOutput = QLineEdit()
        iLightsOutput.setReadOnly(True)
        iLightsOutput.setFont(self.timesNewRoman18)
        iLightsOutput.setAlignment(self.alignCenter)
        iLightsOutput.setText("On")

        layout.addWidget(iLightsLabel, 2, 4, self.alignCenter)
        layout.addWidget(iLightsOutput, 2, 5, 1, 2, self.alignCenter)

        # External Lights Label and Output
        eLightsLabel = QLabel("External Lights")
        eLightsLabel.setFont(self.timesNewRoman18)
        eLightsOutput = QLineEdit()
        eLightsOutput.setReadOnly(True)
        eLightsOutput.setFont(self.timesNewRoman18)
        eLightsOutput.setAlignment(self.alignCenter)
        eLightsOutput.setText("On")

        layout.addWidget(eLightsLabel, 3, 4, self.alignCenter)
        layout.addWidget(eLightsOutput, 3, 5, 1, 2, self.alignCenter)

        # Murphy Label
        murphyLabel = QLabel("Failure States")
        murphyLabel.setFont(self.timesNewRoman24)

        layout.addWidget(murphyLabel, 4, 5, self.alignCenter)

        # Communcations Label and Button
        communicationsButton = QPushButton("Lose\nCommunications")
        communicationsButton.setFont(self.timesNewRoman18)
        communicationsButton.pressed.connect(self.communicationsButtonPressed)

        layout.addWidget(communicationsButton, 5, 4)

        # Engine Label and Button
        engineButton = QPushButton("Disable\nEngine")
        engineButton.pressed.connect(self.engineButtonPressed)
        engineButton.setFont(self.timesNewRoman18)

        layout.addWidget(engineButton, 5, 5)

        # Service Brake Label and Button
        brakeButton = QPushButton("Disable Service\nBrakes")
        brakeButton.pressed.connect(self.brakeButtonPressed)
        brakeButton.setFont(self.timesNewRoman18)

        layout.addWidget(brakeButton, 5, 6)
        
        # Emergency Brake Label and Button
        emergencyBrakeLabel = QLabel("Emergency Brake")
        emergencyBrakeLabel.setFont(self.timesNewRoman24)
        emergencyBrakeButton = QPushButton("Emergency Brake")
        emergencyBrakeButton.setFont(self.timesNewRoman24)
        emergencyBrakeButton.pressed.connect(self.emergencyBrakeButtonPressed)

        layout.addWidget(emergencyBrakeLabel, 6, 4, 1, 2, self.alignCenter)
        layout.addWidget(emergencyBrakeButton, 7, 4, 1, 2)

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
        self.currentTemperatureOutput.setText("68 F")

        layout.addWidget(temperatureLabel, 6, 6, self.alignCenter)
        layout.addWidget(self.temperatureInput, 7, 6)
        layout.addWidget(currentTemperatureLabel, 8, 4, 1, 2, self.alignCenter)
        layout.addWidget(self.currentTemperatureOutput, 8, 6)

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
        temperature = float(self.temperatureInput.text())
        trainSignals.tempChangedSignal.emit(temperature)

    # Updates outputs every time period
    def updateOutputs(self):
        self.backEnd.runFunctions()
        self.currentTemperatureOutput.setText(str(self.backEnd.data["currTemp"]) + " F")

def main():
    app = QApplication(argv)
    UI = TrainModelMainUI()
    UI.show()
    app.exec()

if (__name__ == "__main__"):
    main()