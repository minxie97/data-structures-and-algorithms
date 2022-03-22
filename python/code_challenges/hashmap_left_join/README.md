# Hashmap LEFT JOIN
mplement a simplified LEFT JOIN for 2 Hashmaps.

## Challenge
Write a function that LEFT JOINs two hashmaps into a single data structure. Takes in a left hashmap that has word strings as keys, and a synonym of the key as values and a right hashmap that has word strings as keys, and antonyms of the key as values.

## Approach & Efficiency
Given my hashtable implementation, the approach was fairly simple. I was able to call the set method and give that method the same key and a list of the left table value and right table value. This allowed me to simply update the key in the left table in accordance with left join logic.
Time complexity of O(N) as the loop/times set is called will increase as the left table grows larger
Space complexity is O(1) as I will be modifying the left table in place.

## Solution
![left-join-whiteboard](https://github.com/minxie97/data-structures-and-algorithms/blob/hashmap-left-join/python/code_challenges/hashmap_left_join/hashmap_left_join.jpg)
