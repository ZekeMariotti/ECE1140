from PyQt6.QtCore import QObject, pyqtSignal

class timeSignals(QObject):
    # Signal for the real time clock
    rtcSignal = pyqtSignal(str)

rtcSignals = timeSignals()