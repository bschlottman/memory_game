""" Tests for memory.py """

from subprocess import getstatusoutput
import os
Import re


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


# --------------------------------------------------
def test_no_args():
    """ Dies on no args """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_missing_input():
    """ Dies on missing input """

    rv, out = getstatusoutput('{} -c codons.RNA'.format(PRG))
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)
