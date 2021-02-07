#Jackson Eubank
#CS362
#HW4 - Array

def getAverage(x):
    z = 0;
    if (len(x) == 0):
        raise ValueError("Unable to get the average of an empty array!");
    for y in x:
        if not str(y).isdigit():
            raise TypeError("Non-real number " + "'" + y + "'" + " in array!");
        z = z + y;
    return z / len(x);
