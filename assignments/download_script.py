# Write a program download_script.py, which downloads a set of files from the internet. 
# The files to download are given as arguments to your program on the command-line as illustrated in the following:

# $ python download_script.py http://www.gutenberg.org/files/2701/2701-0.txt 
# http://www.gutenberg.org/cache/epub/27525/pg27525.txt
# Downloading file to ./2701-0.txt
# Downloading file to ./pg27525.txt
# Reuse your webget module from exercises in 07-Functions and Modules.

# Modify the above program, so that it can download a list of files from stdin. That is, so that you can reuse the output of one CLI command as input to your program.

#$ cat list_of_files.txt | python download_script.py

import sys
from urllib.parse import urlparse
import logging
import os
import webget

log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_fmt)

exstensions = ('.csv', '.txt')


def check_args(arguments):
    for arg in arguments:
        filename = os.path.basename(arg)
        if filename.endswith(exstensions):
            return True
        
    return False


def run(arguments):
    if check_args(arguments):
        for idx, argument in enumerate(arguments):
            logging.info('{} argument is {}'.format(idx, argument))
            webget.download(argument.rstrip())
    else:
        print('Usage: python your_script.py arg_1 [arg_2 ...]')


if __name__ == '__main__':
    # Call me from the CLI for example with:
    # python your_script.py arg_1 [arg_2 ...]
    if len(sys.argv) > 1:
        run(sys.argv[1:])
    
    input_lines = sys.stdin.readlines()
    print(input_lines)
    run(input_lines)