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
    blockCountSignal = pyqtSignal(int, int)
    fromSwitchSignal = pyqtSignal(int, bool)
    switchBlockSignal = pyqtSignal(int, int)
    externalLightsStateSignal = pyqtSignal(int, bool)
    internalLightsStateSignal = pyqtSignal(int, bool)
    leftDoorStateSignal = pyqtSignal(int, bool)
    rightDoorStateSignal = pyqtSignal(int, bool)
    serviceBrakeStateSignal = pyqtSignal(int, bool)
    emergencyBrakeStateSignal = pyqtSignal(int, bool)
    serviceBrakeStatusSignal = pyqtSignal(int, bool)
    engineStatusSignal = pyqtSignal(int, bool)
    communicationsStatusSignal = pyqtSignal(int, bool)
    polaritySignal = pyqtSignal(int, bool)

    # Train Controller to Train Model Signals
    commandedPowerSignal = pyqtSignal(int, float)
    leftDoorCommandSignal = pyqtSignal(int, bool)
    rightDoorCommandSignal = pyqtSignal(int, bool)
    serviceBrakeCommandSignal = pyqtSignal(int, bool)
    emergencyBrakeCommandSignal = pyqtSignal(int, bool)
    externalLightCommandSignal = pyqtSignal(int, bool)
    internalLightCommandSignal = pyqtSignal(int, bool)
    stationAnnouncementSignal = pyqtSignal(int, str)
    stationStateSignal = pyqtSignal(int, bool)

TMTCSignals = trainModelTrainControllerSignals()