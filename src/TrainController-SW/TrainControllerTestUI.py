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
            self.TrainControllerSW = TrainControllerSW(0, 0, 0, "setupTime", False, 0, 0, 0, 0, "setupStationName", 
                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "setupStationAnnouncement")                   

            # set window defaults
            self.setWindowTitle("Train Controller Test UI")
            self.setFixedSize(QSize(480, 540))

            # set element defaults
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
                
            # create visual elements
            self.test = self.testSetup()
            self.currentSpeedSlider = self.currentSpeedSliderSetup()
            self.setEmergencyBrakeState = self.setEmergencyBrakeStateSetup()


                
        # widget setups
        # TODO: speedLimit, temperature, currentSpeed, authority, externalLightState, internalLightState, undergroundState, engineState, doorState, emergencyBrakeState
        # serviceBrakeState
        def testSetup(self):
            test = QLabel()         
            test.setFont(self.stationFont)
            test.setText("Test UI")
            test.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            test.setAlignment(Qt.AlignmentFlag.AlignCenter)
            test.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-test.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.07-test.frameGeometry().height()*0.5)
            test.move(x, y)
            test.setParent(self)
            return test
        
        def currentSpeedSliderSetup(self):
            currentSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            currentSpeedSlider.setFixedSize(QSize(round(self.labelWidth*1), round(self.labelHeight*0.5)))
            currentSpeedSlider.sliderReleased.connect(self.currentSpeedSliderRelease)
            currentSpeedSlider.setRange(0, self.TrainControllerSW.MAX_SPEED)
            currentSpeedSlider.setSingleStep(1)
            x = round(self.frameGeometry().width()*0.5-currentSpeedSlider.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.37)
            currentSpeedSlider.move(x, y)
            currentSpeedSlider.setParent(self)
            return currentSpeedSlider
        
        def setEmergencyBrakeStateSetup(self):
             setEmergencyBrakeState = QComboBox()
             setEmergencyBrakeState.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
             setEmergencyBrakeState.addItems(["Enabled", "Disabled"])
             setEmergencyBrakeState.setEditText("E-Brake")
             setEmergencyBrakeState.activated.connect(self.setEmergencyBrakeStateActivated)
             x = round(self.frameGeometry().width()*0.1)
             y = round(self.frameGeometry().height()*0.2)
             setEmergencyBrakeState.move(x, y)
             setEmergencyBrakeState.setParent(self)
             return setEmergencyBrakeState


        # event actions
        def currentSpeedSliderRelease(self):
             self.TrainControllerSW.inputs.currentSpeed = self.currentSpeedSlider.value()

        def setEmergencyBrakeStateActivated(self):
             self.TrainControllerSW.inputs.emergencyBrakeState = (self.setEmergencyBrakeState.currentText() == "Enabled")
             self.TrainControllerSW.writeInputs()



# class to create color widgets
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