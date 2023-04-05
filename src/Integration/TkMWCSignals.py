from PyQt6.QtCore import QObject, pyqtSignal

class trackModelWaysideControllerSignals(QObject):
    # Wayside to track model
    authoritySignal = pyqtSignal(int, int, int)
    commandedSpeedSignal = pyqtSignal(int, float, int)
    switchStateSignal = pyqtSignal(int, int, int)
    signalStateSignal = pyqtSignal(int, int, int)
    gateStateInput = pyqtSignal(int, int)

    # Track Model to Wayide
    failureSignal = pyqtSignal(int, int, int)
    currBlockSignal = pyqtSignal(int, bool, int)

TkMWCSignals = trackModelWaysideControllerSignals()