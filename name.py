#Jackson Eubank
#CS362
#HW4 - Full Name

def getFullName(first,last):
    if (len(first) == 0):
        raise ValueError("Recieved an empty array for a first name!");
    if (len(last) == 0):
        raise ValueError("Recieved an empty array for a last name!");
    for x in first:
        if(first.isdigit()):
            raise TypeError("First name cannot be made of numbers!");
    for x in last:
        if(last.isdigit()):
            raise TypeError("Last name cannot be made of numbers!");
    return first + " " + last;
