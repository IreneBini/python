import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# accumulate attribute will be either the sum() function, if --sum was specified at the 
# command line, or the max() function if it was not

args = parser.parse_args() # return an object with 2 attributes (integers and accumulate)
print(args.accumulate(args.integers))