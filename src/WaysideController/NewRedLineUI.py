from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from waysideclassred import WaysideControllerRed
import sys

#global variables

rowheaders =["0","1","2","3","4","5","6","7"]
colheaders =["0","1","2","3","4","5","6","7","8","9"]

class Worker(QObject):
      finished = pyqtSignal()

class MainWindow(QMainWindow):
    def __init__(self):

        super().__init__()

        #Intialize Wayside class
        self.WaysideControllerRed = WaysideControllerRed(1,True)
        #self.WaysideController.writeOutputs()
        #self.WaysideController.readInputs()

        #Window

        self.setWindowTitle("Red Line")
        self.setFixedSize(QSize(1000,600))
        self.setMinimumSize(1150,650)
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
        #PLC
        self.PLC = self.PLCButton()        
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
            CommandedSpeed.setRowCount(8)
            CommandedSpeed.setVerticalHeaderLabels(rowheaders)
            CommandedSpeed.setHorizontalHeaderLabels(colheaders)
            CommandedSpeed.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,77):
                value=self.WaysideControllerRed.getCommandedSpeed(k)
                CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=7
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
          AuthorityLabel.move(480,-100)
          AuthorityLabel.setParent(self)
          return(AuthorityLabel)
    
    def AuthoritySetup(self):
            Authority = QTableWidget()
            Authority.setFont(self.labelFont)
            Authority.setFixedSize(QSize(700,70))
            Authority.setColumnCount(10)
            Authority.setRowCount(8)
            Authority.setVerticalHeaderLabels(rowheaders)
            Authority.setHorizontalHeaderLabels(colheaders)
            Authority.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,77):
                value=self.WaysideControllerRed.getAuthority(k)
                Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=7
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
          RailLabel.move(500,25)
          RailLabel.setParent(self)
          return(RailLabel)
    
    def BrokenRailSetup(self):
            BrokenRail = QTableWidget()
            BrokenRail.setFont(self.labelFont)
            BrokenRail.setFixedSize(QSize(700,70))
            BrokenRail.setColumnCount(10)
            BrokenRail.setRowCount(8)
            BrokenRail.setVerticalHeaderLabels(rowheaders)
            BrokenRail.setHorizontalHeaderLabels(colheaders)
            BrokenRail.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,77):
                if self.WaysideControllerRed.getBrokenRail(k) == True:
                    BrokenRail.setItem(i,j,QTableWidgetItem("X"))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=7
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
          ColorLabel.setParent(self)
          ColorLabel.move(470,155)
          return(ColorLabel)
    
    def SignalLightSetup(self):
            SignalLight = QTableWidget()
            SignalLight.setFont(self.labelFont)
            SignalLight.setFixedSize(QSize(700,70))
            SignalLight.setColumnCount(10)
            SignalLight.setRowCount(8)
            SignalLight.setVerticalHeaderLabels(rowheaders)
            SignalLight.setHorizontalHeaderLabels(colheaders)
            SignalLight.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,77):
                value=self.WaysideControllerRed.getSignalLights(k)
                SignalLight.setItem(i,j,QTableWidgetItem((value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=7
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
          OccupancyLabel.move(500,275)
          OccupancyLabel.setParent(self)
          return(OccupancyLabel)  
            
    def OccupancySetup(self):
            Occupancy = QTableWidget()
            Occupancy.setFont(self.labelFont)
            Occupancy.setFixedSize(QSize(700,70))
            Occupancy.setColumnCount(10)
            Occupancy.setRowCount(8)
            Occupancy.setVerticalHeaderLabels(rowheaders)
            Occupancy.setHorizontalHeaderLabels(colheaders)
            Occupancy.setItem(0,0,QTableWidgetItem("-"))
            i=0
            j=1
            for k in range(1,77):
                if self.WaysideControllerRed.getBrokenRail(k) == True:
                    Occupancy.setItem(i,j,QTableWidgetItem("X"))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
            j=7
            for k in range(152,161):
                Occupancy.setItem(7,j,QTableWidgetItem("-"))
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

            if self.WaysideControllerRed.getGatePositions() == True:
                gate.setText("Block 47 Gate:  UP")

            else:
                gate.setText("Block 47 Gate:  DOWN")

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
          Switch1Label.setText("\nSwitch 1\n\n\nSwitch 2\n\n\nSwitch 3\n\n\nSwitch 4\n\n\nSwitch 5\n\n\nSwitch 6\n\n\nSwtich 7") 
          Switch1Label.setParent(self)
          Switch1Label.move(750,0)
          return(Switch1Label)
      
    def Switch1ButtonL(self):
          Push1L = QPushButton("75 to Yard")
          Push1L.setFont(self.labelFont) 
          Push1L.setFixedSize(QSize(70,40))  
          Push1L.clicked.connect(self.Switch1ButtonLClick)
          Push1L.setParent(self)
          Push1L.move(820,60)
          return(Push1L)
    
    def Switch1ButtonR(self):
          Push1R = QPushButton("Yard to 75")
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

          if self.WaysideControllerRed.getSwitchPositions(1)==True:
                Output1.setText("75 to Yard")
          else:
                Output1.setText("Yard to 75")

          Output1.setParent(self)
          Output1.move(1000,-160)
          return(Output1)
    
    def Switch2OutSetup(self):
          Output2 = QLabel()
          Output2.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(2)==True:
                Output2.setText("15 to 16")
          else:
                Output2.setText("1 to 15")

          Output2.setParent(self)
          Output2.move(1000,-105)
          return(Output2)

    def Switch3OutSetup(self):
          Output3 = QLabel()
          Output3.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(3)==True:
                Output3.setText("27 to 28")
          else:
                Output3.setText("27 to 76")

          Output3.setParent(self)
          Output3.move(1000,-50)
          return(Output3)

    def Switch4OutSetup(self):
          Output4 = QLabel()
          Output4.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(4)==True:
                Output4.setText("32 to 33")
          else:
                Output4.setText("33 to 72")

          Output4.setParent(self)
          Output4.move(1000,10)
          return(Output4)

    def Switch5OutSetup(self):
          Output5 = QLabel()
          Output5.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(5)==True:
                Output5.setText("38 to 39")
          else:
                Output5.setText("38 to 71")

          Output5.setParent(self)
          Output5.move(1000,65)
          return(Output5)
        
    def Switch6OutSetup(self):
          Output6 = QLabel()
          Output6.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(5)==True:
                Output6.setText("43 to 44")
          else:
                Output6.setText("44 to 67")

          Output6.setParent(self)
          Output6.move(1000,120)
          return(Output6)

    def Switch7OutSetup(self):
          Output7 = QLabel()
          Output7.setFont(self.labelFont)

          if self.WaysideControllerRed.getSwitchPositions(5)==True:
                Output7.setText("52 to 53")
          else:
                Output7.setText("52 to 66")

          Output7.setParent(self)
          Output7.move(1000,175)
          return(Output7)
     
    def PLCButton(self):
         PLCButton = QPushButton("PLC")
         PLCButton.setFont(self.labelFont) 
         PLCButton.setFixedSize(QSize(70,40))  
         #PLCButton.clicked.connect()
         PLCButton.setParent(self)
         PLCButton.move(870,480)
         return(PLCButton) 
                  
    #Clicking stuff    
    def Switch1ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,1)
    
    def Switch1ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,1)
    
    def Switch2ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,2)
    
    def Switch2ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,2)
    
    def Switch3ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,3)
    
    def Switch3ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,3)
    
    def Switch4ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,4)
    
    def Switch4ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,4)          
    
    def Switch5ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,5)          
          
    def Switch5ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,5)

    def Switch6ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,6)          
          
    def Switch6ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,6)

    def Switch7ButtonLClick(self):
          self.WaysideControllerRed.setSwitchPositions(True,7)          
          
    def Switch7ButtonRClick(self):
          self.WaysideControllerRed.setSwitchPositions(False,7)          
          
    def updateVisualElements(self):
          #hour = str(self.WaysideController.realTime.hour) if self.WaysideController.realTime.hour <=12 else str(self.WaysideController.realTime.hour - 12)   
          #if(int(hour)==0):
           #     hour = "12"
          #minute = str(self.WaysideController.realTime.minute)
          #second = str(self.WaysideController.realTime.second)
          #might add to ui
          #self.realTimeClock.setText(f'Time: {hour}:{minute}:{second}')
          
          if self.WaysideControllerRed.getSwitchPositions(1)==True:
                self.Switch1Out.setText("75 to Yard")
          else:
                self.Switch1Out.setText("Yard to 75")

          if self.WaysideControllerRed.getSwitchPositions(2)==True:
                self.Switch2Out.setText("15 to 16")
          else:
                self.Switch2Out.setText("1 to 16")    

          if self.WaysideControllerRed.getSwitchPositions(3)==True:
                self.Switch3Out.setText("27 to 28")
          else:
                self.Switch3Out.setText("27 to 76")

          if self.WaysideControllerRed.getSwitchPositions(4)==True:
                self.Switch4Out.setText("32 to 33")
          else:
                self.Switch4Out.setText("33 to 72")

          if self.WaysideControllerRed.getSwitchPositions(5)==True:
                self.Switch5Out.setText("38 to 39")
          else:
                self.Switch5Out.setText("38 to 71")

          if self.WaysideControllerRed.getSwitchPositions(6)==True:
                self.Switch6Out.setText("43 to 44")
          else:
                self.Switch6Out.setText("44 to 67")

          if self.WaysideControllerRed.getSwitchPositions(7)==True:
                self.Switch7Out.setText("52 to 53")
          else:
                self.Switch7Out.setText("52 to 66")

