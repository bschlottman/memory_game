""" Tests for memory.py """

from subprocess import getstatusoutput
import os
import re


PRG = './memory.py'



# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)