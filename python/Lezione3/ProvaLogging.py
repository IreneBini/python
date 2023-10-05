import logging

logging.basicConfig(level=logging.INFO) #this line is necessary because without this, the info messages are not wrote on terminal

logging.warning('This is a warning')
logging.error('This is an error')

file_path = 'pg1497.txt'

logging.info(f'Opening input file {file_path}...')
data = open(file_path).read() # apre il libro come file di lettura
logging.info(f'Done, {len(data)} character(s) found.') # stampo il numero di caratteri