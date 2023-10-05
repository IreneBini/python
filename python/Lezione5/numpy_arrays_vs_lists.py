import numpy as np

# arrays and lists seem similar...
l = [1., 2., 3.]
a = np.array(l)
print(l)
print(a)

# ...but they support basic arithmetic in a different fashion
print(l + l) # concatenation of this 2 list -> it becomes a six elements' list
print(a + a) # sum the elements -> at the end we have again a 3 elements' array
