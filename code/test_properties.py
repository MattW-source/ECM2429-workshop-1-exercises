import pytest
from properties import Person

def test_getname():
    ''' 
    Ensure name returned the same as set in the constructor?
    '''
    michael = Person("Michael", 21)
    assert michael.name == "Michael"

def test_setname():
    '''
    Ensure we can set the name of a Person object
    '''
    michael = Person("Micheal", 21)
    michael.name = "Bob"
    assert michael.name == "Bob"

def test_intname():
    '''
    Do not allow an integer name
    '''
    michael = Person("Micheal", 21)
    with pytest.raises(ValueError):
        michael.name = 1

def test_setintname():
    '''
    Do not allow an integer name
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
         michael.name = 1

def test_noname():
    '''
    Do not allow an invalid name, empty string or None
    '''
    # This is a bad idea -
    # michael = Person("", 0)
    # assert michael.name == ""
    # Instead let's expect an exception for
    # empty string, or None
    with pytest.raises(ValueError):
        michael = Person("", 0)
    with pytest.raises(ValueError):
        michael = Person(None, 0)

def test_setnoname():
    '''
    Do not allow an invalid name, empty string or None
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
         michael.name = ""
    with pytest.raises(ValueError):
         michael.name = None

def test_getage():
    '''
    Ensure age returned the same as set in the constructor?
    '''
    michael = Person("Michael", 21)
    assert michael.age == 21

def test_setage():
    '''
    Ensure we can set the age of a Person object
    '''
    michael = Person("Michael", 21)
    assert michael.age == 21
    michael.age = 25
    assert michael.age == 25

def test_negativeage():
    '''
    Do not allow a negative age
    '''
    with pytest.raises(ValueError):
        michael = Person("Michael", -420)

def test_setnegativeage():
    '''
    Do not allow a negative age
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
        michael.age = -420

def test_stringage():
    '''
    Do not allow a string age
    '''
    with pytest.raises(ValueError):
        michael = Person("Michael", "Twenty-One")

def test_setstringage():
    '''
    Do not allow a string age
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
        michael.age = "Twenty-One"

def test_floatage():
    '''
    Do not allow a floating point age
    '''
    with pytest.raises(ValueError):
        michael = Person("Michael", 1.1)

def test_setfloatage():
    '''
    Do not allow a floating point age
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
        michael.age = 1.1

def test_noage():
    '''
    Do not allow an invalid age, empty string or None
    '''
    with pytest.raises(ValueError):
        michael = Person("Michael", None)

def test_setnoage():
    '''
    Do not allow an invalid age, empty string or None
    '''
    michael = Person("Michael", 21)
    with pytest.raises(ValueError):
        michael.age = None
