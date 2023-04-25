# Main UI for the Train Controller Software

from distutils.cmd import Command
import sys
import os

sys.path.append(__file__.replace("\TrainControllerSoftware\TrainControllerMainUI.py", ""))

import Integration.Conversions as Conversions

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from TrainControllerSW import TrainControllerSW
from TrainControllerTestUI import TestWindow
from Integration.TMTCSignals import *
from animated_toggle import AnimatedToggle


# Class for Worker (multithreading)
class Worker(QObject):
    finished = pyqtSignal()

# Class for the main window
class MainWindow(QMainWindow):

        # Constructor 
        def __init__(self, trainLine , id=2):
            super().__init__()

            # Enable Test UI
            self.testUI = True 
            
            # Initialize TrainControllerSW object
            self.TrainControllerSW = TrainControllerSW(trainId=id, line = trainLine, commandedSpeed=0, currentSpeed=0, authority=10, inputTime="2023-02-20T21:52:48.3940347-05:00", 
                                                       undergroundState=False, temperature=0, stationName="setupStationName", platformSide=0, 
                                                       nextStationName="station2", isBeacon=False, externalLightsState=False, internalLightsState=False, leftDoorState=False, 
                                                       rightDoorState=False, serviceBrakeState=False, emergencyBrakeState=False, serviceBrakeStatus=False, engineStatus=False, 
                                                       communicationsStatus=False, power=0, leftDoorCommand=False, rightDoorCommand=False, serviceBrakeCommand=False, 
                                                       emergencyBrakeCommand=False, externalLightCommand=False, internalLightCommand=False, stationAnnouncement="setupStationAnnouncement")
            
            # Get block list
            self.TrainControllerSW.getBlocksData()

            # Update Inputs, Outputs, and time
            self.TrainControllerSW.writeOutputs()          
            self.TrainControllerSW.previousTime = self.TrainControllerSW.realTime
            self.TrainControllerSW.currentTime = self.TrainControllerSW.realTime

            # Set window defaults
            self.setWindowTitle(f'Train Controller {self.TrainControllerSW.trainId}')
            self.setFixedSize(QSize(960, 540))
            self.setMinimumSize(1050, 550)
            self.move(100, 200)

            # Set element defaults
            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.13*self.windowWidth)
            self.buttonHeight = round(0.07*self.windowHeight)
            self.labelWidth = self.buttonWidth*2
            self.labelHeight = round(self.buttonHeight*1.3)
            
            self.globalFont = "Times New Roman"     
            self.labelFont = QFont(self.globalFont, 13)
            self.buttonFont = QFont(self.globalFont, 9)
            self.stationFont = QFont(self.globalFont, 16)  

            # Styling elements
            #self.setStyleSheet("QLabel { background-color: rgb(180, 180, 180); border: 1px solid; border-color: rgb(0, 0, 0) }")
                
            # Create visual elements
            self.mainTimer = self.mainTimerSetup()
            self.KpLabel = self.KpLabelSetup()
            self.Kp = self.KpSetup()
            self.KiLabel = self.KiLabelSetup()
            self.Ki = self.KiSetup()
            self.station = self.stationSetup()
            self.currentSpeed = self.currentSpeedSetup()
            self.communicationsError = self.communicationsErrorSetup()
            self.manualSpeedOverride = self.manualSpeedOverrideSetup()
            self.manualModeToggle = self.manualModeToggleSetup()
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

            # Test UI
            if (self.testUI):
                self.TrainControllerTestUI = TestWindow()
                self.TrainControllerTestUI.move(self.frameGeometry().width()+round(1.1*self.frameGeometry().x()), 200)


                
        # Widget setups
        def mainThreadSetup(self):
            self.timerThread = QThread()
            self.timerThread.started.connect(self.mainTimerSetup)

        def mainTimerSetup(self):     
            mainTimer = QTimer()
            mainTimer.setInterval(100)
            mainTimer.timeout.connect(self.mainEventLoop)
            mainTimer.setParent(self)
            mainTimer.start()
            return mainTimer
        
        def KpLabelSetup(self):
            KpLabel = QLabel()
            KpLabel.setFont(self.labelFont)
            KpLabel.setText("Kp: ")
            KpLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            KpLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            KpLabel.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.8-KpLabel.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.8-KpLabel.frameGeometry().height()*0.5)
            KpLabel.move(x, y)
            KpLabel.setParent(self)
            return KpLabel
        
        def KpSetup(self):
            Kp = QLineEdit()
            Kp.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight)))
            Kp.textChanged.connect(self.kpTextChanged)
            x = round(self.frameGeometry().width()*0.77-Kp.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.85-Kp.frameGeometry().height()*0.5)
            Kp.move(x, y)
            Kp.setParent(self)
            return Kp
        
        def KiLabelSetup(self):
            KiLabel = QLabel()
            KiLabel.setFont(self.labelFont)
            KiLabel.setText("Ki: ")
            KiLabel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight)))
            KiLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            KiLabel.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.9-KiLabel.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.8-KiLabel.frameGeometry().height()*0.5)
            KiLabel.move(x, y)
            KiLabel.setParent(self)
            return KiLabel
        
        def KiSetup(self):
            Ki = QLineEdit()
            Ki.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight)))
            Ki.textChanged.connect(self.kiTextChanged)
            x = round(self.frameGeometry().width()*0.87-Ki.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.85-Ki.frameGeometry().height()*0.5)
            Ki.move(x, y)
            Ki.setParent(self)
            return Ki

        def stationSetup(self):
            station = QLabel()         
            station.setFont(self.stationFont)

            if(self.TrainControllerSW.stationState == True):
                station.setText(f'Current Station:\n{self.TrainControllerSW.inputs.stationName}')
            else:
                station.setText(f'Next Station:\n{self.TrainControllerSW.inputs.nextStationName}')       
            
            station.setFixedSize(QSize(round(self.labelWidth*1.3), round(self.labelHeight*1.25)))
            station.setAlignment(Qt.AlignmentFlag.AlignCenter)
            station.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-station.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.07-station.frameGeometry().height()*0.5)
            station.move(x, y)
            station.setParent(self)
            return station

        def currentSpeedSetup(self):
            currentSpeed = QLabel()
            currentSpeed.setFont(self.stationFont)
            currentSpeed.setText("Current Speed: " + str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.inputs.currentSpeed))) + " MPH")
            currentSpeed.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            currentSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            currentSpeed.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-currentSpeed.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.19-currentSpeed.frameGeometry().height()*0.5)
            currentSpeed.move(x, y)
            currentSpeed.setParent(self)
            return currentSpeed
        
        def communicationsErrorSetup(self):
            communicationsError = QLabel()
            communicationsError.setFont(self.stationFont)
            communicationsError.setText("ERROR: External Communications Failure")
            communicationsError.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            communicationsError.setAlignment(Qt.AlignmentFlag.AlignCenter)
            communicationsError.setWordWrap(True)
            communicationsError.setStyleSheet("QLabel { color : Red; }")
            x = round(self.frameGeometry().width()*0.5-communicationsError.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.26-communicationsError.frameGeometry().height()*0.5)
            communicationsError.move(x, y)
            communicationsError.setParent(self)

            if (self.TrainControllerSW.inputs.communicationsStatus == True):
                communicationsError.hide()
            else:
                communicationsError.show()
            return communicationsError

        def manualSpeedOverrideSetup(self):
            manualSpeedOverride = QLabel()  
            manualSpeedOverride.setFont(self.stationFont)
            manualSpeedOverride.setText(f'Manual Mode: {"Enabled" if self.TrainControllerSW.manualMode else "Disabled"}')
            manualSpeedOverride.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*0.5)))
            manualSpeedOverride.setAlignment(Qt.AlignmentFlag.AlignCenter)
            manualSpeedOverride.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-manualSpeedOverride.frameGeometry().width()*.5)
            y = round(self.frameGeometry().height()*0.33-manualSpeedOverride.frameGeometry().height()*0.5)
            manualSpeedOverride.move(x, y)
            manualSpeedOverride.setParent(self)
            return manualSpeedOverride
        
        def manualModeToggleSetup(self):
            manualModeToggle = AnimatedToggle()
            manualModeToggle.setFixedSize(manualModeToggle.sizeHint())
            manualModeToggle.stateChanged.connect(self.manualModeToggleEvent)
            x = round(self.frameGeometry().width()*0.61)
            y = round(self.frameGeometry().height()*0.36)
            manualModeToggle.move(x, y)
            manualModeToggle.setParent(self)
            return manualModeToggle

        def realTimeClockSetup(self):
            realTimeClock = QLabel() 
            realTimeClock.setFont(self.stationFont) 

            realTimeClock.setText(f'Time: {self.TrainControllerSW.realTime.time()}'[:-7])

            realTimeClock.setFixedSize(QSize(self.labelWidth, round(self.labelHeight*0.5)))
            realTimeClock.setAlignment(Qt.AlignmentFlag.AlignCenter)
            realTimeClock.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.18-realTimeClock.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.05-realTimeClock.frameGeometry().height()*0.5)
            realTimeClock.move(x, y)
            realTimeClock.setParent(self)
            return realTimeClock

        def engineStateSetup(self):
            engineState = QLabel()    
            engineState.setFont(self.labelFont)        
            engineState.setText("Engine State:\n" + self.TrainControllerSW.getEngineState())
            engineState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            engineState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            engineState.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.18-engineState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.15-engineState.frameGeometry().height()*0.5)
            engineState.move(x, y)
            engineState.setParent(self)
            return engineState
        
        def emergencyBrakeStateSetup(self):
            emergencyBrakeState = QLabel() 
            emergencyBrakeState.setFont(self.labelFont) 
            emergencyBrakeState.setText("Emergency Brake:\n" + self.TrainControllerSW.getEmergencyBrakeState())
            emergencyBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            emergencyBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emergencyBrakeState.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.5-emergencyBrakeState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.5-emergencyBrakeState.frameGeometry().height()*0.75)
            emergencyBrakeState.move(x, y)
            emergencyBrakeState.setParent(self)
            return emergencyBrakeState

        def emergencyBrakeEnableSetup(self):
            emergencyBrakeEnable = QPushButton("Enable\nEmergency Brake")     
            emergencyBrakeEnable.setFont(self.buttonFont)
            emergencyBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeEnable.clicked.connect(self.emergencyBrakeEnableClick)
            x = round(self.frameGeometry().width()*0.5-emergencyBrakeEnable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.55-emergencyBrakeEnable.frameGeometry().height()*0.5)
            emergencyBrakeEnable.move(x, y)
            emergencyBrakeEnable.setParent(self)
            return emergencyBrakeEnable

        def emergencyBrakeDisableSetup(self):
            emergencyBrakeDisable = QPushButton("Disable\nEmergency Brake")    
            emergencyBrakeDisable.setFont(self.buttonFont)       
            emergencyBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            emergencyBrakeDisable.clicked.connect(self.emergencyBrakeDisableClick)
            x = round(self.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.55-emergencyBrakeDisable.frameGeometry().height()*0.5)
            emergencyBrakeDisable.move(x, y)
            emergencyBrakeDisable.setParent(self)
            return emergencyBrakeDisable

        def serviceBrakeStateSetup(self):
            serviceBrakeState = QLabel()
            serviceBrakeState.setFont(self.labelFont)
            serviceBrakeState.setText("Service Brake:\n" + self.TrainControllerSW.getServiceBrakeState())
            serviceBrakeState.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            serviceBrakeState.setWordWrap(True)
            serviceBrakeState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.5-serviceBrakeState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.65-serviceBrakeState.frameGeometry().height()*0.75)
            serviceBrakeState.move(x, y)
            serviceBrakeState.setParent(self)
            return serviceBrakeState

        def serviceBrakeEnableSetup(self):
            serviceBrakeEnable = QPushButton("Enable\nService Brake")  
            serviceBrakeEnable.setFont(self.buttonFont)
            serviceBrakeEnable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeEnable.clicked.connect(self.serviceBrakeEnableClick)
            x = round(self.frameGeometry().width()*0.5-serviceBrakeEnable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.7-serviceBrakeEnable.frameGeometry().height()*0.5)
            serviceBrakeEnable.move(x, y)
            serviceBrakeEnable.setParent(self)
            return serviceBrakeEnable

        def serviceBrakeDisableSetup(self):
            serviceBrakeDisable = QPushButton("Disable\nService Brake")
            serviceBrakeDisable.setFont(self.buttonFont)
            serviceBrakeDisable.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            serviceBrakeDisable.clicked.connect(self.serviceBrakeDisableClick)
            x = round(self.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.7-serviceBrakeDisable.frameGeometry().height()*0.5)
            serviceBrakeDisable.move(x, y)
            serviceBrakeDisable.setParent(self)
            return serviceBrakeDisable

        # slider in km/hr because slider.setRange only takes integer (need max to be exactly 70km/hr), user sees it as mph
        def commandedSpeedSliderSetup(self):
            commandedSpeedSlider = QSlider(Qt.Orientation.Horizontal)
            commandedSpeedSlider.setFixedSize(QSize(round(self.labelWidth*0.9), round(self.labelHeight*0.5)))
            commandedSpeedSlider.valueChanged.connect(self.commandedSpeedSliderValueChanged)
            commandedSpeedSlider.setRange(0, self.TrainControllerSW.MAX_SPEED)
            commandedSpeedSlider.setSingleStep(1)
            x = round(self.frameGeometry().width()*0.5-commandedSpeedSlider.frameGeometry().width()*0.55)
            y = round(self.frameGeometry().height()*0.37)
            commandedSpeedSlider.move(x, y)
            commandedSpeedSlider.setParent(self)
            return commandedSpeedSlider

        def commandedSpeedSetup(self):
            commandedSpeed = QLabel()
            commandedSpeed.setFont(self.labelFont)

            if (self.TrainControllerSW.manualMode == True):
                commandedSpeed.setText(f'Commanded Speed:\n{str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.commandedSpeedManual)))} MPH')
            else:
                commandedSpeed.setText(f'Commanded Speed:\n{str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.inputs.commandedSpeed)))} MPH')
            
            commandedSpeed.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            commandedSpeed.setAlignment(Qt.AlignmentFlag.AlignCenter)
            commandedSpeed.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.08-commandedSpeed.frameGeometry().height()*0.5)
            commandedSpeed.move(x, y)
            commandedSpeed.setParent(self)
            return commandedSpeed

        def authoritySetup(self):
            authority = QLabel()    
            authority.setFont(self.labelFont)    
            authority.setText("Authority:\n" + str(self.TrainControllerSW.inputs.authority) + " Blocks")
            authority.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            authority.setAlignment(Qt.AlignmentFlag.AlignCenter)
            authority.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.21-authority.frameGeometry().height()*0.5)
            authority.move(x, y)
            authority.setParent(self)
            return authority

        def speedLimitSetup(self):
            speedLimit = QLabel()  
            speedLimit.setFont(self.labelFont)   
            speedLimit.setText("Speed Limit:\n" + str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.speedLimit))) + " MPH")
            speedLimit.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            speedLimit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            speedLimit.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.33-speedLimit.frameGeometry().height()*0.5)
            speedLimit.move(x, y)
            speedLimit.setParent(self)
            return speedLimit

        def temperatureSetup(self):
            temperature = QLabel()  
            temperature.setFont(self.labelFont)      
            temperature.setText("Temperature:\n" + str(float(self.TrainControllerSW.inputs.temperature)) + " F")
            temperature.setFixedSize(QSize(self.labelWidth, self.labelHeight))
            temperature.setAlignment(Qt.AlignmentFlag.AlignCenter)
            temperature.setWordWrap(True)
            x = round(self.frameGeometry().width()*0.65)
            y = round(self.frameGeometry().height()*0.46-temperature.frameGeometry().height()*0.5)
            temperature.move(x, y)
            temperature.setParent(self)
            return temperature

        def internalLightsStateSetup(self):
            internalLightsState = QLabel()   
            internalLightsState.setFont(self.labelFont)       
            internalLightsState.setText("Internal Lights: " + self.TrainControllerSW.getInternalLightsState())
            internalLightsState.setFixedSize(QSize(round(self.labelWidth*0.8), round(self.labelHeight*0.8)))
            internalLightsState.setWordWrap(True)
            internalLightsState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.18-internalLightsState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.25-internalLightsState.frameGeometry().height()*0.6)
            internalLightsState.move(x, y)
            internalLightsState.setParent(self)
            return internalLightsState

        def internalLightsEnableSetup(self):
            internalLightsEnable = QPushButton("Enable\nInternal Lights") 
            internalLightsEnable.setFont(self.buttonFont)     
            internalLightsEnable.setFixedSize(QSize(round(self.buttonWidth*0.6), self.buttonHeight))
            internalLightsEnable.clicked.connect(self.internalLightsEnableClick)
            x = round(self.frameGeometry().width()*0.18-internalLightsEnable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.3-internalLightsEnable.frameGeometry().height()*0.5)
            internalLightsEnable.move(x, y)
            internalLightsEnable.setParent(self)
            return internalLightsEnable

        def internalLightsDisableSetup(self):
            internalLightsDisable = QPushButton("Disable\nInternal Lights")      
            internalLightsDisable.setFont(self.buttonFont)      
            internalLightsDisable.setFixedSize(QSize(round(self.buttonWidth*0.6), self.buttonHeight))
            internalLightsDisable.clicked.connect(self.internalLightsDisableClick)
            x = round(self.frameGeometry().width()*0.18)
            y = round(self.frameGeometry().height()*0.3-internalLightsDisable.frameGeometry().height()*0.5)
            internalLightsDisable.move(x, y)
            internalLightsDisable.setParent(self)
            return internalLightsDisable

        def externalLightsStateSetup(self):
            externalLightsState = QLabel()
            externalLightsState.setFont(self.labelFont)
            externalLightsState.setText("External Lights: " + self.TrainControllerSW.getExternalLightsState())
            externalLightsState.setFixedSize(QSize(round(self.labelWidth*0.8), round(self.labelHeight*0.8)))
            externalLightsState.setWordWrap(True)
            externalLightsState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.18-externalLightsState.frameGeometry().width()*0.5)
            y = round(self.frameGeometry().height()*0.4-externalLightsState.frameGeometry().height()*0.6)
            externalLightsState.move(x, y)
            externalLightsState.setParent(self)
            return externalLightsState

        def externalLightsEnableSetup(self):
            externalLightsEnable = QPushButton("Enable\nExternal Lights")
            externalLightsEnable.setFont(self.buttonFont)
            externalLightsEnable.setFixedSize(QSize(round(self.buttonWidth*0.6), self.buttonHeight))
            externalLightsEnable.clicked.connect(self.externalLightsEnableClick)
            x = round(self.frameGeometry().width()*0.18-externalLightsEnable.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.45-externalLightsEnable.frameGeometry().height()*0.5)
            externalLightsEnable.move(x, y)
            externalLightsEnable.setParent(self)
            return externalLightsEnable

        def externalLightsDisableSetup(self):
            externalLightsDisable = QPushButton("Disable\nExternal Lights")    
            externalLightsDisable.setFont(self.buttonFont)     
            externalLightsDisable.setFixedSize(QSize(round(self.buttonWidth*0.6), self.buttonHeight))
            externalLightsDisable.clicked.connect(self.externalLightsDisableClick)
            x = round(self.frameGeometry().width()*0.18)
            y = round(self.frameGeometry().height()*0.45-externalLightsDisable.frameGeometry().height()*0.5)
            externalLightsDisable.move(x, y)
            externalLightsDisable.setParent(self)
            return externalLightsDisable
            
        def leftDoorStateSetup(self):
            leftDoorState = QLabel()
            leftDoorState.setFont(QFont(self.globalFont, 12))
            leftDoorState.setText("Left Door\n" + self.TrainControllerSW.getLeftDoorState())
            leftDoorState.setFixedSize(QSize(round(self.labelWidth*0.6), round(self.labelHeight*0.8)))
            leftDoorState.setWordWrap(True)
            leftDoorState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.18-leftDoorState.frameGeometry().width()*0.75)
            y = round(self.frameGeometry().height()*0.55-leftDoorState.frameGeometry().height()*0.6)
            leftDoorState.move(x, y)
            leftDoorState.setParent(self)
            return leftDoorState
             
        def leftDoorOpenSetup(self):
            leftDoorOpen = QPushButton("Open Doors")
            leftDoorOpen.setFont(self.buttonFont)
            leftDoorOpen.setFixedSize(QSize(round(self.buttonWidth*0.6), round(self.buttonHeight*0.5)))
            leftDoorOpen.clicked.connect(self.leftDoorOpenClick)
            x = round(self.frameGeometry().width()*0.18-leftDoorOpen.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.6-leftDoorOpen.frameGeometry().height()*0.5)
            leftDoorOpen.move(x, y)
            leftDoorOpen.setParent(self)
            return leftDoorOpen
        
        def leftDoorCloseSetup(self):
            leftDoorClose = QPushButton("Close Doors")
            leftDoorClose.setFont(self.buttonFont)
            leftDoorClose.setFixedSize(QSize(round(self.buttonWidth*0.6), round(self.buttonHeight*0.5)))
            leftDoorClose.clicked.connect(self.leftDoorCloseClick)
            x = round(self.frameGeometry().width()*0.18-leftDoorClose.frameGeometry().width())
            y = round(self.frameGeometry().height()*0.6+leftDoorClose.frameGeometry().height()*0.5)
            leftDoorClose.move(x, y)
            leftDoorClose.setParent(self)
            return leftDoorClose

        def rightDoorStateSetup(self):
            rightDoorState = QLabel()
            rightDoorState.setFont(QFont(self.globalFont, 12))
            rightDoorState.setText("Right Door\n" + self.TrainControllerSW.getRightDoorState())
            rightDoorState.setFixedSize(QSize(round(self.labelWidth*0.6), round(self.labelHeight*0.8)))
            rightDoorState.setWordWrap(True)
            rightDoorState.setAlignment(Qt.AlignmentFlag.AlignCenter)
            x = round(self.frameGeometry().width()*0.18-rightDoorState.frameGeometry().width()*0.25)
            y = round(self.frameGeometry().height()*0.55-rightDoorState.frameGeometry().height()*0.6)
            rightDoorState.move(x, y)
            rightDoorState.setParent(self)
            return rightDoorState
            
        def rightDoorOpenSetup(self):
            rightDoorOpen = QPushButton("Open Doors")
            rightDoorOpen.setFont(self.buttonFont)
            rightDoorOpen.setFixedSize(QSize(round(self.buttonWidth*0.6), round(self.buttonHeight*0.5)))
            rightDoorOpen.clicked.connect(self.rightDoorOpenClick)
            x = round(self.frameGeometry().width()*0.18)
            y = round(self.frameGeometry().height()*0.6-rightDoorOpen.frameGeometry().height()*0.5)
            rightDoorOpen.move(x, y)
            rightDoorOpen.setParent(self)
            return rightDoorOpen
        
        def rightDoorCloseSetup(self):
            rightDoorClose = QPushButton("Close Doors")
            rightDoorClose.setFont(self.buttonFont)
            rightDoorClose.setFixedSize(QSize(round(self.buttonWidth*0.6), round(self.buttonHeight*0.5)))
            rightDoorClose.clicked.connect(self.rightDoorCloseClick)
            x = round(self.frameGeometry().width()*0.18)
            y = round(self.frameGeometry().height()*0.6+rightDoorClose.frameGeometry().height()*0.5)
            rightDoorClose.move(x, y)
            rightDoorClose.setParent(self)
            return rightDoorClose
            

        # Event actions
        
        # Closes test UI if main window closes, minimizes if in main UI
        def closeEvent(self, event):
            if(self.testUI):
                if (self.TrainControllerTestUI):
                    self.TrainControllerTestUI.close()
            if(__name__ == "__main__"):
                self.close()
            else:
                self.setVisible(False)

        # Updates everything during every each loop of the timer 
        def mainEventLoop(self):
            self.TrainControllerSW.currentTime = self.TrainControllerSW.realTime
            self.TrainControllerSW.calculatePower()     
            self.TrainControllerSW.failureMode()

            # Only run in automatic mode
            if(self.TrainControllerSW.manualMode == False):
                self.TrainControllerSW.autoSetServiceBrake()
                self.TrainControllerSW.stayBelowSpeedLimitAndMaxSpeed()
                self.TrainControllerSW.autoUpdateDoorState()
                self.TrainControllerSW.autoUpdateLights()
            else:
                self.commandedSpeedSliderValueChanged()

            self.updateVisualElements()

            self.TrainControllerSW.writeOutputs()
            self.TrainControllerSW.previousTime = self.TrainControllerSW.realTime

        def updateVisualElements(self):
            self.realTimeClock.setText(f'Time: {self.TrainControllerSW.realTime.time()}'[:-7])

            if (self.TrainControllerSW.manualMode == False):
                self.commandedSpeedSlider.setEnabled(False)
                self.internalLightsEnable.setEnabled(False)
                self.internalLightsDisable.setEnabled(False)
                self.externalLightsEnable.setEnabled(False)
                self.externalLightsDisable.setEnabled(False)
                self.leftDoorOpen.setEnabled(False)
                self.leftDoorClose.setEnabled(False)
                self.rightDoorOpen.setEnabled(False)
                self.rightDoorClose.setEnabled(False)
                self.serviceBrakeEnable.setEnabled(False)
                self.serviceBrakeDisable.setEnabled(False)
            else:
                self.commandedSpeedSlider.setEnabled(True)
                self.internalLightsEnable.setEnabled(True)
                self.internalLightsDisable.setEnabled(True)
                self.externalLightsEnable.setEnabled(True)
                self.externalLightsDisable.setEnabled(True)
                self.leftDoorOpen.setEnabled(True)
                self.leftDoorClose.setEnabled(True)
                self.rightDoorOpen.setEnabled(True)
                self.rightDoorClose.setEnabled(True)
                self.serviceBrakeEnable.setEnabled(True)
                self.serviceBrakeDisable.setEnabled(True)

            if (self.TrainControllerSW.inputs.communicationsStatus == True):
                self.communicationsError.hide()
            else:
                self.communicationsError.show()

            if(self.TrainControllerSW.stationState == True):
                self.station.setText(f'Current Station:\n{self.TrainControllerSW.inputs.stationName}')
            else:
                self.station.setText(f'Next Station:\n{self.TrainControllerSW.inputs.nextStationName}')

            self.manualSpeedOverride.setText(f'Manual Mode: {"Enabled" if self.TrainControllerSW.manualMode else "Disabled"}')
            self.currentSpeed.setText("Current Speed: " + str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.inputs.currentSpeed))) + " MPH")
            self.engineState.setText("Engine State:\n" + self.TrainControllerSW.getEngineState())
            self.emergencyBrakeState.setText("Emergency Brake:\n" + self.TrainControllerSW.getEmergencyBrakeState())
            self.serviceBrakeState.setText("Service Brake:\n" + self.TrainControllerSW.getServiceBrakeState())
            
            if (self.TrainControllerSW.manualMode == True):
                self.commandedSpeed.setText(f'Commanded Speed:\n{str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.commandedSpeedManual)))} MPH')
            else:
                self.commandedSpeed.setText(f'Commanded Speed:\n{str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.inputs.commandedSpeed)))} MPH')
            
            self.authority.setText("Authority:\n" + str(self.TrainControllerSW.inputs.authority) + " Blocks")
            self.speedLimit.setText("Speed Limit:\n" + str(Conversions.metersPerSecondToMilesPerHour(float(self.TrainControllerSW.speedLimit))) + " MPH")
            self.temperature.setText("Temperature:\n" + str(float(self.TrainControllerSW.inputs.temperature)) + " F")
            self.internalLightsState.setText("Internal Lights: " + self.TrainControllerSW.getInternalLightsState())
            self.externalLightsState.setText("External Lights: " + self.TrainControllerSW.getExternalLightsState())
            self.leftDoorState.setText("Left Door\n" + self.TrainControllerSW.getLeftDoorState())
            self.rightDoorState.setText("Right Door\n" + self.TrainControllerSW.getRightDoorState())

        def manualModeToggleEvent(self):
            if (self.manualModeToggle.isChecked()):
                self.TrainControllerSW.manualMode = True
            else:
                self.TrainControllerSW.manualMode = False

        def kpTextChanged(self):
            try:
                self.TrainControllerSW.Kp = float(self.Kp.text())
            except:
                self.TrainControllerSW.Kp = self.TrainControllerSW.Kp

        def kiTextChanged(self):
            try:
                self.TrainControllerSW.Ki = float(self.Ki.text())
            except:
                self.TrainControllerSW.Ki = self.TrainControllerSW.Ki

        def emergencyBrakeEnableClick(self):
            self.TrainControllerSW.outputs.emergencyBrakeCommand = True
            TMTCSignals.emergencyBrakeCommandSignal.emit(self.TrainControllerSW.trainId, self.TrainControllerSW.outputs.emergencyBrakeCommand)

        def emergencyBrakeDisableClick(self):
            self.TrainControllerSW.outputs.emergencyBrakeCommand = False
            TMTCSignals.emergencyBrakeCommandSignal.emit(self.TrainControllerSW.trainId, self.TrainControllerSW.outputs.emergencyBrakeCommand)

        def serviceBrakeEnableClick(self):
            self.TrainControllerSW.outputs.serviceBrakeCommand = True

        def serviceBrakeDisableClick(self):
            self.TrainControllerSW.outputs.serviceBrakeCommand = False

        def commandedSpeedSliderValueChanged(self):
            self.TrainControllerSW.commandedSpeedManual = Conversions.kmPerHourToMetersPerSecond(self.commandedSpeedSlider.value())

        def internalLightsEnableClick(self):
            self.TrainControllerSW.outputs.internalLightCommand = True

        def internalLightsDisableClick(self):
            self.TrainControllerSW.outputs.internalLightCommand = False

        def externalLightsEnableClick(self):
            self.TrainControllerSW.outputs.externalLightCommand = True

        def externalLightsDisableClick(self):
            self.TrainControllerSW.outputs.externalLightCommand = False

        def leftDoorOpenClick(self):
            self.TrainControllerSW.outputs.leftDoorCommand = True
        
        def leftDoorCloseClick(self):
            self.TrainControllerSW.outputs.leftDoorCommand = False

        def rightDoorOpenClick(self):
            self.TrainControllerSW.outputs.rightDoorCommand = True

        def rightDoorCloseClick(self):
            self.TrainControllerSW.outputs.rightDoorCommand = False

# Class to create color widgets
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)



if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    mainWindow = MainWindow("Green", 2)
    mainWindow.show()

    if (mainWindow.testUI):
        mainWindow.TrainControllerTestUI.show()

    app.exec()