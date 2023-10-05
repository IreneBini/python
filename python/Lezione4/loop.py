import time

import numpy as np

N = 100



start_time = time.time()
l = []
for i in range(N): # for loop is slower in python
    l.append(i**2) 
elapsed_time = time.time() - start_time
#print(l)
print('pure-python: ', elapsed_time)

#I have vectorized the problem -> speed up python
# another way to speed up python is 
start_time = time.time()
a = np.arange(N)**2 # easy enought and more speedy when N become very very high
elapsed_time = time.time() - start_time
#print(l)
print('numpy: ', elapsed_time)