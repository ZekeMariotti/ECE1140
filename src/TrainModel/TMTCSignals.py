from PyQt6.QtCore import QObject, pyqtSignal

class trainModelTrainControllerSignals(QObject):
    # Train Model to Train Controller Signals
    commandedSpeedSignal = pyqtSignal(int, float)
    currentSpeedSignal = pyqtSignal(int, float)
    authoritySignal = pyqtSignal(int, int)
    undergroundSignal = pyqtSignal(int, bool)
    temperatureSignal = pyqtSignal(int, float)
    stationNameSignal = pyqtSignal(int, str)
    platformSideSignal = pyqtSignal(int, int)
    nextStationNameSignal = pyqtSignal(int, str)
    isBeaconSignal = pyqtSignal(int, bool)
    externalLightsStateSignal = pyqtSignal(int, bool)
    internalLightsStateSignal = pyqtSignal(int, bool)
    leftDoorStateSignal = pyqtSignal(int, bool)
    rightDoorStateSignal = pyqtSignal(int, bool)
    serviceBrakeStateSignal = pyqtSignal(int, bool)
    emergencyBrakeStateSignal = pyqtSignal(int, bool)
    serviceBrkaeStatusSignal = pyqtSignal(int, bool)
    engineStatusSignal = pyqtSignal(int, bool)
    communicationsStatusSignal = pyqtSignal(int, bool)

    # Train Controller to Train Model Signals
    commandedPowerSignal = pyqtSignal(int, float)
    leftDoorCommandSignal = pyqtSignal(int, bool)
    rightDoorCommandSignal = pyqtSignal(int, bool)
    serviceBrakeCommandSignal = pyqtSignal(int, bool)
    emergencyBrakeCommandSignal = pyqtSignal(int, bool)
    externalLightCommandSignal = pyqtSignal(int, bool)
    internalLightCommandSignal = pyqtSignal(int, bool)
    stationAnnouncementSignal = pyqtSignal(int, str)
    allSignals = pyqtSignal(int, float, bool, bool, bool, bool, bool, bool, str)
