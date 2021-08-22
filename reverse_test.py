import pytest
from reverse import reverseReverse

def testFirst():
    assert reverseReverse(123) == 321

def testSecond():
    assert reverseReverse(0) == 0

def testThird():
    assert reverseReverse(2,400) == 4,2

def testFourth():
    assert reverseReverse(11,245.2) == 2,542.1

