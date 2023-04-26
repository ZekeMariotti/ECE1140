# Main UI for all modules

import sys
import os
import requests
import subprocess
import json
import webbrowser

sys.path.append(os.path.join(os.path.dirname(__file__), "Integration"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrainModel"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrainControllerSoftware"))
sys.path.append(os.path.join(os.path.dirname(__file__), "TrackModel"))



from TrainModelFolder import TrainModelMainUI, TrainModelTestUI
from TrainControllerSoftware import TrainControllerMainUI
from TrackModel import TrackModelMainUI, TrackModelTestUI, IntegrationTestUI
from WaysideController import NewGreenLine,NewGreenLine2,GreenLineTestUi,NewRedLine,NewRedLine2,RedLineTestUI
from Integration import sendJsonToArduinoClass, receiveJsonFromArduinoClass
from Integration.TimeSignals import *
from Integration.TMTCSignals import *
from Integration.ActiveSignals import *

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

            #self.ctcBackendThread = QThread()
            #self.ctcBackendThread.started.connect(self.ctcBackend)
            #self.ctcBackendThread.start()

            # Main clock and simulation speed
            self.RTC = datetime.now()
            self.simulationSpeed = 1
            self.timerInterval = 100  

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

            # Sub Thread Setup
            pool = QThreadPool.globalInstance()

            # sendJson = sendJsonToArduinoClass.jsonToArduino()
            # pool.start(sendJson)

            # fromArduino = receiveJsonFromArduinoClass.arduinoToJson()
            # pool.start(fromArduino)

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

            # Instantiate Wayside Controllers
            self.wc = NewGreenLine.MainWindow("GreenLine 1")
            self.wc2 = NewGreenLine2.MainWindow("GreenLine 2")
            self.wc3 = NewRedLine.MainWindowR("RedLine 1")
            self.wc4 = NewRedLine2.MainWindowR("RedLine 2")
            activeSignals.activeSignal.emit()

            # Test TM and TC    
            #self.trainDispatch(2, "Green")

            #self.TkMTestUI = TrackModelTestUI.TrackModelTestUI()
            #self.TESTUI = IntegrationTestUI.BasicTestUI()
            #self.TESTUI = GreenLineTestUi.TestWindow()
        
        # Widget Setups
        def mainThreadSetup(self):
            self.timerThread = QThread()
            self.timerThread.started.connect(self.mainTimerSetup)

        def ctcBackend(self):
            self.ctcBackendProcess = subprocess.Popen(f'{sys.path[0]}\..\executables\ctcbackend\main.exe', shell=False)

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
            try:
                self.ctcBackendProcess.terminate()
                self.ctcBackendProcess.wait()
            except Exception as ex:
                print(ex)

            for TC in self.TrainControllerList:
                TC.close()

            for TM in self.TrainModelList:
                TM.close()

            #self.TMTestUI.close()
            self.wc.close()
            self.TkM.close()

            sys.exit()

        # Runs all functions during each time interval
        def mainEventLoop(self):
            self.getRTC()
            self.trainDispatchCall()

        def launchCTCClick(self):
            webbrowser.get("windows-default").open_new("http://localhost")
            print("CTC")

        def launchWaysideControllerOneClick(self):
            self.wc.setVisible(True)
            #self.wc.WaysideControllerGreenTestUI.show()
            activeSignals.activeSignal.emit()

        def launchWaysideControllerTwoClick(self):
            self.wc2.setVisible(True)
            activeSignals.activeSignal.emit()

        def launchWaysideControllerThreeClick(self):
            self.wc3.setVisible(True)
            #self.wc3.WaysideControllerRedTestUI.show()
            activeSignals.activeSignal.emit()            

        def launchWaysideControllerFourClick(self):
            self.wc4.setVisible(True)
            activeSignals.activeSignal.emit()

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
            rtcInput = requests.get('http://localhost:8090/api/simulation/time').text.replace("\"", "")
            
            if(len(rtcInput) < 33):
                while(len(rtcInput) != 33):
                    rtcInput = rtcInput[:-6] + '0' + rtcInput[-6:]

            # if no ".", don't emit signal
            if("." in rtcInput):
                rtcSignals.rtcSignal.emit(rtcInput)
                rtcInput = stringRemove(rtcInput, 26)
                self.RTC = datetime.strptime(rtcInput, "%Y-%m-%dT%H:%M:%S.%f%z")   
            

        # Test setups for testing TM and TC
        def trainDispatch(self, trainId, line):
            # trainId of 1 corresponds with train controller hardware
            if(trainId != 1):
                self.TrainControllerList.append(TrainControllerMainUI.MainWindow(line, trainId))
                self.TrainModelList.append(TrainModelMainUI.TrainModelUI(trainId, line))
                self.TkM.backEnd.newTrainMade(trainId, line)
                self.TrainControllerList[len(self.TrainControllerList)-1].move(800, 10)
                self.TrainModelList[len(self.TrainModelList)-1].move(self.screen().availableGeometry().width()-1480, 
                                                                    self.screen().availableGeometry().height()-self.TrainModelList[len(self.TrainModelList)-1].frameGeometry().height()-40)

                # Update TM and TC selectors
                self.selectTrainModel.addItems([str(trainId)])
                self.selectTrainController.addItems([str(trainId)])
            else:
                # Sub Thread Setup
                self.hwtcCreated = True
                pool = QThreadPool.globalInstance()

                sendJson = sendJsonToArduinoClass.jsonToArduino()
                pool.start(sendJson)

                fromArduino = receiveJsonFromArduinoClass.arduinoToJson()
                pool.start(fromArduino)

                self.TrainModelList.append(TrainModelMainUI.TrainModelUI(trainId, line))
                self.TkM.backEnd.newTrainMade(trainId, line)
                self.TrainModelList[len(self.TrainModelList)-1].move(self.screen().availableGeometry().width()-1480, 
                                                                    self.screen().availableGeometry().height()-self.TrainModelList[len(self.TrainModelList)-1].frameGeometry().height()-40)
                self.selectTrainModel.addItems([str(trainId)])
            
        def trainDispatchCall(self):
            test = requests.get('http://localhost:8090/api/dispatchedtrain').text
            if(test!="\"\""):
                jsonTest = json.loads(test)
                if(jsonTest["id"] != 1):
                    self.trainDispatch(jsonTest["id"], jsonTest["line"])

# Function to remove character from a string at nth position
def stringRemove(string, n):  
    first = string[: n]   
    last = string[n+1:]  
    return first + last
            


def main():
    # Start application
    app = QApplication(sys.argv)
    #exec(open("\Integration\\receiveJsonFromArduino.py").read())
    #exec(open(os.path.join(sys.path[0], "Integration", "receiveJsonFromArduino.py")).read())
    #os.system("python" + os.path.join(sys.path[0], "Integration", "receiveJsonFromArduino.py"))
    #subprocess.Popen(['python', os.path.join(sys.path[0], "Integration", "receiveJsonFromArduino.py")])
    #subprocess.Popen(['python', os.path.join(sys.path[0], "Integration", "sendJsonToArduino.py")])


    mainWindow = MainWindow()
    mainWindow.show()

    # Temporary
    #mainWindow.TMTestUI.showMinimized()
    #mainWindow.TkMTestUI.showMinimized()
    #mainWindow.TESTUI.show()

    app.exec() 


# Run main
if (__name__ == "__main__"):
    main()
        