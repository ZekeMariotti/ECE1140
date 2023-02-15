from math import sin, atan

#def findCurrentVelocity(power, prevVelocity, prevAcceleration, mass, time):
#    force = power / prevVelocity
#    currAcceleration = force / mass
#    print(currAcceleration)
#    currVelocity = prevVelocity + ((time / 2) * (currAcceleration + prevAcceleration))
#    return currVelocity

def findCurrentVelocity(power, prevVelocity, prevAcceleration, mass, time, elevation, grade):
    force = power / prevVelocity
    if (grade == 0 | elevation == 0):
        currAcceleration = force / mass
    else:
        currAcceleration = (force - (mass * 9.8 * sin(atan(elevation / (elevation / grade))))) / mass
    currVelocity = prevVelocity + ((time / 2) * (currAcceleration + prevAcceleration))
    return currVelocity

if __name__ == "__main__":
    v = findCurrentVelocity(12000, 15, 0, 40823, 3, 0, 0)
    print("V1: ", v)
    v = findCurrentVelocity(12000, 15, 0, 40823, 3, 1, 0.01)
    print("V2: ", v)
    v = findCurrentVelocity(12000, 15, 0, 40823, 3, -3, -0.03)
    print("V3: ", v)
