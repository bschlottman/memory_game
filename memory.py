#!/usr/bin/env python3
"""
Author : bschlottman <bschlottman@email.arizona.edu>
Date   : 2021-11-16
Purpose: test your memory
"""

import argparse
import os
import random
import string


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
        parser.error('Input string must be 4 characters long')
    return args


# --------------------------------------------------
def test_input():
    """ensure the game gives back the initial string to begin"""

    assert validate_input('foo') == False
    assert validate_input('food') == True
    assert validate_input('foods') == False


# --------------------------------------------------
def validate_input(text: str) -> bool:
    """ensure the game gives back the initial string to begin"""

    if len(text) != 4:
        print('Input string must be 4 characters long', file=sys.stderr)
        return False

    return True


# --------------------------------------------------
def memgame(a_str):
    """given good input, the program will generate
        a new str on a new line and blank out the old string"""

    all_chars = a_str
    letters = string.ascii_lowercase

    while True:
        usr_input = input(a_str + ' ')  # include a space between strings
        if usr_input != all_chars:  # if user input != the strings, print the fail message
            print('LOL, You failed!')
            break  # exit loop
        new_chars = gen_string(4)
        a_str = new_chars
        all_chars += ' ' + new_chars  # join the old and new strings, w/ space between
        os.system('cls' if os.name == 'nt' else
                  'clear')  # clear the old line in terminal so users wont see


# --------------------------------------------------
def gen_string(n: int) -> str:
    """ Generate a new string of N chars """

    return ''.join([random.choice(string.ascii_lowercase) for i in range(n)])


# --------------------------------------------------
def test_gen_string() -> None:
    """ Test gen_string """

    prev_state = random.getstate()
    random.seed(1)
    assert gen_string(0) == ''
    assert gen_string(1) == 'a'
    assert gen_string(2) == 'ab'
    random.setstate(prev_state)


# --------------------------------------------------
def main():
    """bring in a new random string on a new line,
        & replace old line with | | | | |, keeping line position"""

    args = get_args()
    memgame(args.string)


# --------------------------------------------------
if __name__ == '__main__':
    main()