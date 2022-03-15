import pytest
from hashtable import HashTable
from hashmap_repeated_word import hashmap_repeated_word

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

def test_empty_repeated_word():
    assert hashmap_repeated_word("No repeated words") == None

def test_simple_sentence():
    assert hashmap_repeated_word("Once upon a time, there was a brave princess who...") == "a"

def test_a_tale_of_two_cities():
    assert hashmap_repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"

