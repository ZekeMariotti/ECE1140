from TrainModel import TrainModel

testTrainModel = TrainModel(2, "Green")

# Tests the finding acceleration function   
def testAccelerationCalculations(time, power, elevation, blockLength, prevVelocity):
    testTrainModel.data["power"] = power
    testTrainModel.trackData["elevation"] = elevation
    testTrainModel.trackData["blockLength"] = blockLength
    testTrainModel.data["prevVelocity"] = prevVelocity
    testTrainModel.findCurrentAcceleration(time)
    return round(testTrainModel.data["acceleration"], 4)

def testVelocityCalculations(time, prevVel, prevAccel, accel):
    testTrainModel.data["prevVelocity"] = prevVel
    testTrainModel.data["prevAcceleration"] = prevAccel
    testTrainModel.data["acceleration"] = accel
    testTrainModel.findCurrentVelocity(time)
    return round(testTrainModel.data["velocity"], 4)

def testDistanceCalculations(time, prevVelocity, velocity):
    testTrainModel.data["prevVelocity"] = prevVelocity
    testTrainModel.data["velocity"] = velocity
    testTrainModel.findCurrentDistance(time)
    return round(testTrainModel.trackData["distance"], 4)

print("Testing Acceleration", end = " ... ")
assert testAccelerationCalculations(1, 0, 0, 100, 10) == -.0589, f'Acceleration Test Failed. Acceleration = {round(testTrainModel.data["acceleration"], 4)}'
print("Acceleration Test Passed")
print("Testing Velocity", end = " ... ")
assert testVelocityCalculations(1, 15, 3, 3) == 18.0, f'Velocity Test Failed. Velocity = {round(testTrainModel.data["velocity"], 4)}'
print("Velocity Test Passed")
print("Testing Distance", end = " ... ")
assert testDistanceCalculations(2, 15, 20) == 35, f'Distance Test Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
print("Distance Test Passed")
    