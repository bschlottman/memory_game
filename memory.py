#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-16
Purpose: test your memory
"""

import argparse, os, random, string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find out if your memory works',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('string',
                        metavar='str',
                        help='Initial str of length 4')
    # parser error if an initial str of length 4 is not given
    args = parser.parse_args()

    if len(args.string) != 4:
        parser.error(f'Input string must be 4 characters long')

    return args


# --------------------------------------------------
def memgame(a_str):
    """"""

    # carriage return: \r (character returns to beginning of line after print)
    all_chars = a_str
    letters = string.ascii_lowercase
    
    while True:
        usr_input = input(a_str + ' ')
        if usr_input != all_chars:
            print('You failed!')
            break
        new_chars = ''.join([random.choice(letters) for i in range(4)])
        a_str = new_chars
        all_chars += ' ' + new_chars
        os.system('cls' if os.name == 'nt' else 'clear')


# --------------------------------------------------
def main():
    """bring in a new random string on a new line, 
        & replace old line with | | | | |, keeping line position"""

    args = get_args()
    memgame(args.string)

    # printing lowercase
    #letters = string.ascii_lowercase
    #print ( ''.join(random.choice(letters) for i in range(10)) )
    #for args.positional:
    #   print(args.positional) if args.positional is > str[:6]


# --------------------------------------------------
if __name__ == '__main__':
    main()
