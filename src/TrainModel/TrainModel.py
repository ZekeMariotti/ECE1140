# Train Model Overall File

from TrainModelTestUI import TrainModelTestUI
from BackEnd import findCurrentVelocity, findCurrentAcceleration
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication
from sys import argv
from time import sleep

app = QApplication(argv)
form = TrainModelTestUI()
form.show()
exit(app.exec())