import numpy as np

# Initialization from a list
a1 = np.array([1., 2., 3])
print(a1)

# Zeros, ones, and fixed values
a2 = np.zeros(10)
a3 = np.ones((2, 2)) # same that a11 -> it does not matter to write 'shape'
a4 = np.full(7, 3.) # 7 are the rows and 3 are the columns
print(a2)
print(a3)
print(a4)

# Grids
a5 = np.linspace(0., 10., 11)
a6 = np.logspace(0., 3, 4) # da 10^0 a 10^3 spaziato logaritmicamente in 4 elementi
a7 = np.geomspace(1., 1000., num=5) # da 1 (non accetta lo 0) a 1000 spaziato logaritmicamente in 5 elementi
                                    # se non inserisco num = n, allora mette di default 50
                                    # se aggiungo anche endpoint = false, allora non considera il numero finale
a8 = np.geomspace(1., 10000., num=5, endpoint=True) # di default è true, quindi non ha senso scriverlo
a9 = np.geomspace(1., 10000., num=4, endpoint=False)


print(a5)
print(a6)
print(a7)
print(a8)
print(a9)

a10 = np.ones(shape=(2))  # array composed by 2 element
a11 = np.ones(shape=(2,2)) # array composed by 2 array with 2 element (2x2 matrix)
a12 = np.ones(shape=(2,2,2)) # array composed by 2 array composed by 2 array with 2 element
a13 = np.ones(shape=(2,2,2,2)) # array composed by 2 array composed by 2 array composed by 
                               # 2 array with 2 element
print(a10)
print(a11)
print(a12)
print(a13)