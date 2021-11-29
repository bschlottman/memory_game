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
def test_input():
    """ensure the game gives back the initial string to begin"""
    args = get_args
    if len(args.string) != 4:
        assert print(f'Input string must be 4 characters long')

# --------------------------------------------------
def memgame(a_str):
    """given good input, the program will generate 
        a new str on a new line and blank out the old string"""

    all_chars = a_str
    letters = string.ascii_lowercase

    while True:
        usr_input = input(a_str + ' ')  # include a space between strings
        if usr_input != all_chars:  # if user input doesn't equal the strings, print the fail message
            print('LOL, You failed!')
            break  # exit loop
        new_chars = ''.join([random.choice(letters) for i in range(4)
                             ])  # generate random str of 4 chars
        a_str = new_chars
        all_chars += ' ' + new_chars  # join the old and new strings, w/ space between
        os.system('cls' if os.name == 'nt' else
                  'clear')  # clear the old line in terminal so users wont see


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
