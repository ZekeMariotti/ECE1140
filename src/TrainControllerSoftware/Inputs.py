# class for TrainController inputs
class Inputs:
    def __init__(self, commandedSpeed, currentSpeed, authority, inputTime, undergroundState, temperature, 
                 stationName, platformSide, nextStationName, isBeacon, externalLightsState, internalLightsState, leftDoorState, rightDoorState, 
                 serviceBrakeState, emergencyBrakeState, serviceBrakeStatus, engineStatus, communicationsStatus):
        # Inputs
        self.commandedSpeed = commandedSpeed
        self.currentSpeed = currentSpeed
        self.authority = authority
        self.inputTime = str(inputTime)
        self.undergroundState = undergroundState
        self.temperature = temperature
        self.stationName = stationName
        self.platformSide = platformSide
        self.nextStationName = nextStationName
        self.isBeacon = isBeacon
        self.externalLightsState = externalLightsState
        self.internalLightsState = internalLightsState
        self.leftDoorState = leftDoorState
        self.rightDoorState = rightDoorState
        self.serviceBrakeState = serviceBrakeState
        self.emergencyBrakeState = emergencyBrakeState
        self.serviceBrakeStatus = serviceBrakeStatus
        self.engineStatus = engineStatus
        self.communicationsStatus = communicationsStatus