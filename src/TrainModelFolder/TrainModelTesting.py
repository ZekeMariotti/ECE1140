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

def testFindTimeDifference(time1, time2):
    testTrainModel.data["prevRTC"] = time1
    testTrainModel.data["rtc"] = time2
    return testTrainModel.findTimeDifference()

# def testBlockExiting()

# def testNextBlock()

def testAirConditioningControl(time, currTemp, goalTemp):
    testTrainModel.data["currTemp"] = currTemp
    testTrainModel.data["goalTemp"] = goalTemp
    testTrainModel.airConditioningControl(time)
    return testTrainModel.data["currTemp"]

def testFindCurrentMass(passengers, crew):
    testTrainModel.data["passengers"] = passengers
    testTrainModel.data["crew"] = crew
    testTrainModel.findCurrentMass()
    return testTrainModel.data["mass"]

def testBrakeCalculator(passenger, trainController):
    testTrainModel.eBrakes["user"] = passenger
    testTrainModel.eBrakes["trainController"] = trainController
    testTrainModel.brakeCaclulator()
    return testTrainModel.data["eBrakeState"]

def testPassengersOn(passengersOn):
    testTrainModel.data["passengers"] = 10
    testTrainModel.data["passengersOn"] = passengersOn
    testTrainModel.passengersGettingOn()
    return testTrainModel.data["passengers"]

print("Testing Acceleration", end = " ... ")
assert testAccelerationCalculations(1, 0, 0, 100, 10) == -.0589, f'Acceleration Test Failed. Acceleration = {round(testTrainModel.data["acceleration"], 4)}'
print("Acceleration Test Passed")
print("Testing Velocity", end = " ... ")
assert testVelocityCalculations(1, 15, 3, 3) == 18.0, f'Velocity Test Failed. Velocity = {round(testTrainModel.data["velocity"], 4)}'
print("Velocity Test Passed")
print("Testing Distance", end = " ... ")
assert testDistanceCalculations(2, 15, 20) == 35, f'Distance Test 1 Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
assert testDistanceCalculations(1, 15, 20) == 17.5, f'Distance Test 2 Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
assert testDistanceCalculations(0, 15, 20) == 0, f'Distance Test 3 Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
assert testDistanceCalculations(1, 20, 20) == 20, f'Distance Test 4 Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
assert testDistanceCalculations(1, 20, 10) == 15, f'Distance Test 5 Failed. Distance = {round(testTrainModel.data["distance"], 4)}'
print("Distance Test Passed")
print("Testing Air Conditioning", end = " ... ")
assert testAirConditioningControl(1, 5, 10) == 5.5, f'AC Test 1 Failed. CurrentTemp = {testTrainModel.data["currTemp"]}'
assert testAirConditioningControl(0.2, 5, 10) == 5.1, f'AC Test 2 Failed. CurrentTemp = {testTrainModel.data["currTemp"]}'
assert testAirConditioningControl(1, 20, 20) == 20, f'AC Test 3 Failed. CurrentTemp = {testTrainModel.data["currTemp"]}'
assert testAirConditioningControl(5, 20, 100) == 22.5, f'AC Test 4 Failed. CurrentTemp = {testTrainModel.data["currTemp"]}'
assert testAirConditioningControl(0, 5, 10) == 5, f'AC Test 5 Failed. CurrentTemp = {testTrainModel.data["currTemp"]}'
print("Air Conditioning Tests Passed")
print("Testing Current Mass Calculations", end = " ... ")
assert testFindCurrentMass(120, 1) == 49132.7069, f'Current Mass Test 1 Failed. Mass = {testTrainModel.data["mass"]}'
assert testFindCurrentMass(0, 0) == 40900, f'Current Mass Test 2 Failed. Mass = {testTrainModel.data["mass"]}'
print("Current Mass Tests Passed")
print("Testing Brake Calculator", end = " ... ")
assert testBrakeCalculator(False, False) == False, f'Brake Calculator Test 1 Failed. eBrakeState = {testTrainModel.data["eBrakeState"]}'
assert testBrakeCalculator(False, True) == True, f'Brake Calculator Test 2 Failed. eBrakeState = {testTrainModel.data["eBrakeState"]}'
assert testBrakeCalculator(True, False) == True, f'Brake Calculator Test 3 Failed. eBrakeState = {testTrainModel.data["eBrakeState"]}'
assert testBrakeCalculator(True, True) == True, f'Brake Calculator Test 4 Failed. eBrakeState = {testTrainModel.data["eBrakeState"]}'
print("Brake Calculator Tests Passed")
print("Testing Passengers On", end = " ... ")
assert testPassengersOn(0) == 10, f'Passengers On Test 1 Failed. Passengers = {testTrainModel.data["passengers"]}'
assert testPassengersOn(150) == 160, f'Passengers On Test 2 Failed. Passengers = {testTrainModel.data["passengers"]}'
assert testPassengersOn(240) == 222, f'Passengers On Test 3 Failed. Passengers = {testTrainModel.data["passengers"]}'
print("Passengers On Tests Passed")