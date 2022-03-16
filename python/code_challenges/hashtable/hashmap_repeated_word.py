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
