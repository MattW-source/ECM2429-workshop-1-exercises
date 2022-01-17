import pytest
from properties import Person

def test_getname():
    ''' 
    Ensure name returned the same as set in the constructor?
    '''
    michael = Person("Michael", 21)
    assert michael.name == "Michael"

def test_noname():
    '''
    Do not allow an invalid name, empty string or None
    '''
    # This is a bad idea -
    # noname = Person("", 0)
    # assert noname.name == ""
    # Instead let's expect an exception for
    # empty string, or None
    with pytest.raises(ValueError):
        noname = Person("", 0)