#self.Authority
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerRed.getAuthority(k)
                self.Authority.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
          #self.CommandedSpeed
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerRed.getCommandedSpeed(k)
                self.CommandedSpeed.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                        j=0
                        i=i+1           
          #self.BrokenRail 
          i=0
          j=1
          for k in range(1,151):
                if value == self.WaysideControllerRed.getBrokenRail(k)== True:
                        self.BrokenRail.setItem(i,j,QTableWidgetItem(str("ERROR")))
                        j=j+1
                if j>9:
                 j=0
                 i=i+1
          #self.SignalLight 
          i=0
          j=1
          for k in range(1,151):
                value=self.WaysideControllerRed.getSignalLights(k)
                self.SignalLight.setItem(i,j,QTableWidgetItem(str(value)))
                j=j+1
                if j>9:
                 j=0
                 i=i+1
         #self.Occupancy
          i=0
          j=1
          for k in range(1,151):
                if value == self.WaysideControllerRed.getOccupancy(k):
                        self.Occupancy.setItem(i,j,QTableWidgetItem(str("X")))
                        j=j+1
                if j>9:
                        j=0
                        i=i+1        

          if self.WaysideControllerRed.getGatePositions()==True:
                self.Gate.setText("Block 47 Gate:  UP")
          else:
                self.Gate.setText("Block 47 Gate:  DOWN")

    def mainEventLoop(self):
          self.WaysideControllerRed.currentTime = self.WaysideControllerRed.realTime

          self.updateVisualElements()

          self.WaysideControllerRed.previousTime = self.WaysideControllerRed.realTime
          WaysideControllerRed.WaysideToCTC()
          WaysideControllerRed.WaysideToTrack()

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.show()

app.exec()
        
  