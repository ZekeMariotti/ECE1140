from time import sleep

def findCurrentVelocity(power, prevVelocity, prevAcceleration, mass, time):
    force = power / prevVelocity
    currAcceleration = force / mass
    print(currAcceleration)
    currVelocity = prevVelocity + ((time / 2) * (currAcceleration + prevAcceleration))
    return currVelocity

if __name__ == "__main__":
    v = findCurrentVelocity(12000, 15, 0, 15000, 3)
    print(v)

