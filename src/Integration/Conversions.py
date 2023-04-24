# File for converting units to imperial before outputting them
from datetime import *

# Takes an input in Meters and converts it to Feet
def metersToFeet(number):
    return round(number * 3.28084, 2)

# Takes an input in Kilometers and converts it to Miles
def kilometersToMiles(number):
    return round(number * 0.621371, 2)

# Takes an input in Kilograms and converts it to US Tons
def kilogramsToTons(number):
    return round(number * 0.00110231, 2)

# Takes an input in Meters Per Second and converts it to Miles Per Hour
def metersPerSecondToMilesPerHour(number):
    return round(number * 2.23695, 2)

# Takes an input in Miles Per Hour and converts it to Meters Per Second
def milesPerHourToMetersPerSecond(number):
    return round(number * 0.44704, 2)

# Takes an input in Meters Per Second ^2 and conerts it to Feet Per Second ^ 2
def metersPerSecondSquaredToFeetPerSecondSquared(number):
    return round(number * 3.28084, 2)

# Takes an input in Watts and converts it to Horsepower
def wattsToHorsepower(number):
    return round(number * 0.00134102, 2)

# Converts a string for ISO8601 format to a human readable string
def ISO8601ToHumanTime(string):
    #print(string)
    inputTime = string[:26] + string[27:]
    #print(inputTime)
    temp = datetime.strptime(inputTime, "%Y-%m-%dT%H:%M:%S.%f%z")
    return temp

# Takes an input in Celsius and converts it to Fahrenheit
def celsiusToFahrenheit(number):
    return round(number*1.8 + 32)

# Takes an input in km/h and converts it to m/s
def kmPerHourToMetersPerSecond(number):
    return round(number*0.2777782, 2)