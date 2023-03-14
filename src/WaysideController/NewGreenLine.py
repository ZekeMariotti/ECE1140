from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from waysideclass import WaysideControllerGreen
from GreenLineTestUi import TestWindow
import sys

#global variables

rowheaders =["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
colheaders =["0","1","2","3","4","5","6","7","8","9"]

class Worker(QObject):
      finished = pyqtSignal()

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        #Intialize Wayside class
        self.WaysideControllerGreen = WaysideControllerGreen(1,True)
        self.TestUI = True
        #self.WaysideController.writeOutputs()
        #self.WaysideController.readInputs()

        #Window

        self.setWindowTitle("Green Line")
        self.setFixedSize(QSize(1100,660))
        self.setMinimumSize(1100,650)
        self.move(0,0)
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

        #Switch Outputs
        self.Switch1Out = self.Switch1OutSetup()
        self.Switch2Out = self.Switch2OutSetup()
        self.Switch3Out = self.Switch3OutSetup()
        self.Switch4Out = self.Switch4OutSetup()
        self.Switch5Out = self.Switch5OutSetup()

        #Gate
        self.GateLabel = self.GateLabelSetup()
        self.Gate = self.GateSetup()

        #Test UI
        if self.TestUI :
              self.WaysideControllerGreenTestUI = TestWindow()
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

    def CommandedSpeedLabelSetup(self):
            CommandedLabel = QLabel()
            CommandedLabel.setFont(self.titleFont)
            CommandedLabel.setText("Commanded Speed (MPH)")
            CommandedLabel.move(450,-220)
            CommandedLabel.setParent(self)
            return(CommandedLabel)
    
    def CommandedSpeedSetup(self):
            CommandedSpeed = QTableWidget()
            CommandedSpeed.setFont(self.labelFont)
            CommandedSpeed.setFixedSize(QSize(700,70))
            CommandedSpeed.setColumnCount(10)
            CommandedSpeed.setRowCount(16)
            CommandedSpeed.setVerticalHeaderLabels(rowheaders)
            CommandedSpeed.setHorizontalHeaderLabels(colheaders)
            CommandedSpeed.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,151):
                value=self.WaysideControllerGreen.getCommandedSpeed(k)
                CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
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
          AuthorityLabel.move(480,-100)
          AuthorityLabel.setParent(self)
          return(AuthorityLabel)
    
    def AuthoritySetup(self):
            Authority = QTableWidget()
            Authority.setFont(self.labelFont)
            Authority.setFixedSize(QSize(700,70))
            Authority.setColumnCount(10)
            Authority.setRowCount(16)
            Authority.setVerticalHeaderLabels(rowheaders)
            Authority.setHorizontalHeaderLabels(colheaders)
            Authority.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
                Authority.setItem(15,j,QTableWidgetItem("-"))
                j=j+1            
            Authority.setParent(self)
            Authority.move(0,170)
            return(Authority)
    
                #Broken Rail Functions

    def RailLabelSetup(self):
          RailLabel = QLabel()
          RailLabel.setFont(self.titleFont)
          RailLabel.setText("Broken Rail")
          RailLabel.move(500,25)
          RailLabel.setParent(self)
          return(RailLabel)
    
    def BrokenRailSetup(self):
            BrokenRail = QTableWidget()
            BrokenRail.setFont(self.labelFont)
            BrokenRail.setFixedSize(QSize(700,70))
            BrokenRail.setColumnCount(10)
            BrokenRail.setRowCount(16)
            BrokenRail.setVerticalHeaderLabels(rowheaders)
            BrokenRail.setHorizontalHeaderLabels(colheaders)
            BrokenRail.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,151):
                if self.WaysideControllerGreen.getBrokenRail(k) == True:
                    BrokenRail.setItem(i,j,QTableWidgetItem("X"))
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
          ColorLabel.setParent(self)
          ColorLabel.move(470,155)
          return(ColorLabel)
    
    def SignalLightSetup(self):
            SignalLight = QTableWidget()
            SignalLight.setFont(self.labelFont)
            SignalLight.setFixedSize(QSize(700,70))
            SignalLight.setColumnCount(10)
            SignalLight.setRowCount(16)
            SignalLight.setVerticalHeaderLabels(rowheaders)
            SignalLight.setHorizontalHeaderLabels(colheaders)
            SignalLight.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,151):
                value=self.WaysideControllerGreen.getSignalLights(k)
                SignalLight.setItem(i,j,QTableWidgetItem((value)))
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
          OccupancyLabel.move(500,275)
          OccupancyLabel.setParent(self)
          return(OccupancyLabel)  
            
    def OccupancySetup(self):
            Occupancy = QTableWidget()
            Occupancy.setFont(self.labelFont)
            Occupancy.setFixedSize(QSize(700,70))
            Occupancy.setColumnCount(10)
            Occupancy.setRowCount(16)
            Occupancy.setVerticalHeaderLabels(rowheaders)
            Occupancy.setHorizontalHeaderLabels(colheaders)
            Occupancy.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,151):
                if self.WaysideControllerGreen.getBrokenRail(k) == True:
                    Occupancy.setItem(i,j,QTableWidgetItem("X"))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=1
            for k in range(152,161):
                Occupancy.setItem(15,j,QTableWidgetItem("-"))
                j=j+1
            Occupancy.setParent(self)
            Occupancy.move(0,550)
            return(Occupancy)
    
                    #Gate Functions

    def GateLabelSetup(self):
          GateLabel = QLabel()
          GateLabel.setFont(self.titleFont)
          GateLabel.setText("Gate State")
          GateLabel.move(875,300)
          GateLabel.setParent(self)
          return(GateLabel)  
    
    def GateSetup(self):
            gate = QLabel()
            gate.setFont(self.labelFont)

            if self.WaysideControllerGreen.getGatePositions() == True:
                gate.setText("Block 19 Gate:  UP")

            else:
                gate.setText("Block 19 Gate:  DOWN")

            gate.move(875,350)
            gate.setParent(self)
            return(gate)

                    #Switch Functions

    def MainSwitchLabel(self):
          MainSwitchLabel = QLabel()
          MainSwitchLabel.setFont(self.titleFont)
          MainSwitchLabel.setText("Switches")
          MainSwitchLabel.setParent(self)
          MainSwitchLabel.move(875,-200)
          return(MainSwitchLabel)
    
    def SwitchLabels(self):
          Switch1Label = QLabel()
          Switch1Label.setFont(self.labelFont)
          Switch1Label.setText("Switch 1\n\n\nSwitch 2\n\n\nSwitch 3\n\n\nSwitch 4\n\n\nSwitch 5") 
          Switch1Label.setParent(self)
          Switch1Label.move(750,0)
          return(Switch1Label)
      
    def Switch1ButtonL(self):
          Push1L = QPushButton("12 to 13")
          Push1L.setFont(self.labelFont) 
          Push1L.setFixedSize(QSize(70,40))  
          Push1L.clicked.connect(self.Switch1ButtonLClick)
          Push1L.setParent(self)
          Push1L.move(820,105)
          return(Push1L)
    
    def Switch1ButtonR(self):
          Push1R = QPushButton("1 to 13")
          Push1R.setFont(self.labelFont) 
          Push1R.setFixedSize(QSize(70,40))  
          Push1R.clicked.connect(self.Switch1ButtonRClick)
          Push1R.setParent(self)
          Push1R.move(910,105)
          return(Push1R)
    
    def Switch2ButtonL(self):
          Push2L = QPushButton("29 to 30")
          Push2L.setFont(self.labelFont) 
          Push2L.setFixedSize(QSize(70,40))  
          Push2L.clicked.connect(self.Switch2ButtonLClick)
          Push2L.setParent(self)
          Push2L.move(820,160)
          return(Push2L)
    
    def Switch2ButtonR(self):
          Push2R = QPushButton("29 to 150")
          Push2R.setFont(self.labelFont) 
          Push2R.setFixedSize(QSize(70,40))  
          Push2R.clicked.connect(self.Switch2ButtonRClick)
          Push2R.setParent(self)
          Push2R.move(910,160)
          return(Push2R)
    
    def Switch3ButtonL(self):
          Push3L = QPushButton("57 to Yard")
          Push3L.setFont(self.labelFont) 
          Push3L.setFixedSize(QSize(70,40))  
          Push3L.clicked.connect(self.Switch3ButtonLClick)
          Push3L.setParent(self)
          Push3L.move(820,215)
          return(Push3L)
    
    def Switch3ButtonR(self):
          Push3R = QPushButton("57 to 58")
          Push3R.setFont(self.labelFont) 
          Push3R.setFixedSize(QSize(70,40))  
          Push3R.clicked.connect(self.Switch3ButtonRClick)
          Push3R.setParent(self)
          Push3R.move(910,215)
          return(Push3R)

    def Switch4ButtonL(self):
          Push4L = QPushButton("76 to 77")
          Push4L.setFont(self.labelFont) 
          Push4L.setFixedSize(QSize(70,40))  
          Push4L.clicked.connect(self.Switch4ButtonLClick)
          Push4L.setParent(self)
          Push4L.move(820,270)
          return(Push4L)
    
    def Switch4ButtonR(self):
          Push4R = QPushButton("77 to 101")
          Push4R.setFont(self.labelFont) 
          Push4R.setFixedSize(QSize(70,40))  
          Push4R.clicked.connect(self.Switch4ButtonRClick)
          Push4R.setParent(self)
          Push4R.move(910,270)
          return(Push4R)
    
    def Switch5ButtonL(self):
          Push5L = QPushButton("85 to 86")
          Push5L.setFont(self.labelFont) 
          Push5L.setFixedSize(QSize(70,40))  
          Push5L.clicked.connect(self.Switch5ButtonLClick)
          Push5L.setParent(self)
          Push5L.move(820,325)
          return(Push5L)
    
    def Switch5ButtonR(self):
          Push5R = QPushButton("100 to 85")
          Push5R.setFont(self.labelFont) 
          Push5R.setFixedSize(QSize(70,40))  
          Push5R.clicked.connect(self.Switch5ButtonRClick)
          Push5R.setParent(self)
          Push5R.move(910,325)
          return(Push5R)
    
    def Switch1OutSetup(self):
          Output1 = QLabel()
          Output1.setFont(self.labelFont)

          if self.WaysideControllerGreen.getSwitchPositions(1)==True:
                Output1.setText("12 to 13")
          else:
                Output1.setText("1 to 13")

          Output1.setParent(self)
          Output1.move(1000,-115)
          return(Output1)
    
    def Switch2OutSetup(self):
          Output2 = QLabel()
          Output2.setFont(self.labelFont)

          if self.WaysideControllerGreen.getSwitchPositions(2)==True:
                Output2.setText("29 to 30")
          else:
                Output2.setText("29 to 150")

          Output2.setParent(self)
          Output2.move(1000,-60)
          return(Output2)

    def Switch3OutSetup(self):
          Output3 = QLabel()
          Output3.setFont(self.labelFont)

          if self.WaysideControllerGreen.getSwitchPositions(3)==True:
                Output3.setText("57 to Yard")
          else:
                Output3.setText("57 to 58")

          Output3.setParent(self)
          Output3.move(1000,-5)
          return(Output3)

    def Switch4OutSetup(self):
          Output4 = QLabel()
          Output4.setFont(self.labelFont)

          if self.WaysideControllerGreen.getSwitchPositions(4)==True:
                Output4.setText("76 to 77")
          else:
                Output4.setText("77 to 101")

          Output4.setParent(self)
          Output4.move(1000,50)
          return(Output4)

    def Switch5OutSetup(self):
          Output5 = QLabel()
          Output5.setFont(self.labelFont)

          if self.WaysideControllerGreen.getSwitchPositions(5)==True:
                Output5.setText("85 to 86")
          else:
                Output5.setText("100 to 85")

          Output5.setParent(self)
          Output5.move(1000,105)
          return(Output5)
        
    #Clicking stuff    
    def Switch1ButtonLClick(self):
          self.WaysideControllerGreen.setSwitchPositions(True,1)
    
    def Switch1ButtonRClick(self):
          self.WaysideControllerGreen.setSwitchPositions(False,1)
    
    def Switch2ButtonLClick(self):
          self.WaysideControllerGreen.setSwitchPositions(True,2)
    
    def Switch2ButtonRClick(self):
          self.WaysideControllerGreen.setSwitchPositions(False,2)
    
    def Switch3ButtonLClick(self):
          self.WaysideControllerGreen.setSwitchPositions(True,3)
    
    def Switch3ButtonRClick(self):
          self.WaysideControllerGreen.setSwitchPositions(False,3)
    
    def Switch4ButtonLClick(self):
          self.WaysideControllerGreen.setSwitchPositions(True,4)
    
    def Switch4ButtonRClick(self):
          self.WaysideControllerGreen.setSwitchPositions(False,4)          
    
    def Switch5ButtonLClick(self):
          self.WaysideControllerGreen.setSwitchPositions(True,5)          
          
    def Switch5ButtonRClick(self):
          self.WaysideControllerGreen.setSwitchPositions(False,5)
          
    def updateVisualElements(self):
          #hour = str(self.WaysideController.realTime.hour) if self.WaysideController.realTime.hour <=12 else str(self.WaysideController.realTime.hour - 12)   
          #if(int(hour)==0):
           #     hour = "12"
          #minute = str(self.WaysideController.realTime.minute)
          #second = str(self.WaysideController.realTime.second)
          #might add to ui
          #self.realTimeClock.setText(f'Time: {hour}:{minute}:{second}')
          
          if self.WaysideControllerGreen.getSwitchPositions(1)==True:
                self.Switch1Out.setText("12 to 13")
          else:
                self.Switch1Out.setText("1 to 13")

          if self.WaysideControllerGreen.getSwitchPositions(2)==True:
                self.Switch2Out.setText("29 to 30")
          else:
                self.Switch2Out.setText("29 to 150")    

          if self.WaysideControllerGreen.getSwitchPositions(3)==True:
                self.Switch3Out.setText("57 to Yard")
          else:
                self.Switch3Out.setText("57 to 58")

          if self.WaysideControllerGreen.getSwitchPositions(4)==True:
                self.Switch4Out.setText("76 to 77")
          else:
                self.Switch4Out.setText("77 to 101")

          if self.WaysideControllerGreen.getSwitchPositions(5)==True:
                self.Switch5Out.setText("85 to 86")
          else:
                self.Switch5Out.setText("100 to 85")
          #self.Authority
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                self.Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
          #self.CommandedSpeed
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                self.CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1           
          #self.BrokenRail 
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                self.BrokenRail.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
          #self.SignalLight 
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                self.SignalLight.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
         #self.Occupancy
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerGreen.getAuthority(k)
                self.Occupancy.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1        
          if self.WaysideControllerGreen.getGatePositions()==True:
                self.Gate.setText("Block 19 Gate:  UP")
          else:
                self.Gate.setText("Block 19 Gate:  DOWN")

    def mainEventLoop(self):
          self.WaysideControllerGreen.currentTime = self.WaysideControllerGreen.realTime

          self.updateVisualElements()

          self.WaysideControllerGreen.previousTime = self.WaysideControllerGreen.realTime
          
app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

if (mainWindow.TestUI) :
      mainWindow.WaysideControllerGreenTestUI.show()

app.exec()
        
  