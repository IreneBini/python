import numpy as np

a1 = np.array([1., 2.]) #array
a2 = np.array([[1., 2.], [3., 4.]]) # matrix -> in every [ ] I write the rows
aa = np.array(a2).T # transpose array of a1
c = np.pi # pi greco

print(a1)
print(a2)
print(aa)
print(c)
print(a1 * a1) # first colomn is multiply by the first column and second column by the second 
               #So we can multiply arraies only if they have same number of columns
               # it works like that also with other operation

print(a1 * c) # multiply any singol enement by c
print(a1 * a2) # first element of a1 is multiplied by first matrix's column (1 and 3)

d = np.exp(a2) # sostituisce gli elementi di a2 con il loro esponenziale -> same shape
e = a1 * d 
f = np.power(a1, a2) # a è la base e a2 è l'esponente -> 1^1, 2^2, 1^3, 2^4

print(d)
print(e)
print(f)

# Can I do the mean of something without use loops ?
a3 = np.random.normal(size=(10, 5)) # pseudo random generator -> array with 10 rows and 5 columns
np.mean(a3) # do the mean of all the elements of array
np.mean(a3, axis = 1) # do the mean along rows
np.mean(a3, axis = 0) # do the mean along columns

# Extract element by arrays
z = a3[0, 0] # give the element 0,0 of the array
y = a3[0] # give the entire row -> because it is a matrix
w = a3[:, 0] # give the entire column 


a4 = np.arange(16) # give an array of all the integers from 0 to 15
a5 = np.arange(16).reshape((4, 4)) # change the shape -> become a 4x4 matrix

# how can I extraxt a small squae in the middle of a matrix ?
a6 = a5[1:3, 1:3] # the maximum is always excluded -> it takes only 1 and 2
a7 = a5[:3, :3] # it takes 0, 1 and 2

print(a6)
print(a7)