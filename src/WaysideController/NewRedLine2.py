import sys
import os
sys.path.append(__file__.replace("/WaysideController/NewRedLine.py", ""))
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from WaysideController.TestGenericWayside import Wayside
from WaysideController.PLC import PLC
from Integration.TkMWCSignals import *
from Integration.ActiveSignals import *
from WaysideController.RedLineTestUI import TestWindow
from WaysideController.NewRedLine import *


#global variables

rowheaders =["0","1","2","3","4","5","6","7"]
rowheaders2 =["5","6","7"]
colheaders =["0","1","2","3","4","5","6","7","8","9"]

class Worker(QObject):
      finished = pyqtSignal()

class MainWindowR(QMainWindow):
    def __init__(self,name):

        super().__init__()

        #Intialize Wayside class change sim time int later

        self.TestUI = True
        self.active = False
        activeSignals.activeSignal.connect(self.activeSignal)
        TkMWCSignals.failureSignal.connect(self.brokenRailHandler)
        TkMWCSignals.stopSignal.connect(self.error)
        TkMWCSignals.currBlockSignal.connect(self.currBlockHandler) 
        #Window
        self.name = name
        self.setWindowTitle(str(self.name))
        self.setFixedSize(QSize(1000,600))
        self.setMinimumSize(1150,650)
        self.move(0,0)
        self.globalFont = "Times New Roman"
        self.labelFont = QFont(self.globalFont,12)
        self.titleFont = QFont(self.globalFont,16)
        
        self.File1 = os.path.join(sys.path[0], "WaysideController", "RedLine.txt")
        self.File2 = os.path.join(sys.path[0], "WaysideController", "RedLine2.txt")


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
        self.Switch7BL = self.Switch7ButtonL()
        self.Switch7BR = self.Switch7ButtonR()
              

        #Switch Outputs
        self.Switch1Out = self.Switch1OutSetup()
        self.Switch2Out = self.Switch2OutSetup()
        self.Switch3Out = self.Switch3OutSetup()
        self.Switch4Out = self.Switch4OutSetup()
        self.Switch5Out = self.Switch5OutSetup()
        self.Switch6Out = self.Switch6OutSetup()
        self.Switch7Out = self.Switch7OutSetup()

        #Gate
        self.GateLabel = self.GateLabelSetup()
        self.Gate = self.GateSetup()
        self.Up = self.GateUp()
        self.Down = self.GateDown()
        #PLC
        self.PLCLabel = self.PLCLabelSetup()
        self.PLC = self.PLCButton()     

        self.maintenanceMode = False
        self.maintenanceButton = self.maintenanceButtonSetup() 
        self.maintenanceLabel = self.maintenanceLabelSetup()          
        self.PLCMain = PLC(WaysideControllerRed,WaysideControllerRed2,"Red")
        if self.TestUI :
              self.WaysideControllerRedTestUI = TestWindow(WaysideControllerRed,WaysideControllerRed2)             

    def brokenRailHandler(self, line, logic, blockNo):
         if line == 0 and blockNo <= 50:
            WaysideControllerRed.setBrokenRail(bool(logic), blockNo)
         elif line == 0 and blockNo > 50:
            WaysideControllerRed2.setBrokenRail(bool(logic), blockNo)

    def currBlockHandler(self, line, logic, blockNo):
         if line == 0 and blockNo <= 50:
            WaysideControllerRed.setOccupancy(logic, blockNo)
         elif line == 0 and blockNo > 50:
            WaysideControllerRed2.setOccupancy(logic, blockNo)

    def errorHandler(status):
         WaysideControllerRed.setError(status)
         WaysideControllerRed2.setError(status) 
       
    def activeSignal(self):
         self.active = True

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
            CommandedSpeed.setFixedSize(QSize(700,70))
            CommandedSpeed.setColumnCount(10)
            CommandedSpeed.setRowCount(3)
            CommandedSpeed.setVerticalHeaderLabels(rowheaders2)
            CommandedSpeed.setHorizontalHeaderLabels(colheaders)
            CommandedSpeed.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(51,77):
                  value=WaysideControllerRed2.commandedSpeed[k]
                  CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                  j=j+1
                  if j>9:
                        j=0
                        i=i+1
            for k in range(77,81):
                CommandedSpeed.setItem(7,j,QTableWidgetItem("-"))
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
            Authority.setFixedSize(QSize(700,70))
            Authority.setColumnCount(10)
            Authority.setRowCount(3)
            Authority.setVerticalHeaderLabels(rowheaders2)
            Authority.setHorizontalHeaderLabels(colheaders)
            Authority.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(51,77):
                value=WaysideControllerRed2.authority[k]
                Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1                  
            for k in range(78,81):
                Authority.setItem(7,j,QTableWidgetItem("-"))
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
            BrokenRail.setFixedSize(QSize(700,70))
            BrokenRail.setColumnCount(10)
            BrokenRail.setRowCount(3)
            BrokenRail.setVerticalHeaderLabels(rowheaders2)
            BrokenRail.setHorizontalHeaderLabels(colheaders)
            BrokenRail.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(51,77):
                if WaysideControllerRed2.brokenRail[k] == True:
                    BrokenRail.setItem(i,j,QTableWidgetItem("X"))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            for k in range(78,81):
                BrokenRail.setItem(7,j,QTableWidgetItem("-"))
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
            SignalLight.setFixedSize(QSize(700,70))
            SignalLight.setColumnCount(10)
            SignalLight.setRowCount(3)
            SignalLight.setVerticalHeaderLabels(rowheaders2)
            SignalLight.setHorizontalHeaderLabels(colheaders)
            SignalLight.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(51,77):
                if WaysideControllerRed2.signalLights[k]==True:
                  value="G"
                else:
                  value="R"
                if(k==52 or k==53 or k==66 or k==67 or k==71 or k==72 or k==76):
                  SignalLight.setItem(i,j,QTableWidgetItem((value)))
                else:
                  SignalLight.setItem(i,j,QTableWidgetItem((" ")))
                j=j+1
                if j>9:
                 j=0
                 i=i+1     
            for k in range(78,81):
                SignalLight.setItem(7,j,QTableWidgetItem("-"))
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
            Occupancy.setFixedSize(QSize(700,70))
            Occupancy.setColumnCount(10)
            Occupancy.setRowCount(3)
            Occupancy.setVerticalHeaderLabels(rowheaders2)
            Occupancy.setHorizontalHeaderLabels(colheaders)
            Occupancy.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(51,77):
                if WaysideControllerRed2.brokenRail[k] == True:
                    Occupancy.setItem(i,j,QTableWidgetItem("X"))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            Occupancy.setParent(self)
            Occupancy.move(0,550)
            return(Occupancy)
    
                    #Gate Functions

    def GateLabelSetup(self):
          GateLabel = QLabel()
          GateLabel.setFont(self.titleFont)
          GateLabel.setText("Gate State")
          GateLabel.setFixedSize(QSize(100,20))
          GateLabel.move(880,540)
          GateLabel.setParent(self)
          return(GateLabel)  
    
    def GateSetup(self):
            gate = QLabel()
            gate.setFont(self.labelFont)
            gate.setFixedSize(120,20)
            if WaysideControllerRed2.gates[1] == True:
                gate.setText("Block 47 Gate:  UP")

            else:
                gate.setText("Block 47 Gate:  DOWN")

            gate.move(875,580)
            gate.setParent(self)
            return(gate)

                    #Switch Functions

    def GateUp(self):
          Up = QPushButton("Up")
          Up.setFont(self.labelFont) 
          Up.setFixedSize(QSize(70,40))  
          Up.clicked.connect(self.UpClicked)
          Up.setParent(self)
          Up.move(1050,550)
          return(Up)

    def GateDown(self):
          Down = QPushButton("Down")
          Down.setFont(self.labelFont) 
          Down.setFixedSize(QSize(70,40))  
          Down.clicked.connect(self.DownClicked)
          Down.setParent(self)
          Down.move(1050,600)
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
          Switch1Label.setText("\nSwitch 1\n\n\nSwitch 2\n\n\nSwitch 3\n\n\n\nSwitch 4\n\n\nSwitch 5\n\n\nSwitch 6\n\n\nSwitch 7") 
          Switch1Label.setParent(self)
          Switch1Label.move(750,0)
          return(Switch1Label)
      
    def Switch1ButtonL(self):
          Push1L = QPushButton("9 to Yard")
          Push1L.setFont(self.labelFont) 
          Push1L.setFixedSize(QSize(70,40))  
          Push1L.clicked.connect(self.Switch1ButtonLClick)
          Push1L.setParent(self)
          Push1L.move(820,60)
          return(Push1L)
    
    def Switch1ButtonR(self):
          Push1R = QPushButton("Yard to 9")
          Push1R.setFont(self.labelFont) 
          Push1R.setFixedSize(QSize(70,40))  
          Push1R.clicked.connect(self.Switch1ButtonRClick)
          Push1R.setParent(self)
          Push1R.move(910,60)
          return(Push1R)
    
    def Switch2ButtonL(self):
          Push2L = QPushButton("15 to 16")
          Push2L.setFont(self.labelFont) 
          Push2L.setFixedSize(QSize(70,40))  
          Push2L.clicked.connect(self.Switch2ButtonLClick)
          Push2L.setParent(self)
          Push2L.move(820,115)
          return(Push2L)
    
    def Switch2ButtonR(self):
          Push2R = QPushButton("1 to 16")
          Push2R.setFont(self.labelFont) 
          Push2R.setFixedSize(QSize(70,40))  
          Push2R.clicked.connect(self.Switch2ButtonRClick)
          Push2R.setParent(self)
          Push2R.move(910,115)
          return(Push2R)
    
    def Switch3ButtonL(self):
          Push3L = QPushButton("27 to 28")
          Push3L.setFont(self.labelFont) 
          Push3L.setFixedSize(QSize(70,40))  
          Push3L.clicked.connect(self.Switch3ButtonLClick)
          Push3L.setParent(self)
          Push3L.move(820,170)
          return(Push3L)
    
    def Switch3ButtonR(self):
          Push3R = QPushButton("27 to 76")
          Push3R.setFont(self.labelFont) 
          Push3R.setFixedSize(QSize(70,40))  
          Push3R.clicked.connect(self.Switch3ButtonRClick)
          Push3R.setParent(self)
          Push3R.move(910,170)
          return(Push3R)

    def Switch4ButtonL(self):
          Push4L = QPushButton("32 to 33")
          Push4L.setFont(self.labelFont) 
          Push4L.setFixedSize(QSize(70,40))  
          Push4L.clicked.connect(self.Switch4ButtonLClick)
          Push4L.setParent(self)
          Push4L.move(820,230)
          return(Push4L)
    
    def Switch4ButtonR(self):
          Push4R = QPushButton("33 to 72")
          Push4R.setFont(self.labelFont) 
          Push4R.setFixedSize(QSize(70,40))  
          Push4R.clicked.connect(self.Switch4ButtonRClick)
          Push4R.setParent(self)
          Push4R.move(910,230)
          return(Push4R)
    
    def Switch5ButtonL(self):
          Push5L = QPushButton("38 to 39")
          Push5L.setFont(self.labelFont) 
          Push5L.setFixedSize(QSize(70,40))  
          Push5L.clicked.connect(self.Switch5ButtonLClick)
          Push5L.setParent(self)
          Push5L.move(820,285)
          return(Push5L)
    
    def Switch5ButtonR(self):
          Push5R = QPushButton("38 to 71")
          Push5R.setFont(self.labelFont) 
          Push5R.setFixedSize(QSize(70,40))  
          Push5R.clicked.connect(self.Switch5ButtonRClick)
          Push5R.setParent(self)
          Push5R.move(910,285)
          return(Push5R)

    def Switch6ButtonL(self):
          Push6L = QPushButton("43 to 44")
          Push6L.setFont(self.labelFont) 
          Push6L.setFixedSize(QSize(70,40))  
          Push6L.clicked.connect(self.Switch6ButtonLClick)
          Push6L.setParent(self)
          Push6L.move(820,340)
          return(Push6L)
    
    def Switch6ButtonR(self):
          Push6R = QPushButton("44 to 67")
          Push6R.setFont(self.labelFont) 
          Push6R.setFixedSize(QSize(70,40))  
          Push6R.clicked.connect(self.Switch6ButtonRClick)
          Push6R.setParent(self)
          Push6R.move(910,340)
          return(Push6R)

    def Switch7ButtonL(self):
          Push7L = QPushButton("52 to 53")
          Push7L.setFont(self.labelFont) 
          Push7L.setFixedSize(QSize(70,40))  
          Push7L.clicked.connect(self.Switch7ButtonLClick)
          Push7L.setParent(self)
          Push7L.move(820,395)
          return(Push7L)
    
    def Switch7ButtonR(self):
          Push7R = QPushButton("52 to 66")
          Push7R.setFont(self.labelFont) 
          Push7R.setFixedSize(QSize(70,40))  
          Push7R.clicked.connect(self.Switch7ButtonRClick)
          Push7R.setParent(self)
          Push7R.move(910,395)
          return(Push7R)        
    
    def Switch1OutSetup(self):
          Output1 = QLabel()
          Output1.setFont(self.labelFont)
          Output1.setFixedSize(70,20)
          if WaysideControllerRed2.switches[1]==True:
                Output1.setText("9 to Yard")
          else:
                Output1.setText("Yard to 9")

          Output1.setParent(self)
          Output1.move(1000,60)
          return(Output1)
    
    def Switch2OutSetup(self):
          Output2 = QLabel()
          Output2.setFont(self.labelFont)
          Output2.setFixedSize(70,20)
          if WaysideControllerRed2.switches[2]==True:
                Output2.setText("15 to 16")
          else:
                Output2.setText("1 to 15")

          Output2.setParent(self)
          Output2.move(1000,120)
          return(Output2)

    def Switch3OutSetup(self):
          Output3 = QLabel()
          Output3.setFont(self.labelFont)
          Output3.setFixedSize(70,20)
          if WaysideControllerRed2.switches[3]==True:
                Output3.setText("27 to 28")
          else:
                Output3.setText("27 to 76")

          Output3.setParent(self)
          Output3.move(1000,180)
          return(Output3)

    def Switch4OutSetup(self):
          Output4 = QLabel()
          Output4.setFont(self.labelFont)
          Output4.setFixedSize(70,20)
          if WaysideControllerRed2.switches[4]==True:
                Output4.setText("32 to 33")
          else:
                Output4.setText("33 to 72")

          Output4.setParent(self)
          Output4.move(1000,240)
          return(Output4)

    def Switch5OutSetup(self):
          Output5 = QLabel()
          Output5.setFont(self.labelFont)
          Output5.setFixedSize(70,20)
          if WaysideControllerRed2.switches[5]==True:
                Output5.setText("38 to 39")
          else:
                Output5.setText("38 to 71")

          Output5.setParent(self)
          Output5.move(1000,290)
          return(Output5)
        
    def Switch6OutSetup(self):
          Output6 = QLabel()
          Output6.setFont(self.labelFont)
          Output6.setFixedSize(70,20)
          if WaysideControllerRed2.switches[6]==True:
                Output6.setText("43 to 44")
          else:
                Output6.setText("44 to 67")

          Output6.setParent(self)
          Output6.move(1000,350)
          return(Output6)

    def Switch7OutSetup(self):
          Output7 = QLabel()
          Output7.setFont(self.labelFont)
          Output7.setFixedSize(70,20)
          if WaysideControllerRed2.switches[7]==True:
                Output7.setText("52 to 53")
          else:
                Output7.setText("52 to 66")

          Output7.setParent(self)
          Output7.move(1000,410)
          return(Output7)

    def PLCLabelSetup(self):
          PLCLabel = QLabel()
          PLCLabel.setFont(self.titleFont)
          PLCLabel.setText("Upload PLC")
          PLCLabel.setFixedSize(QSize(110,40))
          PLCLabel.move(860,430)
          PLCLabel.setParent(self)
          return(PLCLabel)

    def PLCButton(self):
         PLCButton = QPushButton("PLC")
         PLCButton.setFont(self.labelFont) 
         PLCButton.setFixedSize(QSize(70,40))  
         PLCButton.clicked.connect(self.getfiles)
         PLCButton.setParent(self)
         PLCButton.move(870,480)
         return(PLCButton) 
                  
    #Clicking stuff    
    def Switch1ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,1)
            WaysideControllerRed2.setSwitchPositions(True,1)
            
    def Switch1ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,1)
            WaysideControllerRed2.setSwitchPositions(False,1)

    def Switch2ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,2)
            WaysideControllerRed2.setSwitchPositions(True,2)

    def Switch2ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,2)
            WaysideControllerRed2.setSwitchPositions(False,2)  

    def Switch3ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,3)
            WaysideControllerRed2.setSwitchPositions(True,3)

    def Switch3ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,3)
            WaysideControllerRed2.setSwitchPositions(False,3)
    
    def Switch4ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,4)
            WaysideControllerRed2.setSwitchPositions(True,4)

    def Switch4ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,4)
            WaysideControllerRed.setSwitchPositions(False,4)          
    
    def Switch5ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,5)          
            WaysideControllerRed2.setSwitchPositions(True,5)

    def Switch5ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,5)
            WaysideControllerRed2.setSwitchPositions(False,5)

    def Switch6ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,6)          
            WaysideControllerRed2.setSwitchPositions(True,6)

    def Switch6ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,6)
            WaysideControllerRed2.setSwitchPositions(False,6)

    def Switch7ButtonLClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(True,7)          
            WaysideControllerRed2.setSwitchPositions(True,7)

    def Switch7ButtonRClick(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setSwitchPositions(False,7)
            WaysideControllerRed2.setSwitchPositions(False,7)          
      
    def UpClicked(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setGatePositions(True)
            WaysideControllerRed2.setGatePositions(True)
          
    def DownClicked(self):
          if(self.maintenanceMode==True):
            WaysideControllerRed.setGatePositions(False)
            WaysideControllerRed2.setGatePositions(False)

    def maintenance(self):
          if(self.maintenanceMode==True):
            self.maintenanceMode=False
          else:
            self.maintenanceMode=True 

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
            if self.maintenanceMode == True: 
                  name = QFileDialog.getOpenFileName(self,'Open file','c:\\',"Text files (*.txt)")
                  stringname=(str(name[0]))            
                  self.File2=stringname
                  self.File2 = os.path.join(sys.path[0], "WaysideController", stringname)

    def updateVisualElements(self,active):
          
          if WaysideControllerRed2.commandedSpeed!=WaysideControllerRed2.suggestedSpeed:
            WaysideControllerRed.setCommandedSpeed()

          if WaysideControllerRed2.authority!=WaysideControllerRed2.suggestedAuthority:
            WaysideControllerRed2.setAuthority()

          if (self.Switch1Out.text() == "Yard to 9" and WaysideControllerRed2.switches[1] == False) or (self.Switch1Out.text() == "9 to Yard" and WaysideControllerRed2.switches[1] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[1]), 0, 8)
          if (self.Switch2Out.text() == "1 to 16" and WaysideControllerRed2.switches[2] == False) or (self.Switch2Out.text() == "15 to 16" and WaysideControllerRed2.switches[2] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[2]), 0, 15)
          if (self.Switch3Out.text() == "27 to 76" and WaysideControllerRed2.switches[3] == False) or (self.Switch3Out.text() == "27 to 28" and WaysideControllerRed2.switches[3] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[3]), 0, 26)
          if (self.Switch4Out.text() == "33 to 72" and WaysideControllerRed2.switches[4] == False) or (self.Switch4Out.text() == "32 to 33" and WaysideControllerRed2.switches[4] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[4]), 0, 32)
          if (self.Switch5Out.text() == "38 to 71" and WaysideControllerRed2.switches[5] == False) or (self.Switch5Out.text() == "38 to 39" and WaysideControllerRed2.switches[5] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[5]), 0, 37)
          if (self.Switch6Out.text() == "44 to 67" and WaysideControllerRed2.switches[6] == False) or (self.Switch6Out.text() == "43 to 44" and WaysideControllerRed2.switches[6] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[6]), 0, 43)
          if (self.Switch7Out.text() == "52 to 66" and WaysideControllerRed2.switches[7] == False)  or (self.Switch7Out.text() == "52 to 53" and WaysideControllerRed2.switches[7] == True):
            TkMWCSignals.switchStateSignal.emit(int(WaysideControllerRed2.switches[7]),0,51)

          if(self.maintenanceMode==True):                
                  self.maintenanceLabel.setText("Maintenance ON")
          else:
                  self.maintenanceLabel.setText("Maintenance OFF")  
                          
          if WaysideControllerRed2.switches[1]==True:
                self.Switch1Out.setText("9 to Yard")
          else:
                self.Switch1Out.setText("Yard to 9")

          if WaysideControllerRed2.switches[2]==True:
                self.Switch2Out.setText("15 to 16")
          else:
                self.Switch2Out.setText("1 to 16")    

          if WaysideControllerRed2.switches[3]==True:
                self.Switch3Out.setText("27 to 28")
          else:
                self.Switch3Out.setText("27 to 76")

          if WaysideControllerRed2.switches[4]==True:
                self.Switch4Out.setText("32 to 33")
          else:
                self.Switch4Out.setText("33 to 72")

          if WaysideControllerRed2.switches[5]==True:
                self.Switch5Out.setText("38 to 39")
          else:
                self.Switch5Out.setText("38 to 71")

          if WaysideControllerRed2.switches[6]==True:
                self.Switch6Out.setText("43 to 44")
          else:
                self.Switch6Out.setText("44 to 67")

          if WaysideControllerRed2.switches[7]==True:
                self.Switch7Out.setText("52 to 53")
          else:
                self.Switch7Out.setText("52 to 66")

