""" Tests for memory.py """

#from subprocess import getstatusoutput
import os
#import re


PRG = './memory.py'



# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)

# --------------------------------------------------
def test_input():
    """ ensure the game gives back the initial string to begin """

    