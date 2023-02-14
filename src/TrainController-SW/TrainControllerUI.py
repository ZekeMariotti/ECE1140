# Main UI for the Train Controller Software

from PyQt6.QtWidgets import QApplication, QWidget

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()