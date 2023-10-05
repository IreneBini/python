# This program prints the relative frequence of each letter of the alphabet 
# (without distinguishing between lower and upper case) in the book.

import argparse
import time 

import logging

# I create some functions
def letter_frequency(s, file_path):
    """ 

    """
    t = s.lower() # return a lowercase string from the given string
    Alphabet = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
    ]
    total_letter = 0
    count_letter = []

    logging.info(f'Let us start counting frequencies of each letter in {file_path}')
    for i in range(len(Alphabet)):
        b = t.count(Alphabet[i]) # returns the number of times an object appears in a list
        logging.info(f'{Alphabet[i]} -- {b}')
        count_letter.append(b)

        # total letter count to build histogram
        total_letter = total_letter + b


def process_file(file_path):
    """ Process one file and count the occurences of each characters

    Arguments
    ------------
    file_path : str
        path to the input file.
    


    """
    logging.info(f'Opening input file {file_path}...')
    data = open(file_path).read() # open in reading mode the file
    logging.info(f'Done, {len(data)} character(s) found.') #say how many character there are
    letter_frequency(data, file_path)


# Let the time start to measured
start = time.time()

# necessary to able the info to be write on the terminal
logging.basicConfig(level=logging.INFO)

# esplicate what the program does (program name and description)
parser = argparse.ArgumentParser(prog='wordcount', 
                                 description='Count the letter frequency in a text')

# first argument added
parser.add_argument('count', help='open a file and count the characters')

file_data= 'pg1497.txt'


# the program accepts the path to the input file from the command line
if __name__ == '__main__': # è vero se esegui dalla linea di comando
    args = parser.parse_args() # return an object with one attribute (count)
    process_file(file_data) # call the function


# Stop to measured time
stop = time.time()

elapsed_time = stop - start

logging.info(f'The elapsed time is {elapsed_time} s') 
