import sys

sys.path.append(__file__.replace("\Integration\BlocksClass.py", ""))

class blocks():
    def __init__(self, number, blockLength, elevation, speedLimit, underground):
        self.blockNum = number
        self.blockLength = blockLength
        self.elevation = elevation
        self.speedLimit = speedLimit
        self.undergroundState = underground