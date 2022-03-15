# Hashtables

## Challenge
Create a `HashTable` class with `set()`, `get()`, `contains()`, `keys()`, and `hash()` methods.

## Approach & Efficiency
Hashing works by getting the sum of the ascii value of each character in the key string, multiply that sum by 599, and then modulo by the size of the hashtable to get an index.

Collisions were handled by implementing a linked list for keys that have the same index. If we get a collision, we can go to that index, traverse the linked list, and find what we are looking for.

## Methods
* set
    * Arguments: key, value
    * Returns: nothing
    * This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
    * Should a given key already exist, replace its value from the value argument given to this method.
* get
    * Arguments: key
    * Returns: Value associated with that key in the table
* contains
    * Arguments: key
    * Returns: Boolean, indicating if the key exists in the table already.
* keys
    * Returns: Collection of keys
* hash
    * Arguments: key
    * Returns: Index in the collection for that key

# Hash Map Repeated Word

## Whiteboard

## Approach and efficiency
The approach was to use a hashtable as a sort of word bank. All we needed to do was to go through the given string and check the words against a word bank. If the word isn't in the bank, then we add it to the bank. If it was in the bank, then upon the very first time we get a match, we return the match.

Time complexity this is a O(N) the loop within the function iterates more as the string is longer.

Space complexity this is also O(N). The hashtable word bank can continually grow if the string a very long and a match isn't quickly found.

## Solution
```
from hashtable import HashTable
import re

def hashmap_repeated_word(string):
    curr_word = ""
    word_bank = HashTable()
    for char in string.lower():
        if re.search(r"[a-z]", char):
            curr_word += char
        elif len(curr_word):
            if word_bank.contains(curr_word):
                return curr_word
            else:
                word_bank.set(curr_word, None)
                curr_word = ""
    if len(curr_word) and word_bank.contains(curr_word):
        return curr_word
    return None
```
