from hashtable.hashtable import HashTable
from hashmap_left_join.hashmap_left_join import hashmap_left_join
import pytest

def test_left_join(table_left, table_right):
    hashmap_left_join(table_left, table_right)
    assert table_left.get("diligent") == ["employed", "idle"]
    assert table_left.get('fond') == ['enamored', 'adverse']
    assert table_left.get('guide') == ['usher', 'follow']
    assert table_left.get('outfit') == ['garb', None]
    assert table_left.get('wrath') == ['anger', 'delight']
    assert table_left.get('empty') == None

def test_left_empty(table_right):
    table_left = HashTable()
    hashmap_left_join(table_left, table_right)
    assert table_left.get("diligent") == None
    assert table_left.get('fond') == None
    assert table_left.get('guide') == None
    assert table_left.get('outfit') == None
    assert table_left.get('wrath') == None

def test_right_empty(table_left):
    table_right = HashTable()
    hashmap_left_join(table_left, table_right)
    assert table_left.get("diligent") == ["employed", None]
    assert table_left.get('fond') == ['enamored', None]
    assert table_left.get('guide') == ['usher', None]
    assert table_left.get('outfit') == ['garb', None]
    assert table_left.get('wrath') == ['anger', None]

@pytest.fixture
def table_left():
    left = HashTable()
    left.set("diligent", "employed")
    left.set("fond", "enamored")
    left.set("guide", "usher")
    left.set("outfit", "garb")
    left.set("wrath", "anger")
    return left

@pytest.fixture
def table_right():
    right = HashTable()
    right.set("diligent", "idle")
    right.set("fond", "adverse")
    right.set("guide", "follow")
    right.set("flow", "jam")
    right.set("wrath", "delight")
    return right
