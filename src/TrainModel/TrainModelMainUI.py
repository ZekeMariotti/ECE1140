# UI for the Train Model

from sys import argv
from TrainModelBackEnd import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class TrainModelMainUI(QWidget):
    data = {}

    def __init__(self):
        # Initializing and setting the layout of the UI
        super(TrainModelMainUI, self).__init__()
        self.setWindowTitle("Train Model")
        layout = QGridLayout()
        self.setLayout(layout)
        self.setFont(QFont("Times New Roman"))
        # self.setFixedSize(QSize(720, 480))

        # Initiating the Station Overlay at the top
        stationLabel = QLabel("Station")
        stationLabel.setFont(QFont("Times New Roman", 24))
        stationOutput = QLineEdit()
        stationOutput.setReadOnly(True)
        stationOutput.setFont(QFont("Times New Roman", 24))
        stationOutput.setText("Shadyside")
        stationOutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(stationLabel, 0, 0, 2, 5, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(stationOutput, 0, 5, 2, 5, Qt.AlignmentFlag.AlignLeft)

        # Real Time Clock output
        realTimeClockLabel = QLabel("Time")
        realTimeClockOutput = QLineEdit()
        realTimeClockOutput.setReadOnly(True)
        realTimeClockOutput.setText("12:23:41")
        layout.addWidget(realTimeClockLabel, 1, 0, 3, 3, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(realTimeClockOutput, 1, 3, 3, 2, Qt.AlignmentFlag.AlignLeft)

        # Initiating main data output labels
        velocityLabel = QLabel("Velocity")
        accelerationLabel = QLabel("Acceleration")
        powerLabel = QLabel("Power")
        layout.addWidget(velocityLabel, 4, 0, 2, 3)
        layout.addWidget(accelerationLabel,6, 0, 2, 3)
        layout.addWidget(powerLabel, 8, 0, 2, 3)

        # Random Train data outputs
        passengersLabel = QLabel("Passengers")
        crewLabel = QLabel("Crew")
        undergroundLabel = QLabel("Underground")
        layout.addWidget(passengersLabel, 10, 0)
        layout.addWidget(crewLabel, 11, 0)
        layout.addWidget(undergroundLabel, 12, 0)

        # Train Informtation outputs
        lengthLabel = QLabel("Length")
        widthLabel = QLabel("Width")
        heightLabel = QLabel("Height")
        massLabel = QLabel("Mass")

        # Addings Lights and Doors States
        lDoorsLabel = QLabel("Left Doors")
        lDoorsOutput = QLineEdit()
        lDoorsOutput.setReadOnly(True)
        rDoorsLabel = QLabel("Right Doors")
        rDoorsOutput = QLineEdit()
        rDoorsOutput.setReadOnly(True)
        iLightsLabel = QLabel("Internal Lights")
        iLightsOutput = QLineEdit()
        iLightsOutput.setReadOnly(True)
        eLightsLabel = QLabel("External Lights")
        eLightsOutput = QLineEdit()
        eLightsOutput.setReadOnly(True)
        layout.addWidget(lDoorsLabel, 2, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(lDoorsOutput, 2, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(rDoorsLabel, 3, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(rDoorsOutput, 3, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iLightsLabel, 4, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iLightsOutput, 4, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(eLightsLabel, 5, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(eLightsOutput, 5, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Initializing service states
        communicationsLabel = QLabel("Communication Status")
        engineLabel = QLabel("Engine Status")
        brakeLabel = QLabel("Brake Status")
        layout.addWidget(communicationsLabel, 7, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(engineLabel, 8, 7, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(brakeLabel, 9, 7, Qt.AlignmentFlag.AlignCenter)

        # Adding Murphy Break State Buttons
        murphyLabel = QLabel("Failure States")
        communicationsButton = QPushButton("Lose Communications")
        engineButton = QPushButton("Disable Engine")
        brakeButton = QPushButton("Disable Service Brakes")
        layout.addWidget(murphyLabel, 10, 6, 1, 4, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(communicationsButton, 11, 6)
        layout.addWidget(engineButton, 11, 7, 1, 2)
        layout.addWidget(brakeButton, 11, 9)
        
        # Add Passenger Inputs : Emergency Brake and Temperature
        emergencyBrakeLabel = QLabel("Emergency Brake")
        temperatureLabel = QLabel("Temperature")
        emergencyBrakeButton = QPushButton("Emergency Brake")
        temperatureInput = QLineEdit()
        currentTemperatureLabel = QLabel("Current Temperature")
        currentTemperatureOutput = QLineEdit()
        currentTemperatureOutput.setReadOnly(True)
        layout.addWidget(emergencyBrakeLabel, 12, 6, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(temperatureLabel, 12, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(emergencyBrakeButton, 13, 6, 1, 2)
        layout.addWidget(temperatureInput, 13, 8, 1, 2)
        layout.addWidget(currentTemperatureLabel, 14, 6, 1, 2, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(currentTemperatureOutput, 14, 8, 1, 2)

def main():
    app = QApplication(argv)
    UI = TrainModelMainUI()
    UI.show()
    app.exec()

if (__name__ == "__main__"):
    main()