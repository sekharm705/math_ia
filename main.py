import cordic
import taylor
import math
def testTaylor():
    for i in range(1,20000):
        s = i*(10**(-13))
        val = taylor.calcTaylor(math.pi/(2*i))
def testCordic():
    for i in range(1,20000):
        s = i*(10**(-13))
        val = cordic.calcCordic(math.pi/(2*s))
import timeit
print(timeit.timeit(lambda:testTaylor(), number = 1))
print('Taylor expansion ^')
print(timeit.timeit(lambda:testCordic(), number = 1))
print('CORDIC algorithm ^')
