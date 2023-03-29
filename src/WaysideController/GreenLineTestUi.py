from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from TestGenericWayside import Wayside
import sys 

class Worker(QObject):
      finished = pyqtSignal()

class TestWindow(QMainWindow):
    def __init__(self,Wayside1,Wayside2):

        super().__init__()

        #Intialize Wayside class
        self.WaysideControllerGreen = Wayside1
        self.WaysideControllerGreen2 = Wayside2
        #self.WaysideController.writeOutputs()
        #self.WaysideController.readInputs()

        #Window
        self.storeAuthority = None
        self.storeAuthorityBlock = None
        self.storeCommandedSpeed = None
        self.storeCommandedSpeedBlock = None
        self.setWindowTitle("Green Line Test UI")
        self.setFixedSize(QSize(600,800))
        self.setMinimumSize(600,800)
        self.move(0,0)
        self.globalFont = "Times New Roman"
        self.labelFont = QFont(self.globalFont,12)
        self.titleFont = QFont(self.globalFont,16)

        self.Switches = self.MainSwitchLabel()
        self.SwitchLabel = self.SwitchLabels()
        self.Left1 = self.Switch1ButtonL()
        self.Right1 =self.Switch1ButtonR()
        self.Left2 = self.Switch2ButtonL()
        self.Right2 =self.Switch2ButtonR()
        self.Left3 = self.Switch3ButtonL()
        self.Right3 =self.Switch3ButtonR()
        self.Left4 = self.Switch4ButtonL()
        self.Right4 = self.Switch4ButtonR()
        self.Left5 = self.Switch5ButtonL()
        self.Right5 = self.Switch5ButtonR()
        self.AuthorityLabel = self.AuthorityLabelSetup()
        self.Authority = self.AuthorityInput()
        self.AuthorityBlock = self. AuthorityBlockInput()
        self.CommandedSpeedLabel = self.CommandedSpeedLabelSetup()
        self.CommandedSpeed = self.CommandedSpeedInput()
        self.CommandedSpeedBlock = self.CommandedSpeedBlockInput()
        self.OccupancyBlock = self.OccupancyBlockInput()
        self.OccupancyLabel = self.OccupancyLabelSetup()
        #self.Occupied = self.OccupiedButton()
        #self.Unoccupied = self.UnoccupiedButton()
        self.SignalLabel = self.SignalLabelSetup()
        self.signalsBlock = self.SignalBlockInput()
        #self.RedSignal = self.RedButton()
        #self.GreenSignal = self.GreenButton()
        self.GateLabel = self.GateLabelSetup()
        self.Up = self.GateUp()
        self.Down = self.GateDown()

    def MainSwitchLabel(self):
          MainSwitchLabel = QLabel()
          MainSwitchLabel.setFont(self.titleFont)
          MainSwitchLabel.setText("Switches")
          MainSwitchLabel.setParent(self)
          MainSwitchLabel.move(400,-200)
          return(MainSwitchLabel)
    
    def SwitchLabels(self):
          Switch1Label = QLabel()
          Switch1Label.setFont(self.labelFont)
          Switch1Label.setText("Switch 1\n\n\nSwitch 2\n\n\nSwitch 3\n\n\nSwitch 4\n\n\nSwitch 5") 
          Switch1Label.setParent(self)
          Switch1Label.move(300,0)
          return(Switch1Label)
    
    def AuthorityLabelSetup(self):
          Auth = QLabel()
          Auth.setFont(self.labelFont)
          Auth.setText("Authority            Block")
          Auth.setParent(self)
          Auth.move(50,-70)
          return(Auth)
    
    def CommandedSpeedLabelSetup(self):
          CSL = QLabel()
          CSL.setFont(self.labelFont)
          CSL.setText("Commanded Speed       Block")
          CSL.setParent(self)
          CSL.move(20,20)
          return(CSL)
              
    def Switch1ButtonL(self):
          Push1L = QPushButton("12 to 13")
          Push1L.setFont(self.labelFont) 
          Push1L.setFixedSize(QSize(70,40)) 
          Push1L.clicked.connect(self.Switch1ButtonLClick)
          Push1L.setParent(self)
          Push1L.move(400,105)
          return(Push1L)
    
    def Switch1ButtonR(self):
          Push1R = QPushButton("1 to 13")
          Push1R.setFont(self.labelFont) 
          Push1R.setFixedSize(QSize(70,40))  
          Push1R.clicked.connect(self.Switch1ButtonRClick)
          Push1R.setParent(self)
          Push1R.move(500,105)
          return(Push1R)
    
    def Switch2ButtonL(self):
          Push2L = QPushButton("29 to 30")
          Push2L.setFont(self.labelFont) 
          Push2L.setFixedSize(QSize(70,40))  
          Push2L.clicked.connect(self.Switch2ButtonLClick)
          Push2L.setParent(self)
          Push2L.move(400,160)
          return(Push2L)
    
    def Switch2ButtonR(self):
          Push2R = QPushButton("29 to 150")
          Push2R.setFont(self.labelFont) 
          Push2R.setFixedSize(QSize(70,40))  
          Push2R.clicked.connect(self.Switch2ButtonRClick)
          Push2R.setParent(self)
          Push2R.move(500,160)
          return(Push2R)
    
    def Switch3ButtonL(self):
          Push3L = QPushButton("57 to Yard")
          Push3L.setFont(self.labelFont) 
          Push3L.setFixedSize(QSize(70,40))  
          Push3L.clicked.connect(self.Switch3ButtonLClick)
          Push3L.setParent(self)
          Push3L.move(400,215)
          return(Push3L)
    
    def Switch3ButtonR(self):
          Push3R = QPushButton("57 to 58")
          Push3R.setFont(self.labelFont) 
          Push3R.setFixedSize(QSize(70,40))  
          Push3R.clicked.connect(self.Switch3ButtonRClick)
          Push3R.setParent(self)
          Push3R.move(500,215)
          return(Push3R)

    def Switch4ButtonL(self):
          Push4L = QPushButton("76 to 77")
          Push4L.setFont(self.labelFont) 
          Push4L.setFixedSize(QSize(70,40))  
          Push4L.clicked.connect(self.Switch4ButtonLClick)
          Push4L.setParent(self)
          Push4L.move(400,270)
          return(Push4L)
    
    def Switch4ButtonR(self):
          Push4R = QPushButton("77 to 101")
          Push4R.setFont(self.labelFont) 
          Push4R.setFixedSize(QSize(70,40))  
          Push4R.clicked.connect(self.Switch4ButtonRClick)
          Push4R.setParent(self)
          Push4R.move(500,270)
          return(Push4R)
    
    def Switch5ButtonL(self):
          Push5L = QPushButton("85 to 86")
          Push5L.setFont(self.labelFont) 
          Push5L.setFixedSize(QSize(70,40))  
          Push5L.clicked.connect(self.Switch5ButtonLClick)
          Push5L.setParent(self)
          Push5L.move(400,325)
          return(Push5L)
    
    def Switch5ButtonR(self):
          Push5R = QPushButton("100 to 85")
          Push5R.setFont(self.labelFont) 
          Push5R.setFixedSize(QSize(70,40))  
          Push5R.clicked.connect(self.Switch5ButtonRClick)
          Push5R.setParent(self)
          Push5R.move(500,325)
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

    def GateLabelSetup(self):
          GateLabel = QLabel()
          GateLabel.setFont(self.titleFont)
          GateLabel.setText("Block 19 Gate") 
          GateLabel.setParent(self)
          GateLabel.move(70,-200)
          return(GateLabel)

    def GateUp(self):
          Up = QPushButton("Up")
          Up.setFont(self.labelFont) 
          Up.setFixedSize(QSize(70,40))  
          Up.clicked.connect(self.UpClicked)
          Up.setParent(self)
          Up.move(50,100)
          return(Up)

    def GateDown(self):
          Down = QPushButton("Down")
          Down.setFont(self.labelFont) 
          Down.setFixedSize(QSize(70,40))  
          Down.clicked.connect(self.DownClicked)
          Down.setParent(self)
          Down.move(150,100)
          return(Down)

    def AuthorityInput(self):
          AInput = QLineEdit()
          AInput.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          AInput.setParent(self)
          AInput.move(50,200)
          return(AInput)
    
    def AuthorityBlockInput(self):
          ABlock = QComboBox()
          ABlock.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          ABlock.setParent(self)
          ABlock.move(150,200)
          return(ABlock)
     
    def CommandedSpeedInput(self):
          CSInput = QLineEdit()
          CSInput.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          CSInput.setParent(self)
          CSInput.move(50,300)
          return(CSInput)
    
    def CommandedSpeedBlockInput(self):
          CSBlock = QComboBox()
          CSBlock.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          CSBlock.setParent(self)
          CSBlock.move(150,300)
          return(CSBlock)   
    
    def OccupancyLabelSetup(self):
          OblockI = QLabel()
          OblockI.setFont(self.labelFont)
          OblockI.setText("Block") 
          OblockI.setParent(self)
          OblockI.move(60,220)
          return(OblockI)
    
    def SignalLabelSetup(self):
          SignalLabel = QLabel()
          SignalLabel.setFont(self.labelFont)
          SignalLabel.setText("Block") 
          SignalLabel.setParent(self)
          SignalLabel.move(60,320)
          return(SignalLabel)
    
    def OccupancyBlockInput(self):
          OBlock = QComboBox()
          OBlock.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          OBlock.setParent(self)
          OBlock.move(50,500)
          return(OBlock) 
    
    def SignalBlockInput(self):
          SBlock = QComboBox()
          SBlock.setFixedSize(QSize(50,20))
         #AInput.textChanged.connect(self.setAuthorityTextChanged)
          SBlock.setParent(self)
          SBlock.move(50,600)
          return(SBlock)

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
    
    def UpClicked(self):
          self.WaysideControllerGreen.setGatePositions(True)
          
    def DownClicked(self):
          self.WaysideControllerGreen.setGatePositions(False)

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    testWindow = TestWindow()
    testWindow.show()
    app.exec()