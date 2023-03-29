from PyQt6.QtCore import QObject, pyqtSignal

class trainModelSignals(QObject):

    # Train Model Main UI Signals
    commButtonPressedSignal = pyqtSignal(int)
    engineButtonPressedSignal = pyqtSignal(int)
    brakeButtonPressedSignal = pyqtSignal(int)
    eBrakePressedSignal = pyqtSignal(int)
    tempChangedSignal = pyqtSignal(int, float)

    # Test UI Signal
    updateOutputs = pyqtSignal()

trainSignals = trainModelSignals()

# define inside