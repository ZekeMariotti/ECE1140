from PyQt6.QtCore import QObject, pyqtSignal

class activeSig(QObject):
    activeSignal = pyqtSignal()

activeSignals = activeSig()