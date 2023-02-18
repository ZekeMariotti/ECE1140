# Train Model Back End

from math import sin, atan
from time import sleep

simulationSpeed = 5

#class backEndCalculations():

simulationSpeed = 1

def __init__(self):
    self.simulationSpeed = 1

# Finds the current acceleration of a train
def findCurrentAcceleration(power, prevVelocity, mass, elevation, grade) :
    if (prevVelocity == 0):
        force = mass * 0.5
    else:
        force = power / prevVelocity

    if ((grade == 0.0) | (elevation == 0.0)):
        currAcceleration = force / mass
    else:
        # Calculating the effect of weight on the train while it is on an incline
        currAcceleration = (force - (mass * 9.81 * sin(atan(elevation / (elevation / grade))))) / mass
        # Calculate the force due to mg differently

    
    return currAcceleration

# Finds the current velocity of a train given 7 inputs
def findCurrentVelocity(currAcceleration, prevAcceleration, prevVelocity, time):
    currVelocity = prevVelocity + ((time / 2) * (currAcceleration + prevAcceleration))
    return currVelocity if currVelocity >= 0 else 0.0

# Air Conditioning System that changes based on user input
def airConditioningControl(temperatureGoal, temperature):
    while temperatureGoal != temperature:
        sleep(1 / simulationSpeed)
        if temperature < temperatureGoal:
            temperature += 1
        else:
            temperature -= 1
        print(temperature)

# Get distance since the last state update of the system
def getTotalDistance():
    print("Hello There")

# Main function to run if this file is the file being ran as main
def main():
    a = findCurrentAcceleration(12000, 0, 37103.8665, 0, 0)
    print("A:", a)
    v = findCurrentVelocity(a, 0.0, 0.0, simulationSpeed)
    print("V:", v)
    airConditioningControl(100, 40)
    #v = findCurrentVelocity(12000, 15, 0, 40823, 3, 1, 0.01)
    #print("V2: ", v)
    #v = findCurrentVelocity(12000, 15, 0, 40823, 3, -3, -0.03)
    #print("V3: ", v)

if __name__ == "__main__":
    main()
