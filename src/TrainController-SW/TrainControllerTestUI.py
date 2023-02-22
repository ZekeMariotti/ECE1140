# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys

from PyQt6 import QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW

# Class for the main window
class TestWindow(QMainWindow):

        # Constructor 
        def __init__(self):
            super().__init__()    

            # TrainControllerSW Object for Test UI
            self.TrainControllerSW = TrainControllerSW(0, 0, 0, "2023-02-20T21:52:48.3940347-05:00", False, 0, 0, 0, 0, "setupStationName", 
                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "setupStationAnnouncement")    

            # Update Inputs
            self.TrainControllerSW.readInputs()               

            # Set window defaults
            self.setWindowTitle("Train Controller Test UI")
            self.setFixedSize(QSize(480, 540))

            # Set element defaults
            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.15*self.windowWidth)
            self.buttonHeight = round(0.07*self.windowHeight)
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)
            
            self.globalFont = "Times New Roman"     
            self.labelFont = QFont(self.globalFont, 15)
            self.buttonFont = QFont(self.globalFont, 9)
            self.stationFont = QFont(self.globalFont, 20)  
                
            # Create visual elements
            self.testLabel = self.testLabelSetup()
            self.setEmergencyBrakeStateLabel = self.setEmergencyBrakeStateLabelSetup()
            self.setEmergencyBrakeState = self.setEmergencyBrakeStateSetup()
            self.currentSpeedSliderLabel = self.currentSpeedSliderLabelSetup()
            self.currentSpeedSlider = self.currentSpeedSliderSetup()

            # Grid Layout
            self.mainWidget = QWidget()
            self.gridLayout = QGridLayout()
            self.gridLayout.setColumnStretch(3, 100)

            self.gridLayout.addWidget(self.setEmergencyBrakeStateLabel, 0, 0)
            self.gridLayout.addWidget(self.setEmergencyBrakeState, 0, 1)
            self.gridLayout.addWidget(self.currentSpeedSliderLabel, 1, 0)
            self.gridLayout.addWidget(self.currentSpeedSlider, 1, 1)

            self.mainWidget.setLayout(self.gridLayout)
            self.setCentralWidget(self.mainWidget)
            

                
        # widget setups
        # TODO: commandedSpeed, authority, time, undergroundState, speedLimit, temperature, engineState, stationState, stationName, platformSide, externalLightState,
        #       internalLightState, leftDoorState, rightDoorState, serviceBrakeState,  engineStatus, communicationsStatus
        def testLabelSetup(self):
            testLabel = QLabel()         
            testLabel.setFont(self.stationFont)
            testLabel.setText("Test UI")
            testLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            testLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            testLabel.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-testLabel.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.07-testLabel.frameGeometry().height()*0.5)
            testLabel.move(x, y)
            testLabel.setParent(self)
            return testLabel
        
        def setEmergencyBrakeStateLabelSetup(self):
            setEmergencyBrakeStateLabel = QLabel()
            setEmergencyBrakeStateLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            setEmergencyBrakeStateLabel.setText("Emergency\nBrake:")
            setEmergencyBrakeStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
           # x = round(self.frameGeometry().width()*0.05)
           # y = round(self.frameGeometry().height()*0.1)
           # setEmergencyBrakeStateLabel.move(x, y)
            setEmergencyBrakeStateLabel.setParent(self)
            return setEmergencyBrakeStateLabel

        
        def setEmergencyBrakeStateSetup(self):
             setEmergencyBrakeState = QComboBox()
             setEmergencyBrakeState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
             setEmergencyBrakeState.addItems(["Disabled", "Enabled"])
             setEmergencyBrakeState.activated.connect(self.setEmergencyBrakeStateActivated)
           #  x = round(self.setEmergencyBrakeStateLabel.frameGeometry().x())
            # y = round(self.setEmergencyBrakeStateLabel.frameGeometry().height()+self.frameGeometry().width()*0.13)
            # setEmergencyBrakeState.move(x, y)
             setEmergencyBrakeState.setParent(self)
             return setEmergencyBrakeState
        
        def currentSpeedSliderLabelSetup(self):
            currentSpeedSliderLabel = QLabel()
            currentSpeedSliderLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            currentSpeedSliderLabel.setText("Current\nSpeed:")
            currentSpeedSliderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            currentSpeedSliderLabel.setParent(self)
            return currentSpeedSliderLabel

        def currentSpeedSliderSetup(self):
            currentSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            currentSpeedSlider.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonWidth*0.3)))
            currentSpeedSlider.valueChanged.connect(self.currentSpeedSliderRelease)
            currentSpeedSlider.setRange(0, self.TrainControllerSW.MAX_SPEED)
            currentSpeedSlider.setSingleStep(1)
            currentSpeedSlider.setParent(self)
            return currentSpeedSlider


        # event actions
        def currentSpeedSliderRelease(self):
             self.TrainControllerSW.inputs.currentSpeed = self.currentSpeedSlider.value()
             self.TrainControllerSW.writeInputs()

        def setEmergencyBrakeStateActivated(self):
             self.TrainControllerSW.inputs.emergencyBrakeState = (self.setEmergencyBrakeState.currentText() == "Enabled")
             self.TrainControllerSW.writeInputs()


# Class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


# Run Test UI Alone
if (False):  
    app = QApplication(sys.argv)

    testWindow = TestWindow()
    testWindow.show()

    app.exec()