
s = input("Enter a word: ")

def letter_frequency(s):
    t = s.lower() # return a lowercase string from the given string
    Alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    for i in range(len(Alphabet)):
        b = t.count(Alphabet[i]) # returns the number of times an object appears in a list
        print("{} -- {}".format(Alphabet[i], b))

letter_frequency(s)


