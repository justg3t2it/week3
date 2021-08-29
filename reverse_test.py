import pytest
from reverse import reverseReverse

def testFirst():
    assert reverseReverse("123") == "321"

def testSecond():
    assert reverseReverse("0") == "0"

def testThird():
    assert reverseReverse("3,200") == "23"

def testFourth():
    assert reverseReverse("123,4") == "432,1"