#self.Authority
          i=0
          j=1
          for k in range(51,77):
                value=WaysideControllerRed2.authority[k]
                if active and value != int(self.Authority.item(i,j).text()):
                  TkMWCSignals.authoritySignal.emit(k, value, 0)                
                self.Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                    j=0
                    i=i+1                 
          #self.CommandedSpeed
          i=0
          j=1
          for k in range(51,77):
                value=WaysideControllerRed2.commandedSpeed[k]
                value2=value*2.23694               
                if active and value != float(self.CommandedSpeed.item(i,j).text()):
                  TkMWCSignals.commandedSpeedSignal.emit(k, value, 0)                
                self.CommandedSpeed.setItem(i,j,QTableWidgetItem(str(round(value2,2))))
                j=j+1
                if j>9:
                        j=0
                        i=i+1                             
          #self.BrokenRail 
          j=1
          i=0
          for k in range(51,77):
                value = WaysideControllerRed2.brokenRail[k]             
                if value == True:
                        print("Rail is now broken")
                        self.BrokenRail.setItem(i,j,QTableWidgetItem(str("ERROR")))
                j=j+1
                if j>9:
                 j=0
                 i=i+1                 
          #self.SignalLight 
          i=0
          j=1
          for k in range(51,77):
                if WaysideControllerRed2.signalLights[k]==True:
                     value="G"
                else:
                     value="R"
                if(k==52 or k==53 or k==66 or k==67 or k==71 or k==72 or k==76):                     
                  self.SignalLight.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1                 
         #self.Occupancy
          i=0
          j=1      
          for k in range(51,77):
                value = WaysideControllerRed2.occupancy[k]
                if value == True:
                        self.Occupancy.setItem(i,j,QTableWidgetItem(str("X")))
                j=j+1
                if j>9:
                        j=0
                        i=i+1 

          for k in range(51,77):
            if(WaysideControllerRed2.error==True):
                 for i in range(51,77):
                      WaysideControllerRed2.setAAuthority(0,i)

          val = self.Gate.text()
          if WaysideControllerRed2.gates[1]==True:
                self.Gate.setText("Block 47 Gate:  UP")
                if active and val != "Block 47 Gate:  UP":
                    TkMWCSignals.gateStateInput.emit(1, 0, 46)
          else:
                  self.Gate.setText("Block 47 Gate:  DOWN")
                  if active and val != "Block 47 Gate:  DOWN":
                    TkMWCSignals.gateStateInput.emit(0, 0, 46)

          if(self.maintenanceMode==False):
            self.PLCMain.RloadValues2(self.File2)
            self.PLCMain.Rsetswitches()

    def mainEventLoop(self):
          self.updateVisualElements(self.active)
          WaysideControllerRed2.WaysideToCTCInfoR2()
          WaysideControllerRed2.getCTCBlocksRed()


def main():
    app = QApplication(sys.argv)

    mainWindow = MainWindowR()
    mainWindow.show()

    if (mainWindow.TestUI) :
        mainWindow.WaysideControllerRedTestUI.show()

    app.exec()
        
  