file = open('values.txt', 'r')
values = file.read().split('\n')
file.close()
values = [int(i) for i in values[:-1]]
#target = 1.0471 * (10**13)
num_iters = 20
K = 607252935
from math import *
def calcCordic(target):
    
    cos,sin = K,0
    angle = 0
    for i in range(num_iters):
    #print(cos*(1/((10**(13)))), sin*(1/((10**(13)))))
        if angle < target:
            angle += values[i]
            temp = cos
        #cos += -(sin * (2**(-i)))
            cos += -(sin >> i)
        #sin += temp * (2**(-i)) 
            sin += temp >> i
        else:
            angle -= values[i]
            temp = cos
        #cos += sin * (2**(-i))
            cos += sin >> i
        #sin += -(temp * (2**(-i)))
            sin += -(temp >> i)
    return ['0.'+str(cos), '0.'+str(sin)]
