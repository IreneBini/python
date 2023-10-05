import math

def check_float_equal(x, y, tollerance = 10**(-11)):
    return math.fabs(x-y) < tollerance
    
a = 0.1 + 0.2
print(check_float_equal(a, 0.3))



# poi scrivi python floats.py

