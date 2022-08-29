import pytest
from data_structures.hashtable import Hashtable
'''
Setting a key/value to your hashtable results in the value being in the data structure
Retrieving based on a key returns the value stored
Successfully returns null for a key that does not exist in the hashtable
Successfully returns a list of all unique keys that exist in the hashtable
Successfully handle a collision within the hashtable
Successfully retrieve a value from a bucket within the hashtable that has a collision
Successfully hash a key to an in-range value
'''



def test_exists():
    assert Hashtable

def test_null_key():
    pass

def test_contains():
    table = Hashtable()
    table.set('apple', 'banana')
    actual = table.contains('apple')
    expected = True
    assert actual == expected

def test_contains_multiple():
    table = Hashtable()
    table.set('apple', 'banana')
    table.set('attack', 'defend')
    actual = table.contains('attack')
    expected = True
    assert actual == expected


def test_keys():
    table = Hashtable()
    table.set('apple', 'banana')
    table.set('attack', 'defend')
    keys = table.keys()
    actual = keys
    expected = ['apple', 'attack']
    assert actual == expected



def test_get():
    table = Hashtable()
    table.set('apple', 'banana')
    actual = table.get('apple')
    expected = 'banana'
    assert actual == expected


