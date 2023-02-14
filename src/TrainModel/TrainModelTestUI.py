# Train Model Test UI

# Importing all required modules
from sys import argv
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QComboBox, QLineEdit

class TrainModelTestUI(QWidget):
    def __init__(self):
        # Initializing the layout of the UI
        super(TrainModelTestUI, self).__init__()
        self.setWindowTitle("Train Model Test UI")
        layout = QGridLayout()
        self.setLayout(layout)

        # Add the Power Input
        powerLabel = QLabel("Power Input")
        layout.addWidget(powerLabel, 0, 0)
        powerInput = QLineEdit()
        layout.addWidget(powerInput, 0, 1)

        # Add the Service Brake
        serviceBrakeLabel = QLabel("Service Brake")
        layout.addWidget(serviceBrakeLabel, 1, 0)
        serviceBrakeInput = QComboBox()
        serviceBrakeInput.addItems(["Engaged", "Disengaged"])
        layout.addWidget(serviceBrakeInput, 1, 1)

        # Add the Emergency Brake
        emergencyBrakeLabel = QLabel("Service Brake")
        layout.addWidget(emergencyBrakeLabel, 2, 0)
        emergencyBrakeInput = QComboBox()
        emergencyBrakeInput.addItems(["Engaged", "Disengaged"])
        layout.addWidget(emergencyBrakeInput, 2, 1)

        # Add the Left Door Switch
        leftDoorLabel = QLabel("Left Doors")
        layout.addWidget(leftDoorLabel, 3, 0)
        leftDoorInput = QComboBox()
        leftDoorInput.addItems(["Open", "Closed"])
        layout.addWidget(leftDoorInput, 3, 1)

        # Add the Right Door Switch
        rightDoorLabel = QLabel("Right Doors")
        layout.addWidget(rightDoorLabel, 4, 0)
        rightDoorInput = QComboBox()
        rightDoorInput.addItems(["Open", "Closed"])
        layout.addWidget(rightDoorInput, 4, 1)

        # Add the External Lights Switch
        externalLightLabel = QLabel("External Lights")
        layout.addWidget(externalLightLabel, 5, 0)
        externalLightInput = QComboBox()
        externalLightInput.addItems(["On", "Off"])
        layout.addWidget(externalLightInput, 5, 1)

        # Add the Internal Lights Switch
        internalLightLabel = QLabel("Internal Lights")
        layout.addWidget(internalLightLabel, 6, 0)
        internalLightInput = QComboBox()
        internalLightInput.addItems(["On", "Off"])
        layout.addWidget(internalLightInput, 6, 1)

        # Add the Station Announcement Input
        stationLabel = QLabel("Station Announcement")
        layout.addWidget(stationLabel, 7, 0)
        stationInput = QLineEdit()
        layout.addWidget(stationInput, 7, 1)

        # Add the Real Time Clock Input
        realTimeClockLabel = QLabel("Real Time Clock")
        layout.addWidget(realTimeClockLabel, 8, 0)
        realTimeClockInput = QLineEdit()
        layout.addWidget(realTimeClockInput, 8, 1)

        # Add the Authority Input
        authorityLabel = QLabel("Authority")
        layout.addWidget(authorityLabel, 9, 0)
        authorityInput = QLineEdit()
        layout.addWidget(authorityInput, 9, 1)

        # Add the Commanded Speed Input
        commandedSpeedLabel = QLabel("Commanded Speed")
        layout.addWidget(commandedSpeedLabel, 10, 0)
        commandedSpeedInput = QLineEdit()
        layout.addWidget(commandedSpeedInput, 10, 1)

        # Add the Passengers Entering Input
        passengersEnteringLabel = QLabel("Passengers Entering")
        layout.addWidget(passengersEnteringLabel, 11, 0)
        passengersEnteringInput = QLineEdit()
        layout.addWidget(passengersEnteringInput, 11, 1)

        # Add the Grade Input
        gradeLabel = QLabel("Grade")
        layout.addWidget(gradeLabel, 12, 0)
        gradeInput = QLineEdit()
        layout.addWidget(gradeInput, 12, 1)

        # Add the Speed Limit Input
        speedLimitLabel = QLabel("Speed Limit")
        layout.addWidget(speedLimitLabel, 13, 0)
        speedLimitInput = QLineEdit()
        layout.addWidget(speedLimitInput, 13, 1)

        # Add the Acceleration Limit Input
        accelerationLimitLabel = QLabel("Acceleration Limit")
        layout.addWidget(accelerationLimitLabel, 14, 0)
        accelerationLimitInput = QLineEdit()
        layout.addWidget(accelerationLimitInput, 14, 1)

        # Add the Underground State Switch
        undergroundStateLabel = QLabel("Underground State")
        layout.addWidget(undergroundStateLabel, 15, 0)
        undergroundStateInput = QComboBox()
        undergroundStateInput.addItems(["True", "False"])
        layout.addWidget(undergroundStateInput, 15, 1)

        # Add the Beacon Inputs [Station State, Next Station Name, Platform Side]
        beaconLabel = QLabel("Beacon Inputs")
        layout.addWidget(beaconLabel, 16, 0)
        beaconLabel2 = QLabel("[Station State, Next Station Name, Platform Side]")
        layout.addWidget(beaconLabel2, 16, 1)

        # Station State Beacon Input
        stationStateLabel = QLabel("Station State")
        layout.addWidget(stationStateLabel, 17, 0)
        stationStateInput = QComboBox()
        stationStateInput.addItems(["True", "False"])
        layout.addWidget(stationStateInput, 17, 1)

        # Next Station Name Beacon Input
        nextStationLabel = QLabel("Next Station Name")
        layout.addWidget(nextStationLabel, 18, 0)
        nextStationInput = QLineEdit()
        layout.addWidget(nextStationInput, 18, 1)

        # Platform Side Beacon Input
        platformSideLabel = QLabel("Platform Side")
        layout.addWidget(platformSideLabel, 19, 0)
        platformSideInput = QComboBox()
        platformSideInput.addItems(["Left", "Right", "Both"])
        layout.addWidget(platformSideInput, 19, 1)



    

if __name__ == "__main__":
    app = QApplication(argv)

    form = TrainModelTestUI()
    form.show()

    app.exec()