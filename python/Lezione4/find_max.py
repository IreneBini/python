# how many fondamental instructions is this code executing? 
    # 1 assignment
    # 1 list look up before the loop
    # 1 look up, 1 assignment and 1 comparison for each iteration -> 3*(n-1)
    # a variable number of assignments -> between 0 to n-1
    # 1 final return instruction
# min = 1+1+3*(n-1)+0+1 = 3n
# max = 1+1+3*(n-1)+(n-1)+1 = 4n-1
# average = (3n + 4n-1)/2 = (7n-1)/2

# how much time it takes ? it depends on the input data, different computer, ram, ...

def find_maximum(list_):
    """Find the biggest element in a list.
    """
    maximum = list_[0] # assign that value to a local variable 
    for value in list_[1:]: # looping all the list
        if value > maximum:
            maximum = value
    return maximum # function's output

l = [1, 2, 5, 98, 3, 1672, 6, 34, 651]
print(find_maximum(l))
