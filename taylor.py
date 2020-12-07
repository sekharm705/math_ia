import math
def calcTaylor(x):
    sin = 1
    cos = 1
    xMinusPiBy4 = x - math.pi/4
    oneByRootTwo = 1/math.sqrt(2)
    term = 1
    for i in range(1,14):
        term = term * (xMinusPiBy4/i)
        modFour = i%4
        if modFour == 1 or modFour == 2:
            cos -= term
        else:
            cos += term
        if modFour == 2 or modFour == 3:
            sin -= term
        else:
            sin += term
    cos *= oneByRootTwo
    sin *= oneByRootTwo
    return cos, sin
