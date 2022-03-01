# Insertion Sort

## Pseudocode
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

## Trace
sample array: `[8,4,23,42,16,15]`

### Step 1
starting state: `[8,4,23,42,16,15]`

* i is set to 1
* j is set to i-1 which is 0
* temp is set to the array[i] or array[1] `4`
* while j `0` >= 0 (TRUE) and temp `4` < array[j] `8` (TRUE)
  * array[j + 1] or array[1] is set to array[j] `8`
  * j is set to j - 1 which is -1
* loop ends since j >= 0 is no longer true
* array[j + 1] or array[0] is set to temp `4`

ending state: `[4,8,23,42,16,15]`

![step1](https://github.com/minxie97/data-structures-and-algorithms/blob/insertion-sort/python/code_challenges/sorts/insertion-sorts/step1.JPG)

### Step 2
starting state: `[4,8,23,42,16,15]`

* is is set to 2
* j is set to i - 1 which is 1
* temp is set to array[i] or array[2] `23`
* while j `1` >= 0 (TRUE) and temp `23` < array[j] `8` (FALSE)
* while loop doesn't run
* array[j + 1] or array[2] is set to temp `23`

ending state: `[4,8,23,42,16,15]`

![step2](https://github.com/minxie97/data-structures-and-algorithms/blob/insertion-sort/python/code_challenges/sorts/insertion-sorts/step2.JPG)

### Step 3
starting state: `[4,8,23,42,16,15]`

* i is set to 3
* j is set to i - 1 which is 2
* temp is set to array[i] or array[3] `42`
* while j `2` >= 0 (TRUE) and temp `42` < array[j] `23` (FALSE)
* while loop doesn't run
* array[j + 1] or array[3] is set to temp `42`

ending state: `[4,8,23,42,16,15]`

![step3](https://github.com/minxie97/data-structures-and-algorithms/blob/insertion-sort/python/code_challenges/sorts/insertion-sorts/step3.JPG)

### Step 4
starting state: `[4,8,23,42,16,15]`

* i is set to 4
* j is set to i - 1 which is 3
* temp is set to array[i] or array[4] `16`
* while j `3` >= 0 (TRUE) and temp `16` < array[j] `42` (TRUE)
  * array[j + 1] or array[4] is set to array[j] `42`
  * j is set to j - 1 which is 2
* while j `2` >= 0 (TRUE) and temp `16` < array[j] `23` (TRUE)
  * array[j + 1] or array[3] is set to array[j] `23`
  * j is set to j - 1 which is 1
* while j `1` >= 0 (TRUE) and temp `16` < array[j] `8` (FALSE)
* while loop ends
* array[j + 1] or array[2] is set to temp `16`

ending state: `[4,8,16,23,42,15]`

![step4](https://github.com/minxie97/data-structures-and-algorithms/blob/insertion-sort/python/code_challenges/sorts/insertion-sorts/step4.JPG)

### Step 5
starting state: `[4,8,16,23,42,15]`

* i is set to 5
* j is set to i - 1 which is 4
* temp is set to array[i] or array[5] `15`
* while j `4` >= 0 (TRUE) and temp `15` < array[j] `42` (TRUE)
  * array[j + 1] or array[5] is set to array[j] `42`
  * j is set to j - 1 which is 3
* while j `3` >= 0 (TRUE) and temp `15` < array[j] `23` (TRUE)
  * array[j + 1] or array[4] is set to array[j] `23`
  * j is set to j - 1 which is 2
* while j `2` >= 0 (TRUE) and temp `15` < array[j] `16` (TRUE)
  * array[j + 1] or array[3] is set to array[j] `16`
  * j is set to j - 1 which is 1
* while j `1` >= 0 (TRUE) and temp `15` < array[j] `8` (FALSE)
* while loop ends
* array[j + 1] or array[2] is set to temp `15`

ending state: `[4,8,15,16,23,42]`

![step5](https://github.com/minxie97/data-structures-and-algorithms/blob/insertion-sort/python/code_challenges/sorts/insertion-sorts/step5.JPG)

## Efficiency

* Time: time-wise, the code has an O(N^2) efficiency. The worst-case scenario would be sorting a reverse sorted list. In this scenario, the while loop inside the for loop would run every loop in the for loop. The while loop would start with just one loop in the first loop of the for loop, but as the function continues, the while loop will run more and more loops as the integers on the left will need to move more spaces to the right. The longer the list, the more the loop inside the loop will run.
* Space: O(1). No new array is being created, just being altered in place. 
