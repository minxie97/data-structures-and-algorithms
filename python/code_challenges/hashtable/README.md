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
