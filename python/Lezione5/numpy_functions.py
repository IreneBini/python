import numpy as np
import math

a = np.array([0.1, 1., 10.])

print(np.log10(a))
print(np.exp(a))
print(np.sin(a))
print(np.log10(0.1))

print(math.log10(0.1)) # no error
# the next line is an error -> math library does not work with array, but only with numbers
print(math.log10(a)) 