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
        #self.setFixedSize(QSize(720, 480))

        # Initiating the Station Overlay at the top
        stationLabel = QLabel("Station")
        layout.addWidget(stationLabel, 0, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        self.stationOutput = QLineEdit()
        self.stationOutput.setReadOnly(True)
        self.stationOutput.setText("Shadyside")
        self.stationOutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.stationOutput, 0, 3, 1, 2, Qt.AlignmentFlag.AlignCenter)

        # Initiating main data output labels
        velocityLabel = QLabel("Velocity")
        accelerationLabel = QLabel("Acceleration")
        powerLabel = QLabel("Power")
        layout.addWidget(velocityLabel, 1, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(accelerationLabel, 2, 0, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(powerLabel, 3, 0, Qt.AlignmentFlag.AlignCenter)

        # Initializing service states
        communicationsLabel = QLabel("Communication Status")
        engineLabel = QLabel("Engine Status")
        brakeLabel = QLabel("Brake Status")
        layout.addWidget(communicationsLabel, 0, 5, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(engineLabel, 1, 5, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(brakeLabel, 2, 5, Qt.AlignmentFlag.AlignCenter)

        # Adding Murphy Break State Buttons
        murphyLabel = QLabel("Failure States")
        communicationsButton = QPushButton("Lose Communications")
        engineButton = QPushButton("Disable Engine")
        brakeButton = QPushButton("Disable Service Brakes")
        layout.addWidget(murphyLabel, 0, 6, 1, 4, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(communicationsButton, 1, 6)
        layout.addWidget(engineButton, 1, 7, 1, 2)
        layout.addWidget(brakeButton, 1, 9)

        # Addings Lights and Doors States
        lDoorsLabel = QLabel("Left Doors")
        rDoorsLabel = QLabel("Right Doors")
        iLightsLabel = QLabel("Internal Lights")
        eLightsLabel = QLabel("External Lights")
        layout.addWidget(lDoorsLabel, 3, 5, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(rDoorsLabel, 4, 5, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iLightsLabel, 5, 5, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(eLightsLabel, 6, 5, Qt.AlignmentFlag.AlignCenter)

        # Add Passenger Inputs : Emergency Brake and Temperature
        emergencyBrakeLabel = QLabel("Emergency Brake")
        temperatureLabel = QLabel("Temperature")
        emergencyBrakeButton = QPushButton("Emergency Brake")
        temperatureInput = QLineEdit()
        layout.addWidget(emergencyBrakeLabel, 2, 6, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(temperatureLabel, 2, 8, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(emergencyBrakeButton, 3, 6, 1, 2)
        layout.addWidget(temperatureInput, 3, 8, 1, 2)


def main():
    app = QApplication(argv)
    UI = TrainModelMainUI()
    UI.show()
    app.exec()

if (__name__ == "__main__"):
    main()