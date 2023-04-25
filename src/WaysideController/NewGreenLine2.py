import sys
import os
sys.path.append(__file__.replace("/WaysideController/NewGreenLine.py", ""))

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from Integration.TkMWCSignals import *
from Integration.ActiveSignals import *
from WaysideController.TestGenericWayside import Wayside
from WaysideController.GreenLineTestUi import TestWindow
from WaysideController.PLC import PLC
from WaysideController.NewGreenLine import *
#global variables

rowheaders =["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
colheaders =["0","1","2","3","4","5","6","7","8","9"]
rowheaders2 =["10","11","12","13","14","15"]
    
class Worker(QObject):
      finished = pyqtSignal()

class MainWindow(QMainWindow):
    def __init__(self,name):

        super().__init__()

        #Intialize Wayside class
        #No longer needed so communication can be simulated
        #self.WaysideControllerGreen = Wayside(1,True)
        #self.WaysideControllerGreen2 = Wayside(1,True)
        #self.File1 = "C:\\Systems and Progect Engineering\ECE1140-1\src\waysideController\GreenLine.txt"
        #self.File2 = "C:\\Systems and Progect Engineering\ECE1140-1\src\waysideController\GreenLine2.txt"
        self.File1 = os.path.join(sys.path[0], "WaysideController", "GreenLine.txt")
        self.File2 = os.path.join(sys.path[0], "WaysideController", "GreenLine2.txt")
        self.blocks1 =101
        self.blocks2 =151
        self.name = name
        self.TestUI = True
        self.active = False
        activeSignals.activeSignal.connect(self.activeSignal)
        TkMWCSignals.failureSignal.connect(self.brokenRailHandler)
        TkMWCSignals.stopSignal.connect(self.errorHandler)
        TkMWCSignals.currBlockSignal.connect(self.currBlockHandler)
        #Window

        self.setWindowTitle(str(self.name))
        self.setMinimumSize(1100,650)
        self.move(0,0)
        self.windowWidth = self.frameGeometry().width()
        self.windowHeight = self.frameGeometry().height()
        self.buttonWidth = round(0.07*self.windowWidth)
        self.buttonHeight = round(0.06*self.windowHeight)
        self.labelWidth = self.buttonWidth*2
        self.labelHeight = round(self.buttonHeight*1.3)
        self.globalFont = "Times New Roman"
        self.labelFont = QFont(self.globalFont,12)
        self.titleFont = QFont(self.globalFont,16)
        
        self.mainTimer = self.mainTimerSetup()
        #Commanded Speed
        self.CommandedSpeedLabel = self.CommandedSpeedLabelSetup()
        self.CommandedSpeed = self.CommandedSpeedSetup()

        #Authority
        self.AuthorityLabel = self.AuthorityLabelSetup()
        self.Authority = self.AuthoritySetup()
        
        #Signal Color
        self.ColorLabel = self.ColorLabelSetup()
        self.SignalLight = self.SignalLightSetup()

        #Broken Rail
        self.RailLabel = self.RailLabelSetup()
        self.BrokenRail = self.BrokenRailSetup()

        #Occupancy
        self.OccupancyLabel = self.OccupancyLabelSetup()
        self.Occupancy = self.OccupancySetup()

        #Switch Labels
        self.SwitchTitle = self.MainSwitchLabel()
        self.Switches = self.SwitchLabels()

        #Buttons to edit Switch State
        self.Switch1BL = self.Switch1ButtonL()
        self.Switch1BR = self.Switch1ButtonR()
        self.Switch2BL = self.Switch2ButtonL()
        self.Switch2BR = self.Switch2ButtonR()
        self.Switch3BL = self.Switch3ButtonL()
        self.Switch3BR = self.Switch3ButtonR()
        self.Switch4BL = self.Switch4ButtonL()
        self.Switch4BR = self.Switch4ButtonR()
        self.Switch5BL = self.Switch5ButtonL()
        self.Switch5BR = self.Switch5ButtonR()
        self.Switch6BL = self.Switch6ButtonL()
        self.Switch6BR = self.Switch6ButtonR()
        #Switch Outputs
        self.Switch1Out = self.Switch1OutSetup()
        self.Switch2Out = self.Switch2OutSetup()
        self.Switch3Out = self.Switch3OutSetup()
        self.Switch4Out = self.Switch4OutSetup()
        self.Switch5Out = self.Switch5OutSetup()
        self.Switch6Out = self.Switch6OutSetup()

        #Gate
        self.GateLabel = self.GateLabelSetup()
        self.Gate = self.GateSetup()
        self.Up = self.GateUp()
        self.Down = self.GateDown()

        #PLC
        self.PLCLabel = self.PLCLabelSetup()
        self.PLC = self.PLCButton()
        ##Maintenance
        self.maintenanceMode = False
        self.maintenanceButton = self.maintenanceButtonSetup()
        self.maintenanceLabel = self.maintenanceLabelSetup()
        #Test UI
        if self.TestUI :
              self.WaysideControllerGreenTestUI = TestWindow(WaysideControllerGreen,WaysideControllerGreen2)
        #widget setups
    def mainThreadSetup(self):
          self.timerThread = QThread()
          self.timerThread.started.connect(self.mainTimerSetup)

    def mainTimerSetup(self):
          mainTimer = QTimer()
          mainTimer.setInterval(100)
          mainTimer.timeout.connect(self.mainEventLoop)
          mainTimer.setParent(self)
          mainTimer.start()
          return(mainTimer)
    
                #Commanded Speed Functions
    def activeSignal(self):
         self.active = True

    def CommandedSpeedLabelSetup(self):
            CommandedLabel = QLabel()
            CommandedLabel.setFont(self.titleFont)
            CommandedLabel.setText("Commanded Speed (MPH)")
            CommandedLabel.setFixedSize(QSize(230,25))
            CommandedLabel.move(450,0)
            CommandedLabel.setParent(self)
            return(CommandedLabel)
    
    def CommandedSpeedSetup(self):
            CommandedSpeed = QTableWidget()
            CommandedSpeed.setFont(self.labelFont)
            CommandedSpeed.setFixedSize(QSize(int(round(0.6*self.windowWidth)),int(round(0.12*self.windowHeight))))
            CommandedSpeed.setColumnCount(10)
            CommandedSpeed.setRowCount(6)
            CommandedSpeed.setVerticalHeaderLabels(rowheaders2)
            CommandedSpeed.setHorizontalHeaderLabels(colheaders)
            CommandedSpeed.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(self.blocks1,self.blocks2):
                value=WaysideControllerGreen2.commandedSpeed[k]
                CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(151,160):
                CommandedSpeed.setItem(15,j,QTableWidgetItem("-"))
                j=j+1
            CommandedSpeed.setParent(self)
            CommandedSpeed.move(0,50)
            return(CommandedSpeed)
    
                #Authority Functions

    def AuthorityLabelSetup(self):
          AuthorityLabel = QLabel()
          AuthorityLabel.setFont(self.titleFont)
          AuthorityLabel.setText("Authority (Blocks)")
          AuthorityLabel.setFixedSize(QSize(230,25))
          AuthorityLabel.move(480,140)
          AuthorityLabel.setParent(self)
          return(AuthorityLabel)
    
    def AuthoritySetup(self):
            Authority = QTableWidget()
            Authority.setFont(self.labelFont)
            Authority.setFixedSize(QSize(int(round(0.6*self.windowWidth)),int(round(0.12*self.windowHeight))))
            Authority.setColumnCount(10)
            Authority.setRowCount(6)
            Authority.setVerticalHeaderLabels(rowheaders2)
            Authority.setHorizontalHeaderLabels(colheaders)
            Authority.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(self.blocks1,self.blocks2):
                value=WaysideControllerGreen2.authority[k]
                Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            #value=WaysideControllerGreen2.authority[150]
            Authority.setItem(15,0,QTableWidgetItem(str(value)))
            for k in range(151,160):
                Authority.setItem(6,j,QTableWidgetItem("-"))
                j=j+1            
            Authority.setParent(self)
            Authority.move(0,170)
            return(Authority)
    
                #Broken Rail Functions

    def RailLabelSetup(self):
          RailLabel = QLabel()
          RailLabel.setFont(self.titleFont)
          RailLabel.setText("Broken Rail")
          RailLabel.setFixedSize(QSize(230,25))
          RailLabel.move(500,250)
          RailLabel.setParent(self)
          return(RailLabel)
    
    def BrokenRailSetup(self):
            BrokenRail = QTableWidget()
            BrokenRail.setFont(self.labelFont)
            BrokenRail.setFixedSize(QSize(int(round(0.6*self.windowWidth)),int(round(0.12*self.windowHeight))))
            BrokenRail.setColumnCount(10)
            BrokenRail.setRowCount(6)
            BrokenRail.setVerticalHeaderLabels(rowheaders2)
            BrokenRail.setHorizontalHeaderLabels(colheaders)
            BrokenRail.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(self.blocks1,self.blocks2):
                if WaysideControllerGreen2.brokenRail[k] == True:
                    value="ERROR"
                else:
                    value=" "
                BrokenRail.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
                BrokenRail.setItem(15,j,QTableWidgetItem("-"))
                j=j+1
            BrokenRail.setParent(self)
            BrokenRail.move(0,290)
            return(BrokenRail)
    
                # Signal Light Functions

    def ColorLabelSetup(self):
          ColorLabel = QLabel()
          ColorLabel.setFont(self.titleFont)
          ColorLabel.setText("Signal Color (G/R)")
          ColorLabel.setFixedSize(QSize(230,25))
          ColorLabel.setParent(self)
          ColorLabel.move(470,380)
          return(ColorLabel)
    
    def SignalLightSetup(self):
            SignalLight = QTableWidget()
            SignalLight.setFont(self.labelFont)
            SignalLight.setFixedSize(QSize(int(round(0.6*self.windowWidth)),int(round(0.12*self.windowHeight))))
            SignalLight.setColumnCount(10)
            SignalLight.setRowCount(6)
            SignalLight.setVerticalHeaderLabels(rowheaders2)
            SignalLight.setHorizontalHeaderLabels(colheaders)
            SignalLight.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(self.blocks1,self.blocks2):
                if WaysideControllerGreen2.signalLights[k]==True:
                  value="G"
                else:
                  value="R"
                if(k==101 or k==150):
                  SignalLight.setItem(i,j,QTableWidgetItem((value)))
                else:
                  SignalLight.setItem(i,j,QTableWidgetItem((" ")))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
                SignalLight.setItem(15,j,QTableWidgetItem("-"))
                j=j+1            
            SignalLight.setParent(self)
            SignalLight.move(0,420)
            return(SignalLight)
            
                    #Occupancy Functions
                    
    def OccupancyLabelSetup(self):
          OccupancyLabel = QLabel()
          OccupancyLabel.setFont(self.titleFont)
          OccupancyLabel.setText("Occupancy")
          OccupancyLabel.setFixedSize(QSize(230,25))
          OccupancyLabel.move(500,510)
          OccupancyLabel.setParent(self)
          return(OccupancyLabel)  
            
    def OccupancySetup(self):
            Occupancy = QTableWidget()
            Occupancy.setFont(self.labelFont)
            Occupancy.setFixedSize(QSize(int(round(0.6*self.windowWidth)),int(round(0.12*self.windowHeight))))
            Occupancy.setColumnCount(10)
            Occupancy.setRowCount(6)
            Occupancy.setVerticalHeaderLabels(rowheaders2)
            Occupancy.setHorizontalHeaderLabels(colheaders)
            Occupancy.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(self.blocks1,self.blocks2):
                if WaysideControllerGreen2.occupancy[k]==True:
                  value="X"
                else:
                  value=" "
              
                Occupancy.setItem(i,j,QTableWidgetItem((value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
                Occupancy.setItem(5,j,QTableWidgetItem("-"))
                j=j+1            
            Occupancy.setParent(self)
            Occupancy.move(int(round(0.0*self.windowWidth)),int(round(0.85*self.windowHeight)))
            return(Occupancy)
    
                    #Gate Functions

    def GateLabelSetup(self):
          GateLabel = QLabel()
          GateLabel.setFont(self.titleFont)
          GateLabel.setText("Gate State")
          GateLabel.move(int(round(0.85*self.windowWidth)),int(round(0.45*self.windowHeight)))
          GateLabel.setParent(self)
          return(GateLabel)  
    
    def GateSetup(self):
            gate = QLabel()
            gate.setFont(self.labelFont)

            if WaysideControllerGreen2.gates[1] == True:
                gate.setText("Block 19 Gate:  UP")

            else:
                gate.setText("Block 19 Gate:  DOWN")

            gate.move(int(round(0.85*self.windowWidth)),int(round(0.55*self.windowHeight)))
            gate.setParent(self)
            return(gate)

                    #Switch Functions

    def GateUp(self):
          Up = QPushButton("Up")
          Up.setFont(self.labelFont) 
          Up.setFixedSize(QSize(self.buttonWidth,self.buttonHeight))  
          Up.clicked.connect(self.UpClicked)
          Up.setParent(self)
          Up.move(int(round(0.7*self.windowWidth)),int(round(0.8*self.windowHeight)))
          return(Up)

    def GateDown(self):
          Down = QPushButton("Down")
          Down.setFont(self.labelFont) 
          Down.setFixedSize(QSize(self.buttonWidth,self.buttonHeight))  
          Down.clicked.connect(self.DownClicked)
          Down.setParent(self)
          Down.move(int(round(0.7*self.windowWidth)),int(round(0.9*self.windowHeight)))
          return(Down)
    
    def maintenanceButtonSetup(self):
          Man = QPushButton("Maintenance")
          Man.setFont(self.labelFont)
          Man.setFixedSize(QSize(90,40))
          Man.clicked.connect(self.maintenance)
          Man.setParent(self)
          Man.move(1000,0)
          return(Man)
    
    def MainSwitchLabel(self):
          MainSwitchLabel = QLabel()
          MainSwitchLabel.setFont(self.titleFont)
          MainSwitchLabel.setText("Switches")
          MainSwitchLabel.setFixedSize(QSize(80,20))
          MainSwitchLabel.setParent(self)
          MainSwitchLabel.move(830,20)
          return(MainSwitchLabel)
    
    def SwitchLabels(self):
          Switch1Label = QLabel()
          Switch1Label.setFont(self.labelFont)
          Switch1Label.setText("\nSwitch 1\n\n\nSwitch 2\n\n\nSwitch 3\n\n\nSwitch 4\n\n\nSwitch 5\n\n\nSwitch 6") 
          Switch1Label.setParent(self)
          Switch1Label.move(int(round(0.62*self.windowWidth)),int(round(-0.05*self.windowHeight)))
          return(Switch1Label)
      
    def Switch1ButtonL(self):
          Push1L = QPushButton("1 to 13")
          Push1L.setFont(self.labelFont) 
          Push1L.setFixedSize(QSize(70,40))  
          Push1L.clicked.connect(self.Switch1ButtonLClick)
          Push1L.setParent(self)
          Push1L.move(780,55)
          return(Push1L)
    
    def Switch1ButtonR(self):
          Push1R = QPushButton("12 to 13")
          Push1R.setFont(self.labelFont) 
          Push1R.setFixedSize(QSize(70,40))  
          Push1R.clicked.connect(self.Switch1ButtonRClick)
          Push1R.setParent(self)
          Push1R.move(850,55)
          return(Push1R)
    
    def Switch2ButtonL(self):
          Push2L = QPushButton("29 to 150")
          Push2L.setFont(self.labelFont) 
          Push2L.setFixedSize(QSize(70,40))  
          Push2L.clicked.connect(self.Switch2ButtonLClick)
          Push2L.setParent(self)
          Push2L.move(780,110)
          return(Push2L)
    
    def Switch2ButtonR(self):
          Push2R = QPushButton("29 to 30")
          Push2R.setFont(self.labelFont) 
          Push2R.setFixedSize(QSize(70,40))  
          Push2R.clicked.connect(self.Switch2ButtonRClick)
          Push2R.setParent(self)
          Push2R.move(850,110)
          return(Push2R)
    
    def Switch3ButtonL(self):
          Push3L = QPushButton("57 to Yard")
          Push3L.setFont(self.labelFont) 
          Push3L.setFixedSize(QSize(70,40))  
          Push3L.clicked.connect(self.Switch3ButtonLClick)
          Push3L.setParent(self)
          Push3L.move(780,165)
          return(Push3L)
    
    def Switch3ButtonR(self):
          Push3R = QPushButton("57 to 58")
          Push3R.setFont(self.labelFont) 
          Push3R.setFixedSize(QSize(70,40))  
          Push3R.clicked.connect(self.Switch3ButtonRClick)
          Push3R.setParent(self)
          Push3R.move(850,165)
          return(Push3R)

    def Switch4ButtonL(self):
          Push4L = QPushButton("Yard to 63")
          Push4L.setFont(self.labelFont) 
          Push4L.setFixedSize(QSize(70,40))  
          Push4L.clicked.connect(self.Switch4ButtonLClick)
          Push4L.setParent(self)
          Push4L.move(780,220)
          return(Push4L)
    
    def Switch4ButtonR(self):
          Push4R = QPushButton("62 to 63")
          Push4R.setFont(self.labelFont) 
          Push4R.setFixedSize(QSize(70,40))  
          Push4R.clicked.connect(self.Switch4ButtonRClick)
          Push4R.setParent(self)
          Push4R.move(850,220)
          return(Push4R)
    
    def Switch5ButtonL(self):
          Push5L = QPushButton("77 to 101")
          Push5L.setFont(self.labelFont) 
          Push5L.setFixedSize(QSize(70,40))  
          Push5L.clicked.connect(self.Switch5ButtonLClick)
          Push5L.setParent(self)
          Push5L.move(780,280)
          return(Push5L)
    
    def Switch5ButtonR(self):
          Push5R = QPushButton("76 to 77")
          Push5R.setFont(self.labelFont) 
          Push5R.setFixedSize(QSize(70,40))  
          Push5R.clicked.connect(self.Switch5ButtonRClick)
          Push5R.setParent(self)
          Push5R.move(850,280)
          return(Push5R)
    
    def Switch6ButtonL(self):
          Push6L = QPushButton("85 to 100")
          Push6L.setFont(self.labelFont) 
          Push6L.setFixedSize(QSize(70,40))  
          Push6L.clicked.connect(self.Switch6ButtonLClick)
          Push6L.setParent(self)
          Push6L.move(780,330)
          return(Push6L)
    
    def Switch6ButtonR(self):
          Push6R = QPushButton("85 to 86")
          Push6R.setFont(self.labelFont) 
          Push6R.setFixedSize(QSize(70,40))  
          Push6R.clicked.connect(self.Switch6ButtonRClick)
          Push6R.setParent(self)
          Push6R.move(850,330)
          return(Push6R)
    def Switch1OutSetup(self):
          Output1 = QLabel()
          Output1.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[1]==True:
                Output1.setText("1 to 13")
          else:
                Output1.setText("12 to 13")

          Output1.setParent(self)
          Output1.move(1000,-165)
          return(Output1)
    
    def Switch2OutSetup(self):
          Output2 = QLabel()
          Output2.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[2]==True:
                Output2.setText("29 to 150")
          else:
                Output2.setText("29 to 30")

          Output2.setParent(self)
          Output2.move(1000,-115)
          return(Output2)

    def Switch3OutSetup(self):
          Output3 = QLabel()
          Output3.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[3]==True:
                Output3.setText("57 to Yard")
          else:
                Output3.setText("57 to 58")

          Output3.setParent(self)
          Output3.move(1000,-60)
          return(Output3)

    def Switch4OutSetup(self):
          Output4 = QLabel()
          Output4.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[4]==True:
                Output4.setText("Yard to 63")
          else:
                Output4.setText("62 to 63")

          Output4.setParent(self)
          Output4.move(1000,-5)
          return(Output4)

    def Switch5OutSetup(self):
          Output5 = QLabel()
          Output5.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[5]==True:
                Output5.setText("77 to 101")
          else:
                Output5.setText("76 to 77")

          Output5.setParent(self)
          Output5.move(1000,50)
          return(Output5)

    def Switch6OutSetup(self):
          Output5 = QLabel()
          Output5.setFont(self.labelFont)

          if WaysideControllerGreen2.switches[5]==True:
                Output5.setText("85 to 100")
          else:
                Output5.setText("85 to 86")

          Output5.setParent(self)
          Output5.move(1000,105)
          return(Output5)    

    def PLCLabelSetup(self):
          PLCLabel = QLabel()
          PLCLabel.setFont(self.titleFont)
          PLCLabel.setText("Upload PLC")
          PLCLabel.setFixedSize(QSize(110,40))
          PLCLabel.move(860,400)
          PLCLabel.setParent(self)
          return(PLCLabel)

    def PLCButton(self):
         PLCButton = QPushButton("PLC")
         PLCButton.setFont(self.labelFont) 
         PLCButton.setFixedSize(QSize(70,40))  
         PLCButton.clicked.connect(self.getfiles)
         PLCButton.setParent(self)
         PLCButton.move(870,450)
         return(PLCButton) 
    
    def brokenRailHandler(self, line, logic, blockNo):
         if line == 1 and blockNo <= 100:
            WaysideControllerGreen.setBrokenRail(bool(logic), blockNo)
         elif line == 1 and blockNo > 100:
            WaysideControllerGreen2.setBrokenRail(bool(logic), blockNo)

    def currBlockHandler(self, line, logic, blockNo):
         if line == 1 and blockNo <= 100:
            WaysideControllerGreen.setOccupancy(logic, blockNo)
         elif line == 1 and blockNo > 100:
            WaysideControllerGreen2.setOccupancy(logic, blockNo)
         
    def errorHandler(status):
         WaysideControllerGreen.setError(status)
         WaysideControllerGreen2.setError(status)
            
    #Clicking stuff
    def Switch1ButtonLClick(self):
          if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,1)
            WaysideControllerGreen2.setSwitchPositions(True,1)
    
    def Switch1ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,1)
            WaysideControllerGreen2.setSwitchPositions(False,1)
    
    def Switch2ButtonLClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,2)
            WaysideControllerGreen2.setSwitchPositions(True,2)
    
    def Switch2ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,2)
            WaysideControllerGreen2.setSwitchPositions(False,2)
    
    def Switch3ButtonLClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,3)
            WaysideControllerGreen2.setSwitchPositions(True,3)
    
    def Switch3ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,3)
            WaysideControllerGreen2.setSwitchPositions(False,3)
    
    def Switch4ButtonLClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,4)
            WaysideControllerGreen2.setSwitchPositions(True,4)
    
    def Switch4ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,4)
            WaysideControllerGreen2.setSwitchPositions(False,4)          
    
    def Switch5ButtonLClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,5)
            WaysideControllerGreen2.setSwitchPositions(True,5)          
          
    def Switch5ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,5)
            WaysideControllerGreen2.setSwitchPositions(False,5)

    def Switch6ButtonLClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(True,6)
            WaysideControllerGreen2.setSwitchPositions(True,6)


    def Switch6ButtonRClick(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setSwitchPositions(False,6)
            WaysideControllerGreen2.setSwitchPositions(False,6)            

    def UpClicked(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setGatePositions(True)
            WaysideControllerGreen2.setGatePositions(True)
    def DownClicked(self):
           if self.maintenanceMode == True:
            WaysideControllerGreen.setGatePositions(False)
            WaysideControllerGreen2.setGatePositions(False)
    def maintenance(self):
         if self.maintenanceMode==False:
            self.maintenanceMode=True
         else: 
            self.maintenanceMode=False
    def maintenanceLabelSetup(self):
            MLabel = QLabel()
            MLabel.setFont(self.labelFont)
            if(self.maintenanceMode==True):                
                  MLabel.setText("Maintenance ON")
            else:
                  MLabel.setText("Maintenance OFF")
            MLabel.setWordWrap(True)
            MLabel.setFixedSize(QSize(120,50))
            MLabel.setParent(self)
            return(MLabel)
    
    def getfiles(self):
            if self.maintenanceMode==True:
                name = QFileDialog.getOpenFileName(self,'Open file','c:\\',"Text files (*.txt)")
                stringname=(str(name[0]))            
                self.File2=stringname
                self.File2 = os.path.join(sys.path[0], "WaysideController", stringname)

    def updateVisualElements(self, active):
          
          if WaysideControllerGreen2.commandedSpeed!=WaysideControllerGreen2.suggestedSpeed:
            WaysideControllerGreen2.setCommandedSpeed()
            
          if WaysideControllerGreen2.authority!=WaysideControllerGreen2.suggestedAuthority:
            WaysideControllerGreen2.setAuthority()

          self.PLCMain = PLC(WaysideControllerGreen,WaysideControllerGreen2,"Green")
          if (self.Switch1Out.text() == "1 to 13" and WaysideControllerGreen2.switches[1] == False) or (self.Switch1Out.text() == "12 to 13" and WaysideControllerGreen2.switches[1] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[1]), 1, 12)
          if (self.Switch2Out.text() == "29 to 150" and WaysideControllerGreen2.switches[2] == False) or (self.Switch2Out.text() == "29 to 30" and WaysideControllerGreen2.switches[2] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[2]), 1, 28)
          if (self.Switch3Out.text() == "57 to Yard" and WaysideControllerGreen2.switches[3] == False) or (self.Switch3Out.text() == "57 to 58" and WaysideControllerGreen2.switches[3] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[3]), 1, 56)
          if (self.Switch4Out.text() == "Yard to 63" and WaysideControllerGreen2.switches[4] == False) or (self.Switch4Out.text() == "62 to 63" and WaysideControllerGreen2.switches[4] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[4]), 1, 62)
          if (self.Switch5Out.text() == "77 to 101" and WaysideControllerGreen2.switches[5] == False) or (self.Switch5Out.text() == "76 to 77" and WaysideControllerGreen2.switches[5] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[5]), 1, 76)
          if (self.Switch6Out.text() == "85 to 100" and WaysideControllerGreen2.switches[6] == False) or (self.Switch6Out.text() == "85 to 86" and WaysideControllerGreen2.switches[6] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerGreen2.switches[6]), 1, 84)
          if(self.maintenanceMode==True):                
                  self.maintenanceLabel.setText("Maintenance ON")
          else:
                  self.maintenanceLabel.setText("Maintenance OFF")
          if WaysideControllerGreen2.switches[1]==True:
                self.Switch1Out.setText("1 to 13")
          else:
                self.Switch1Out.setText("12 to 13")

          if WaysideControllerGreen2.switches[2]==True:
                self.Switch2Out.setText("29 to 150")
          else:
                self.Switch2Out.setText("29 to 30")    

          if WaysideControllerGreen2.switches[3]==True:
                self.Switch3Out.setText("57 to Yard")
          else:
                self.Switch3Out.setText("57 to 58")

          if WaysideControllerGreen2.switches[4]==True:
                self.Switch4Out.setText("Yard to 63")
          else:
                self.Switch4Out.setText("62 to 63")

          if WaysideControllerGreen2.switches[5]==True:
                self.Switch5Out.setText("77 to 101")
          else:
                self.Switch5Out.setText("76 to 77")

          if WaysideControllerGreen2.switches[6]==True:
                self.Switch6Out.setText("85 to 100")
          else:
                self.Switch6Out.setText("85 to 86")
          #self.Authority
          i=0
          j=1
          for k in range(101,self.blocks2):
                value=WaysideControllerGreen2.authority[k]
                if active and value != int(self.Authority.item(i,j).text()):
                    TkMWCSignals.authoritySignal.emit(k, value, 1)
                self.Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                  j=0
                  i=i+1 
          #self.CommandedSpeed
          j=1
          i=0
          for k in range(101,self.blocks2):
                value=WaysideControllerGreen2.commandedSpeed[k]
                value2=value*2.23694
                if active and value != float(self.CommandedSpeed.item(i,j).text()):
                  TkMWCSignals.commandedSpeedSignal.emit(k, float(value), 1)
                self.CommandedSpeed.setItem(i,j,QTableWidgetItem(str(round(value2,2))))
                j=j+1
                if j>9:
                        j=0
                        i=i+1          
          #self.BrokenRail 

          j=1
          i=0
          for k in range(101,self.blocks2):
                if WaysideControllerGreen2.brokenRail[k] == True:
                    value="Error"
                else:
                    value=" "
                self.BrokenRail.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                        j=0
                        i=i+1   
          #self.SignalLight 

          j=1
          i=0
          for k in range(101,self.blocks2):
                if WaysideControllerGreen2.signalLights[k]==True:
                  value="G"
                else:
                  value="R"
                if((k==1) | (k==13) | (k==77) | (k==100) | (k==84)):                  
                  if active and value != self.SignalLight.item(i,j).text():
                        if value == "G":
                              TkMWCSignals.signalStateSignal.emit(0, 1, k - 1)
                        elif value == "R":
                              TkMWCSignals.signalStateSignal.emit(2, 1, k - 1)
                if(k==101 or k==150):
                  self.SignalLight.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1       
         #self.Occupancy
          i=0
          j=1

          for k in range(101,self.blocks2):
                if WaysideControllerGreen2.occupancy[k]==True:
                  value="X"
                else:
                  value=" "
                self.Occupancy.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1

          for k in range(self.blocks1,self.blocks2):
            if(WaysideControllerGreen2.error==True):
                 for i in range(self.blocks1,self.blocks2):
                      WaysideControllerGreen2.setAAuthority(0,i)                 

          val = self.Gate.text()
          if WaysideControllerGreen2.gates[1]==True:
                self.Gate.setText("Block 19 Gate:  UP")
                if active and val != "Block 19 Gate:  UP":
                    TkMWCSignals.gateStateInput.emit(1, 1, 18)
          else:
                  self.Gate.setText("Block 19 Gate:  DOWN")
                  if active and val != "Block 19 Gate:  DOWN":
                    TkMWCSignals.gateStateInput.emit(0, 1, 18)

          if(self.maintenanceMode==False):                    
            self.PLCMain.GloadValues2(self.File2)
            self.PLCMain.setswitches()

    def mainEventLoop(self):
          self.updateVisualElements(self.active)
          WaysideControllerGreen2.WaysideToCTCInfoG2()
          WaysideControllerGreen2.getCTCBlocks()
          

def main():
      app = QApplication(sys.argv)

      mainWindow = MainWindow()
      mainWindow.show()

      if (mainWindow.TestUI) :
            mainWindow.WaysideControllerGreenTestUI.show()

      app.exec()
            
  