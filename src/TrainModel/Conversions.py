# File for converting units to imperial before outputting them
help(round)

# Takes an input in Meters and converts it to Feet
def metersToFeet(number):
    return round(number * 3.28084, 3)

# Takes an input in Kilometers and converts it to Miles
def kilometersToMiles(number):
    return round(number * 0.621371, 3)

# Takes an input in Kilograms and converts it to US Tons
def kilogramsToTons(number):
    return round(number * 0.00110231, 3)

# Takes an input in Meters Per Second and converts it to Miles Per Hour
def metersPerSecondToMilesPerHour(number):
    return round(number * 2.23695, 3)

# Takes an input in Meters Per Second ^2 and conerts it to Feet Per Second ^2
def metersPerSecondSquaredToFeetPerSecondSquared(number):
    return round(number * 3.28084, 3)

# Takes an input in Watts and converts it to Horsepower
def wattsToHorsepower(number):
    return round(number * 0.00134102, 3)