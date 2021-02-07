#Jackson Eubank
#CS362
#HW4 - Cube

#input
def cubeVolume(x):
    if (x <= 0):
        raise ValueError("Can't get volume from a cube with dimensions less than or equal to zero!");
    return(x*x*x);
