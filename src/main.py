# Main UI for all modules

import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), "Integration"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrainModel"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrainControllerSoftware"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrackModel"))


from TrainModelFolder import TrainModelMainUI, TrainModelTestUI
from TrainControllerSoftware import TrainControllerMainUI
from TrackModel import TrackModelMainUI, TrackModelTestUI, IntegrationTestUI
from Integration.TimeSignals import *
from Integration.TMTCSignals import *

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from datetime import *



# Class for the main window
class MainWindow(QMainWindow):
        TrainControllerList = []
        TrainModelList = []

        # Constructor 
        def __init__(self):
            super().__init__()

            #print(requests.get('https://w3schools.com/python/demopage.htm').text)

            # Main clock and simulation speed
            self.RTC = datetime.now() # Temporarily set time manually
            self.simulationSpeed = 1
            self.timerInterval = 100  
            rtcSignals.rtcSignal.connect(self.rtcSignalHandler) # Temporary for testing rtc

            # Set window defaults
            self.setWindowTitle(" ")
            self.setFixedSize(QSize(600, 600))
            self.move(600, 200)

            # Element sizing
            self.windowWidth = self.frameGeometry().width()
            self.windowHeight = self.frameGeometry().height()
            self.buttonWidth = round(0.2*self.windowWidth)
            self.buttonHeight = round(0.1*self.windowHeight)
            self.labelWidth = self.buttonWidth*1
            self.labelHeight = round(self.buttonHeight*0.5)

            # Styling
            self.globalFont = "Times New Roman"
            self.labelStyle = "background-color: rgb(180, 180, 180); border: 1px solid; border-color: rgb(0, 0, 0)"

            self.buttonStyle = ("QPushButton{background-color : rgb(180, 180, 180);}"
                                "QPushButton::pressed{background-color : rgb(200, 200, 200); color : rgb(70, 70, 70);}"
                                "QPushButton:hover!pressed{background-color : rgb(190, 190, 190);}"
                                )
            
            self.setStyleSheet("background-color: rgb(230, 230, 230);")    

            # Grid Layout
            self.mainWidget = QWidget()
            self.gridLayout = QGridLayout()
            self.waysideLayout = QGridLayout()
            self.waysideLayout.setSpacing(0)

            # Create elements
            self.mainThreadSetup()
            self.mainTimerSetup()
            self.HeaderLabelSetup()

            self.CTCLabelSetup()
            self.launchCTCSetup()

            self.WaysideControllerLabelSetup()
            self.launchWaysideControllerOneSetup()
            self.launchWaysideControllerTwoSetup()
            self.launchWaysideControllerThreeSetup()
            self.launchWaysideControllerFourSetup()
            
            self.TrackModelLabelSetup()
            self.launchTrackModelSetup()

            self.TrainModelLabelSetup()
            self.launchTrainModelSetup()
            self.selectTrainModelSetup()

            self.TrainControllerLabelSetup()
            self.launchTrainControllerSetup()
            self.selectTrainControllerSetup()

            # Add elements to grid layout
            self.gridLayout.addWidget(self.HeaderLabel, 0, 0, 1, 2, Qt.AlignmentFlag.AlignAbsolute)

            self.gridLayout.addWidget(self.CTCLabel, 1, 0, 1, 1)
            self.gridLayout.addWidget(self.launchCTC, 1, 1, 1, 1)

            self.gridLayout.addWidget(self.WaysideControllerLabel, 2, 0, 1, 1)
            self.waysideLayout.addWidget(self.launchWaysideControllerOne, 0, 0)
            self.waysideLayout.addWidget(self.launchWaysideControllerTwo, 0, 1)
            self.waysideLayout.addWidget(self.launchWaysideControllerThree, 1, 0)
            self.waysideLayout.addWidget(self.launchWaysideControllerFour, 1, 1)
            self.gridLayout.addLayout(self.waysideLayout, 2, 1, Qt.AlignmentFlag.AlignTop)
            
            self.gridLayout.addWidget(self.TrackModelLabel, 3, 0, 1, 1)
            self.gridLayout.addWidget(self.launchTrackModel, 3, 1, 1, 1)

            self.gridLayout.addWidget(self.TrainModelLabel, 4, 0, 1, 1)
            self.gridLayout.addWidget(self.launchTrainModel, 4, 1, 1, 1, Qt.AlignmentFlag.AlignTop)
            self.gridLayout.addWidget(self.selectTrainModel, 4, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

            self.gridLayout.addWidget(self.TrainControllerLabel, 5, 0, 1, 1)
            self.gridLayout.addWidget(self.launchTrainController, 5, 1, 1, 1, Qt.AlignmentFlag.AlignTop)
            self.gridLayout.addWidget(self.selectTrainController, 5, 1, 1, 1, Qt.AlignmentFlag.AlignBottom)

            self.mainWidget.setLayout(self.gridLayout)
            self.setCentralWidget(self.mainWidget)

            # Instantiate the Track Model
            self.TkM = TrackModelMainUI.TrackModelMainUI()

            # Test TM and TC
            for i in range(2, 4):
                self.trainDispatch(i)    
            self.TMTestUI = TrainModelTestUI.TrainModelTestUI() # temporary TM test UI 
            #self.TkMTestUI = TrackModelTestUI.TrackModelTestUI()
            self.TESTUI = IntegrationTestUI.BasicTestUI()
        
        # Widget Setups
        def mainThreadSetup(self):
            self.timerThread = QThread()
            self.timerThread.started.connect(self.mainTimerSetup)

        def mainTimerSetup(self):     
            mainTimer = QTimer()
            mainTimer.setInterval(self.timerInterval)
            mainTimer.timeout.connect(self.mainEventLoop)
            mainTimer.setParent(self)
            mainTimer.start()

        def HeaderLabelSetup(self):
            self.HeaderLabel = QLabel()
            self.HeaderLabel.setStyleSheet(self.labelStyle)     
            self.HeaderLabel.setFont(QFont(self.globalFont, 20))
            self.HeaderLabel.setText("Choo Choo - Trains Are My Passion")
            self.HeaderLabel.setFixedSize(QSize(round(self.labelWidth*3.2), round(self.labelHeight*2)))
            self.HeaderLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.HeaderLabel.setWordWrap(True)
            self.HeaderLabel.setParent(self)

        def CTCLabelSetup(self):
            self.CTCLabel = QLabel()
            self.CTCLabel.setStyleSheet(self.labelStyle)     
            self.CTCLabel.setFont(QFont(self.globalFont, 20))
            self.CTCLabel.setText("CTC")
            self.CTCLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            self.CTCLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.CTCLabel.setWordWrap(True)
            self.CTCLabel.setParent(self)

        def launchCTCSetup(self):
            self.launchCTC = QPushButton("Launch")
            self.launchCTC.setStyleSheet(self.buttonStyle)     
            self.launchCTC.setFont(QFont(self.globalFont, 20))
            self.launchCTC.setFixedSize(QSize(self.buttonWidth, self.buttonHeight))
            self.launchCTC.clicked.connect(self.launchCTCClick)
            self.launchCTC.setParent(self)

        def WaysideControllerLabelSetup(self):
            self.WaysideControllerLabel = QLabel()   
            self.WaysideControllerLabel.setStyleSheet(self.labelStyle)      
            self.WaysideControllerLabel.setFont(QFont(self.globalFont, 20))
            self.WaysideControllerLabel.setText("Wayside Controller")
            self.WaysideControllerLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            self.WaysideControllerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.WaysideControllerLabel.setWordWrap(True)
            self.WaysideControllerLabel.setParent(self)

        def launchWaysideControllerOneSetup(self):
            self.launchWaysideControllerOne = QPushButton("Launch\nGreen One")   
            self.launchWaysideControllerOne.setStyleSheet(self.buttonStyle)  
            self.launchWaysideControllerOne.setFont(QFont(self.globalFont, 9))
            self.launchWaysideControllerOne.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            self.launchWaysideControllerOne.clicked.connect(self.launchWaysideControllerOneClick)
            self.launchWaysideControllerOne.setParent(self)

        def launchWaysideControllerTwoSetup(self):
            self.launchWaysideControllerTwo = QPushButton("Launch\nGreen Two")   
            self.launchWaysideControllerTwo.setStyleSheet(self.buttonStyle)  
            self.launchWaysideControllerTwo.setFont(QFont(self.globalFont, 9))
            self.launchWaysideControllerTwo.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            self.launchWaysideControllerTwo.clicked.connect(self.launchWaysideControllerTwoClick)
            self.launchWaysideControllerTwo.setParent(self)

        def launchWaysideControllerThreeSetup(self):
            self.launchWaysideControllerThree = QPushButton("Launch\nRed One")   
            self.launchWaysideControllerThree.setStyleSheet(self.buttonStyle)  
            self.launchWaysideControllerThree.setFont(QFont(self.globalFont, 9))
            self.launchWaysideControllerThree.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            self.launchWaysideControllerThree.clicked.connect(self.launchWaysideControllerThreeClick)
            self.launchWaysideControllerThree.setParent(self)

        def launchWaysideControllerFourSetup(self):
            self.launchWaysideControllerFour = QPushButton("Launch\nRed Two")   
            self.launchWaysideControllerFour.setStyleSheet(self.buttonStyle)  
            self.launchWaysideControllerFour.setFont(QFont(self.globalFont, 9))
            self.launchWaysideControllerFour.setFixedSize(QSize(round(self.buttonWidth*0.5), round(self.buttonHeight*0.5)))
            self.launchWaysideControllerFour.clicked.connect(self.launchWaysideControllerFourClick)
            self.launchWaysideControllerFour.setParent(self)

        def TrackModelLabelSetup(self):
            self.TrackModelLabel = QLabel()         
            self.TrackModelLabel.setStyleSheet(self.labelStyle)
            self.TrackModelLabel.setFont(QFont(self.globalFont, 20))
            self.TrackModelLabel.setText("Track Model")
            self.TrackModelLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            self.TrackModelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.TrackModelLabel.setWordWrap(True)
            self.TrackModelLabel.setParent(self)

        def launchTrackModelSetup(self):
            self.launchTrackModel = QPushButton("Launch")   
            self.launchTrackModel.setStyleSheet(self.buttonStyle)  
            self.launchTrackModel.setFont(QFont(self.globalFont, 20))
            self.launchTrackModel.setFixedSize(QSize(self.buttonWidth, round(self.buttonHeight)))
            self.launchTrackModel.clicked.connect(self.launchTrackModelClick)
            self.launchTrackModel.setParent(self)

        def TrainModelLabelSetup(self):
            self.TrainModelLabel = QLabel()   
            self.TrainModelLabel.setStyleSheet(self.labelStyle)      
            self.TrainModelLabel.setFont(QFont(self.globalFont, 20))
            self.TrainModelLabel.setText("Train Model")
            self.TrainModelLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            self.TrainModelLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.TrainModelLabel.setWordWrap(True)
            self.TrainModelLabel.setParent(self)

        def launchTrainModelSetup(self):
            self.launchTrainModel = QPushButton("Launch")   
            self.launchTrainModel.setStyleSheet(self.buttonStyle)  
            self.launchTrainModel.setFont(QFont(self.globalFont, 20))
            self.launchTrainModel.setFixedSize(QSize(self.buttonWidth, round(self.buttonHeight*0.5)))
            self.launchTrainModel.clicked.connect(self.launchTrainModelClick)
            self.launchTrainModel.setParent(self)

        def selectTrainModelSetup(self):
            self.selectTrainModel = QComboBox()
            self.selectTrainModel.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight*0.5)))       

        def TrainControllerLabelSetup(self):
            self.TrainControllerLabel = QLabel()   
            self.TrainControllerLabel.setStyleSheet(self.labelStyle)      
            self.TrainControllerLabel.setFont(QFont(self.globalFont, 20))
            self.TrainControllerLabel.setText("Train Controller")
            self.TrainControllerLabel.setFixedSize(QSize(round(self.labelWidth*1.6), round(self.labelHeight*2)))
            self.TrainControllerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.TrainControllerLabel.setWordWrap(True)
            self.TrainControllerLabel.setParent(self) 

        def launchTrainControllerSetup(self):
            self.launchTrainController = QPushButton("Launch")   
            self.launchTrainController.setStyleSheet(self.buttonStyle)  
            self.launchTrainController.setFont(QFont(self.globalFont, 20))
            self.launchTrainController.setFixedSize(QSize(self.buttonWidth, round(self.buttonHeight*0.5)))
            self.launchTrainController.clicked.connect(self.launchTrainControllerClick)
            self.launchTrainController.setParent(self)

        def selectTrainControllerSetup(self):
            self.selectTrainController = QComboBox()
            self.selectTrainController.setFixedSize(QSize(round(self.buttonWidth), round(self.buttonHeight*0.5)))
            
            

        # Events

        # Close all windows when closing main UI
        def closeEvent(self, event):
            for TC in self.TrainControllerList:
                TC.close()

            for TM in self.TrainModelList:
                TM.close()

            self.TMTestUI.close()

        # Runs all functions during each time interval
        def mainEventLoop(self):
            self.getRTC()

        def launchCTCClick(self):
             print("CTC")

        def launchWaysideControllerOneClick(self):
            print("Wayside Controller One")

        def launchWaysideControllerTwoClick(self):
            print("Wayside Controller Two")

        def launchWaysideControllerThreeClick(self):
            print("Wayside Controller Three")

        def launchWaysideControllerFourClick(self):
            print("Wayside Controller Four")

        def launchTrackModelClick(self):
            self.TkM.setVisible(True)

        def launchTrainModelClick(self):
             if(len(self.TrainModelList) > 0):
                self.TrainModelList[int(self.selectTrainModel.currentIndex())].setVisible(True)

        def launchTrainControllerClick(self):
             if(len(self.TrainControllerList) > 0):
                self.TrainControllerList[int(self.selectTrainController.currentIndex())].setVisible(True)

        # Get time from CTC module
        def getRTC(self):
            self.RTC = self.RTC + timedelta(0, 0, 0, self.timerInterval*self.simulationSpeed) # Temporary increment time
            rtcSignals.rtcSignal.emit(self.RTC.isoformat() + "0-05:00")

        # Test setups for testing TM and TC
        def trainDispatch(self, trainId):
            self.TrainControllerList.append(TrainControllerMainUI.MainWindow(trainId))
            self.TrainModelList.append(TrainModelMainUI.TrainModelUI(trainId, "Green"))
            self.TkM.backEnd.newTrainMade(trainId, "Green")
            self.TrainControllerList[len(self.TrainControllerList)-1].move(800, 10)
            self.TrainModelList[len(self.TrainModelList)-1].move(self.screen().availableGeometry().width()-1480, 
                                                                 self.screen().availableGeometry().height()-self.TrainModelList[len(self.TrainModelList)-1].frameGeometry().height()-40)

            # Update TM and TC selectors
            self.selectTrainModel.addItems([str(trainId)])
            self.selectTrainController.addItems([str(trainId)])

        def rtcSignalHandler(self, rtc):
            #print(rtc)
            test=1
            



# Start application
app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

# Temporary
#mainWindow.TMTestUI.showMinimized()
#mainWindow.TkMTestUI.showMinimized()
mainWindow.TESTUI.show()

app.exec() 