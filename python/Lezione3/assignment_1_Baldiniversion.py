
import argparse 

import logging

parser = argparse.ArgumentParser(prog='wordcount', description='Count the letter frequency in a text')
parser.add_argument('infile')


def process_file(file_path):
    """
    """
    logging.info(f'Opening input file {file_path}...')
    data = open(file_path).read()
    logging.info(f'Done, {len(data)} character(s) found.')


if __name__ == '__main__':
    args = parser.parse_args()
    process_file(args.infile)