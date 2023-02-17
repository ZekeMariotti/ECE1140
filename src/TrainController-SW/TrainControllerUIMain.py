# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys

from PyQt6.QtWidgets import *
from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW

# Class for the main window
class MainWindow(QMainWindow):

        # Constructor 
        def __init__(self):
            super().__init__()

            self.TrainControllerSW = TrainControllerSW(0, 0, 0, "setupTime", False, 0, 0, 0, 0, "setupStationName", 
                                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "setupStationAnnouncement")
            testState = True

            if(testState):
                self.TrainControllerSW.time = "8:46"
                self.TrainControllerSW.stationName = "SHADYSIDE"
                self.TrainControllerSW.currentSpeed = 20
                self.TrainControllerSW.engineState = 1
                self.TrainControllerSW.emergencyBrakeState = False
                self.TrainControllerSW.serviceBrakeState = False
                self.TrainControllerSW.commandedSpeed = 20
                self.TrainControllerSW.authority = 600
                self.TrainControllerSW.speedLimit = 25
                self.TrainControllerSW.temperature = 75
                self.TrainControllerSW.internalLightsState = True
                self.TrainControllerSW.externalLightsState = False
                self.TrainControllerSW.leftDoorState = False
                self.TrainControllerSW.rightDoorState = False

            self.setWindowTitle("Train Controller")
            self.resize(QSize(1366, 768))
            self.setMinimumSize(1050, 550)

            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.13*self.windowWidth)
            self.buttonHeight = round(0.06*self.windowHeight)
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)             
                
            self.station = self.stationSetup()
            self.currentSpeed = self.currentSpeedSetup()
            self.manualSpeedOverride = self.manualSpeedOverrideSetup()
            self.realTimeClock = self.realTimeClockSetup()
            self.engineState = self.engineStateSetup()
            self.emergencyBrakeState = self.emergencyBrakeStateSetup()
            self.emergencyBrakeEnable = self.emergencyBrakeEnableSetup()
            self.emergencyBrakeDisable = self.emergencyBrakeDisableSetup()
            self.serviceBrakeState = self.serviceBrakeStateSetup()
            self.serviceBrakeEnable = self.serviceBrakeEnableSetup()
            self.serviceBrakeDisable = self.serviceBrakeDisableSetup()
            self.commandedSpeedSlider = self.commandedSpeedSliderSetup()  
            self.commandedSpeed = self.commandedSpeedSetup()
            self.authority = self.authoritySetup()
            self.speedLimit = self.speedLimitSetup()
            self.temperature = self.temperatureSetup()
            self.internalLightsState = self.internalLightsStateSetup()
            self.internalLightsEnable = self.internalLightsEnableSetup()
            self.internalLightsDisable = self.internalLightsDisableSetup()
            self.externalLightsState = self.externalLightsStateSetup()
            self.externalLightsEnable = self.externalLightsEnableSetup()
            self.externalLightsDisable = self.externalLightsDisableSetup()
            self.leftDoorState = self.leftDoorStateSetup()
            self.leftDoorOpen = self.leftDoorOpenSetup()
            self.leftDoorClose = self.leftDoorCloseSetup()
            self.rightDoorState = self.rightDoorStateSetup()
            self.rightDoorOpen = self.rightDoorOpenSetup()
            self.rightDoorClose = self.rightDoorCloseSetup()


                
        # widget setups
        def stationSetup(self):
            station = QLabel()          
            station.setText("Current Station:\n" + self.TrainControllerSW.stationName)
            station.setFixedSize(QSize(round(self.labelWidth*1.6), self.labelHeight*2))
            station.setAlignment(Qt.AlignmentFlag.AlignCenter)
            station.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-station.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.05-station.frameGeometry().height()*0.5)
            station.move(x, y)
            station.setParent(self)
            return station

        def currentSpeedSetup(self):
            currentSpeed = QLabel()
            currentSpeed.setText("Current Speed: " + str(self.TrainControllerSW.currentSpeed) + " MPH")
            currentSpeed.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            currentSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            currentSpeed.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-currentSpeed.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.15-currentSpeed.frameGeometry().height()*0.5)
            currentSpeed.move(x, y)
            currentSpeed.setParent(self)
            return currentSpeed

        def manualSpeedOverrideSetup(self):
            manualSpeedOverride = QLabel()  
            manualSpeedOverride.setText("Manual Speed Override:")
            manualSpeedOverride.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            manualSpeedOverride.setAlignment(Qt.AlignmentFlag.AlignCenter)
            manualSpeedOverride.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-manualSpeedOverride.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.3-manualSpeedOverride.frameGeometry().height()*0.5)
            manualSpeedOverride.move(x, y)
            manualSpeedOverride.setParent(self)
            return manualSpeedOverride

        def realTimeClockSetup(self):
            realTimeClock = QLabel()  
            realTimeClock.setText("Time: " + self.TrainControllerSW.time)
            realTimeClock.setFixedSize(QSize(self.labelWidth, round(self.labelHeight*0.5)))
            realTimeClock.setAlignment(Qt.AlignmentFlag.AlignCenter)
            realTimeClock.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.05-realTimeClock.frameGeometry().height()*0.5)
            realTimeClock.move(x, y)
            realTimeClock.setParent(self)
            return realTimeClock

        def engineStateSetup(self):
            engineState = QLabel()            
            engineState.setText("Engine State:\n" + self.TrainControllerSW.getEngineState())
            engineState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            engineState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            engineState.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.15-engineState.frameGeometry().height()*0.5)
            engineState.move(x, y)
            engineState.setParent(self)
            return engineState
        
        def emergencyBrakeStateSetup(self):
            emergencyBrakeState = QLabel()  
            emergencyBrakeState.setText("Emergency Brake:\n" + self.TrainControllerSW.getEmergencyBrakeState())
            emergencyBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            emergencyBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emergencyBrakeState.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.25-emergencyBrakeState.frameGeometry().height()*0.6)
            emergencyBrakeState.move(x, y)
            emergencyBrakeState.setParent(self)
            return emergencyBrakeState

        def emergencyBrakeEnableSetup(self):
            emergencyBrakeEnable = QPushButton("Enable\nEmergency Brake")     
            emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeEnable.clicked.connect(self.emergencyBrakeEnableClick)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.3-emergencyBrakeEnable.frameGeometry().height()*0.5)
            emergencyBrakeEnable.move(x, y)
            emergencyBrakeEnable.setParent(self)
            return emergencyBrakeEnable

        def emergencyBrakeDisableSetup(self):
            emergencyBrakeDisable = QPushButton("Disable\nEmergency Brake")           
            emergencyBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeDisable.clicked.connect(self.emergencyBrakeDisableClick)
            x = round(self.frameGeometry().width()*0.05+emergencyBrakeDisable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.3-emergencyBrakeDisable.frameGeometry().height()*0.5)
            emergencyBrakeDisable.move(x, y)
            emergencyBrakeDisable.setParent(self)
            return emergencyBrakeDisable

        def serviceBrakeStateSetup(self):
            serviceBrakeState = QLabel()
            serviceBrakeState.setText("Service Brake:\n" + self.TrainControllerSW.getServiceBrakeState())
            serviceBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            serviceBrakeState.setWordWrap(True)
            serviceBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.4-serviceBrakeState.frameGeometry().height()*0.6)
            serviceBrakeState.move(x, y)
            serviceBrakeState.setParent(self)
            return serviceBrakeState

        def serviceBrakeEnableSetup(self):
            serviceBrakeEnable = QPushButton("Enable\nService Brake")  
            serviceBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeEnable.clicked.connect(self.serviceBrakeEnableClick)
            x = round(self.frameGeometry().width()*0.05)
            y = round(self.frameGeometry().height()*0.45-serviceBrakeEnable.frameGeometry().height()*0.5)
            serviceBrakeEnable.move(x, y)
            serviceBrakeEnable.setParent(self)
            return serviceBrakeEnable

        def serviceBrakeDisableSetup(self):
            serviceBrakeDisable = QPushButton("Disable\nService Brake")
            serviceBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeDisable.clicked.connect(self.serviceBrakeDisableClick)
            x = round(self.frameGeometry().width()*0.05+serviceBrakeDisable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.45-serviceBrakeDisable.frameGeometry().height()*0.5)
            serviceBrakeDisable.move(x, y)
            serviceBrakeDisable.setParent(self)
            return serviceBrakeDisable

        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(QSize(round(self.labelWidth*1.2), round(self.labelHeight*0.5)))
            commandedSpeedSlider.sliderReleased.connect(self.commandedSpeedSliderRelease)
            commandedSpeedSlider.setRange(0, 100)
            commandedSpeedSlider.setSingleStep(1)
            x = round(self.frameGeometry().width()*0.5-commandedSpeedSlider.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.325)
            commandedSpeedSlider.move(x, y)
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider

        def commandedSpeedSetup(self):
            commandedSpeed = QLabel()
            commandedSpeed.setText("Commanded Speed:\n" + str(self.TrainControllerSW.commandedSpeed) + " MPH")
            commandedSpeed.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            commandedSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            commandedSpeed.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.05-commandedSpeed.frameGeometry().height()*0.5)
            commandedSpeed.move(x, y)
            commandedSpeed.setParent(self)
            return commandedSpeed

        def authoritySetup(self):
            authority = QLabel()        
            authority.setText("Authority:\n" + str(self.TrainControllerSW.authority) + " FEET")
            authority.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            authority.setAlignment(Qt.AlignmentFlag.AlignCenter)
            authority.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.15-authority.frameGeometry().height()*0.5)
            authority.move(x, y)
            authority.setParent(self)
            return authority

        def speedLimitSetup(self):
            speedLimit = QLabel()     
            speedLimit.setText("Speed Limit:\n" + str(self.TrainControllerSW.speedLimit) + " MPH")
            speedLimit.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            speedLimit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            speedLimit.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.25-speedLimit.frameGeometry().height()*0.5)
            speedLimit.move(x, y)
            speedLimit.setParent(self)
            return speedLimit

        def temperatureSetup(self):
            temperature = QLabel()        
            temperature.setText("Temperature:\n" + str(self.TrainControllerSW.temperature) + " F")
            temperature.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            temperature.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temperature.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.35-temperature.frameGeometry().height()*0.5)
            temperature.move(x, y)
            temperature.setParent(self)
            return temperature

        def internalLightsStateSetup(self):
            internalLightsState = QLabel()          
            internalLightsState.setText("Internal Lights: " + self.TrainControllerSW.getInternalLightsState())
            internalLightsState.setFixedSize(QSize(round(self.labelWidth*0.8), round(self.labelHeight*0.8)))
            internalLightsState.setWordWrap(True)
            internalLightsState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.42-internalLightsState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.45-internalLightsState.frameGeometry().height()*0.6)
            internalLightsState.move(x, y)
            internalLightsState.setParent(self)
            return internalLightsState

        def internalLightsEnableSetup(self):
            internalLightsEnable = QPushButton("Enable\nInternal Lights")      
            internalLightsEnable.setFixedSize(QSize(round(self.buttonWidth*0.5), self.buttonHeight))
            internalLightsEnable.clicked.connect(self.internalLightsEnableClick)
            x = round(self.frameGeometry().width()*0.35)
            y = round(self.frameGeometry().height()*0.5-internalLightsEnable.frameGeometry().height()*0.5)
            internalLightsEnable.move(x, y)
            internalLightsEnable.setParent(self)
            return internalLightsEnable

        def internalLightsDisableSetup(self):
            internalLightsDisable = QPushButton("Disable\nInternal Lights")            
            internalLightsDisable.setFixedSize(QSize(round(self.buttonWidth*0.5), self.buttonHeight))
            internalLightsDisable.clicked.connect(self.internalLightsDisableClick)
            x = round(self.frameGeometry().width()*0.35+internalLightsDisable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.5-internalLightsDisable.frameGeometry().height()*0.5)
            internalLightsDisable.move(x, y)
            internalLightsDisable.setParent(self)
            return internalLightsDisable

        def externalLightsStateSetup(self):
            externalLightsState = QLabel()
            externalLightsState.setText("External Lights: " + self.TrainControllerSW.getExternalLightsState())
            externalLightsState.setFixedSize(QSize(round(self.labelWidth*0.8), round(self.labelHeight*0.8)))
            externalLightsState.setWordWrap(True)
            externalLightsState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.42-externalLightsState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.6-externalLightsState.frameGeometry().height()*0.6)
            externalLightsState.move(x, y)
            externalLightsState.setParent(self)
            return externalLightsState

        def externalLightsEnableSetup(self):
            externalLightsEnable = QPushButton("Enable\nExternal Lights")
            externalLightsEnable.setFixedSize(QSize(round(self.buttonWidth*0.5), self.buttonHeight))
            externalLightsEnable.clicked.connect(self.externalLightsEnableClick)
            x = round(self.frameGeometry().width()*0.35)
            y = round(self.frameGeometry().height()*0.65-externalLightsEnable.frameGeometry().height()*0.5)
            externalLightsEnable.move(x, y)
            externalLightsEnable.setParent(self)
            return externalLightsEnable

        def externalLightsDisableSetup(self):
            externalLightsDisable = QPushButton("Disable\nExternal Lights")         
            externalLightsDisable.setFixedSize(QSize(round(self.buttonWidth*0.5), self.buttonHeight))
            externalLightsDisable.clicked.connect(self.externalLightsDisableClick)
            x = round(self.frameGeometry().width()*0.35+externalLightsDisable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.65-externalLightsDisable.frameGeometry().height()*0.5)
            externalLightsDisable.move(x, y)
            externalLightsDisable.setParent(self)
            return externalLightsDisable
            
        def leftDoorStateSetup(self):
            leftDoorState = QLabel()
            leftDoorState.setText("Left Door\n" + self.TrainControllerSW.getLeftDoorState())
            leftDoorState.setFixedSize(QSize(round(self.labelWidth*0.4), round(self.labelHeight*0.8)))
            leftDoorState.setWordWrap(True)
            leftDoorState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.55-leftDoorState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.45-leftDoorState.frameGeometry().height()*0.6)
            leftDoorState.move(x, y)
            leftDoorState.setParent(self)
            return leftDoorState
            
        def leftDoorOpenSetup(self):
            leftDoorOpen = QPushButton("Open Doors")
            leftDoorOpen.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            leftDoorOpen.clicked.connect(self.leftDoorOpenClick)
            x = round(self.frameGeometry().width()*0.515)
            y = round(self.frameGeometry().height()*0.485-leftDoorOpen.frameGeometry().height()*0.5)
            leftDoorOpen.move(x, y)
            leftDoorOpen.setParent(self)
            return leftDoorOpen
        
        def leftDoorCloseSetup(self):
            leftDoorClose = QPushButton("Close Doors")
            leftDoorClose.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            leftDoorClose.clicked.connect(self.leftDoorCloseClick)
            x = round(self.frameGeometry().width()*0.515)
            y = round(self.frameGeometry().height()*0.485+leftDoorClose.frameGeometry().height()*0.5)
            leftDoorClose.move(x, y)
            leftDoorClose.setParent(self)
            return leftDoorClose

        def rightDoorStateSetup(self):
            rightDoorState = QLabel()
            rightDoorState.setText("Right Door\n" + self.TrainControllerSW.getRightDoorState())
            rightDoorState.setFixedSize(QSize(round(self.labelWidth*0.4), round(self.labelHeight*0.8)))
            rightDoorState.setWordWrap(True)
            rightDoorState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.56)
            y = round(self.frameGeometry().height()*0.45-rightDoorState.frameGeometry().height()*0.6)
            rightDoorState.move(x, y)
            rightDoorState.setParent(self)
            return rightDoorState
            
        def rightDoorOpenSetup(self):
            rightDoorOpen = QPushButton("Open Doors")
            rightDoorOpen.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            rightDoorOpen.clicked.connect(self.rightDoorOpenClick)
            x = round(self.frameGeometry().width()*0.515+rightDoorOpen.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.485-rightDoorOpen.frameGeometry().height()*0.5)
            rightDoorOpen.move(x, y)
            rightDoorOpen.setParent(self)
            return rightDoorOpen
        
        def rightDoorCloseSetup(self):
            rightDoorClose = QPushButton("Close Doors")
            rightDoorClose.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            rightDoorClose.clicked.connect(self.rightDoorCloseClick)
            x = round(self.frameGeometry().width()*0.515+rightDoorClose.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.485+rightDoorClose.frameGeometry().height()*0.5)
            rightDoorClose.move(x, y)
            rightDoorClose.setParent(self)
            return rightDoorClose
            

        # event actions

        # might use for resizing elements - adds 31 to height for some reason
        # def resizeEvent(self, event):
        #    self.windowWidth = self.frameGeometry().width()
        #    self.windowHeight = self.frameGeometry().height()
        #    self.buttonWidth = round(0.13*self.windowWidth)
        #    self.buttonHeight = round(0.06*self.windowHeight)
        #    self.labelWidth = self.buttonWidth*2
        #    self.labelHeight = round(self.buttonHeight*1.3)
        
        #    print("width: " + str(self.frameGeometry().width()) + " Height: " + str(self.frameGeometry().height()))
        #    emergencyBrakeEnable = self.emergencyBrakeEnable
        #    emergencyBrakeEnable.move(round(self.frameGeometry().width()*0.05), round(self.frameGeometry().height()*0.3-emergencyBrakeEnable.frameGeometry().height()*0.5))
        #    emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
        #    QMainWindow.resizeEvent(self, event)
           

        def emergencyBrakeEnableClick(self):
            self.TrainControllerSW.emergencyBrakeCommand = True

        def emergencyBrakeDisableClick(self):
            self.TrainControllerSW.emergencyBrakeCommand = False

        def serviceBrakeEnableClick(self):
            self.TrainControllerSW.serviceBrakeCommand = True

        def serviceBrakeDisableClick(self):
            self.TrainControllerSW.serviceBrakeCommand = False

        def commandedSpeedSliderRelease(self):
            self.TrainControllerSW.commandedSpeed = self.commandedSpeedSlider.value()

        def internalLightsEnableClick(self):
            self.TrainControllerSW.internalLightCommand = True

        def internalLightsDisableClick(self):
            self.TrainControllerSW.internalLightCommand = False

        def externalLightsEnableClick(self):
            self.TrainControllerSW.externalLightCommand = True

        def externalLightsDisableClick(self):
            self.TrainControllerSW.externalLightCommand = False

        def leftDoorOpenClick(self):
            self.TrainControllerSW.leftDoorCommand = True
        
        def leftDoorCloseClick(self):
            self.TrainControllerSW.leftDoorCommand = False

        def rightDoorOpenClick(self):
            self.TrainControllerSW.rightDoorCommand = True

        def rightDoorCloseClick(self):
            self.TrainControllerSW.rightDoorCommand = False

# class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()