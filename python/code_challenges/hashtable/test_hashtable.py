import pytest
from hashtable import HashTable

def test_setting():
    test = HashTable()
    test.set("testkey", "testvalue")
    assert test.contains("testkey") == True

def test_get_value():
    test = HashTable()
    test.set("testkey", "testvalue")
    assert test.get("testkey") == "testvalue"

def test_get_none():
    test = HashTable()
    test.set("testkey", "testvalue")
    assert test.get("badkey") == None
    empty = HashTable()
    assert empty.get("abc") == None

def test_all_keys():
    test = HashTable()
    test.set("a", 1)
    test.set("b", 2)
    test.set("c", 3)
    for key in test.keys():
        assert test.contains(key) == True

def test_handle_collision():
    test = HashTable()
    test.set("abc", 1)
    test.set("cba", 2)
    assert test.hash("abc") == test.hash("cba")
    assert test.table[test.hash("abc")].key == "abc"
    assert test.table[test.hash("abc")].next.key == "cba"

def test_retrieve_collision_value():
    test = HashTable()
    test.set("abc", 1)
    test.set("cba", 2)
    test.set("bca", 3)
    assert test.get("abc") == 1
    assert test.get("cba") == 2
    assert test.get("bca") == 3

def test_hash_range():
    test = HashTable()
    index = test.hash("a;lsdfjfbnlk;asjfks;dlnvaskjasl;odfcipqjoasdgj09qw uopjpjfjs")
    assert 0 <= index <= 1023
