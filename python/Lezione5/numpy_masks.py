import numpy as np

a = np.linspace(0., 10., 11)
print(a)
print(a.dtype) # type of a's elements
print(a.shape) #print how a is long
print(id(a)) # print the first address of a, or the only one if a is a single variable

b = np.flip(a) # array with the same element of a but take that from the end to the begin
print(b)

c = np.clip(a, 3., 8.) # overwrite the elements of a that are lower of 3 or higher of 8
                         # with the min (3) and max (8.) value respectly
print(c)

# array compared with a number
mask1 = a >= 2.5 # binary comparison -> produced an other array which for each position give 
                 # if it is true or false
mask2 = a < 8.5

print(mask1) # print an array with only true or false
print(mask2)
print(a[mask1]) # print the only element corrisponding to the true of mask1
print(a[mask2])
print(a[np.logical_and(mask1, mask2)]) # print the only element that are true both in 
                                       # mask 1 and mask 2

# array compared with another array -> must have same shape
d = np.array([1., 33, -5.6, 4., -1., 0., 11., -9., 39., 3., 12.1])
mask3 = a >= d

print(mask3)
print(a[mask3])
print(d[mask3])