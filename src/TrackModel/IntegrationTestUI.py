import sys
# Import all reuired modules
sys.path.append(__file__.replace("\TrackModel\IntegrationTestUI.py", ""))

from sys import argv, exit
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QComboBox, QLineEdit
from TrackModel.TrackModelBackEnd import *
from TrackModel.TrackModelMainUI import TrackModelMainUI
from TrackModel.TrackModelSignals import *
from Integration.TMTkMSignals import *

class BasicTestUI(QWidget):
    def __init__(self):
        self.trainID = 0
        # Initializing the layout of the UI
        super(BasicTestUI, self).__init__()
        self.setWindowTitle("Integration Test UI")
        layout = QGridLayout()
        self.setLayout(layout)

        self.trainIDEdit = QLineEdit()
        self.trainIDEdit.editingFinished.connect(self.trainIDHandler)
        layout.addWidget(self.trainIDEdit, 0, 0)

        self.authorityEdit = QLineEdit()
        self.authorityEdit.editingFinished.connect(self.authorityHandler)
        layout.addWidget(self.authorityEdit, 1, 0)

        self.commandedSpeedEdit = QLineEdit()
        self.commandedSpeedEdit.editingFinished.connect(self.cmdSpeedHandler)
        layout.addWidget(self.commandedSpeedEdit, 2, 0)

    def trainIDHandler(self):
        self.trainID = int(self.trainIDEdit.text())

    def authorityHandler(self):
        TMTkMSignals.authoritySignal.emit(self.trainID, int(self.authorityEdit.text()))
        trackSignals.getAuthInput.emit(int(self.authorityEdit.text()), self.trainID)

    def cmdSpeedHandler(self):
        TMTkMSignals.commandedSpeedSignal.emit(self.trainID, float(self.commandedSpeedEdit.text()))
        trackSignals.getCSpeedInput.emit(float(self.commandedSpeedEdit.text()), self.trainID)
    
