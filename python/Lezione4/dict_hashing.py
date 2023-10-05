# hash() is a built-in function in python -> it means that it does not need library to be used

print(hash(3)) # print the key that corrisponds to 3
print(hash(3.)) # print the key that corrisponds to 3.

d = {} # create a dictionary

d[3] = 'Hi there!' # assign that string to the key 3
print(d)

d[3.] = 'How are you?' # assign that string to the key 3 and delete the previous one
print(d)
