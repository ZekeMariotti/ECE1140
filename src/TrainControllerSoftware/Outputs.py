# class for TrainController outputs
class Outputs:
    def __init__(self, power, leftDoorCommand, 
                 rightDoorCommand, serviceBrakeCommand, emergencyBrakeCommand, externalLightCommand, internalLightCommand, stationAnnouncement):
        # outputs
        self.power = power
        self.leftDoorCommand = leftDoorCommand
        self.rightDoorCommand = rightDoorCommand
        self.serviceBrakeCommand = serviceBrakeCommand
        self.emergencyBrakeCommand = emergencyBrakeCommand
        self.externalLightCommand = externalLightCommand
        self.internalLightCommand = internalLightCommand
        self.stationAnnouncement = stationAnnouncement