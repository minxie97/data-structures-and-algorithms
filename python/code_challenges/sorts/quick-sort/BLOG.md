# Quick Sort

## Pseudo Code
```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```
## Trace
sample array: [8, 4, 23, 42, 16, 15]
left = beginning of array = 0
right = end of array = 5

* to begin, we call quicksort using the sample array. the left is set to be the index at the beginning of the array and the right is set to be the index at the end. quicksort([8, 4, 23, 42, 16, 15], 0, 5)

  * define the position. we call partition using the sample array, left, and right as arguments. partition([8, 4, 23, 42, 16, 15], 0, 5)
    * set pivot value to the sample array at index of right, `arr[5]`, which is equal to 15
    * set a low value to be left - 1 which is -1
    * for i in range left to right (0 to 5)
      * if the array at index i is less than or equal to the the pivot value `15`, then we add one to low and swap the values in the array at index low and i
        * loop 1: since arr[0] `8` is less than 15
          * low + 1 = 0
          * swap(arr, 0, 0)
          * arr = [8, 4, 23, 42, 16, 15]
        * loop 2: since arr[1] `4` is less than 15
          * low + 1 = 1
          * swap(arr, 1, 1)
          * arr = [8, 4, 23, 42, 16, 15]
        * loop 3: since arr[2] `23` is greater than 15, does not run
          * arr = [8, 4, 23, 42, 16, 15]
        * loop 4: since arr[3] `42` is less than 15, does not run
          * arr = [8, 4, 23, 42, 16, 15]
        * loop 5: since arr[4] `16` is less than 15, does not run
          * arr = [8, 4, 23, 42, 16, 15]
    * swap(arr, right, low+1) or swap(arr, 5, 2)
      * arr = [8, 4, 15, 42, 16, 23]
    * return low + 1 or 2

* position is set to 2
* call quicksort(arr, left, position - 1) or quicksort([8, 4, 15, 42, 16, 23], 0, 1)
  * define the position. partition([8, 4, 15, 42, 16, 23], 0, 1)
    * pivot is set to arr[1] which is 4
    * low is set to left - 1 which is -1
    * for i in range left to right (0 to 1)
      * loop 1: arr[0] `8` is not less than the pivot `4`. does not run
    * swap(arr, right, low+1) or swap(arr, 1, 0)
      * arr = [4, 8, 15, 42, 16, 23]
    * return low+1 or 0
  * call quicksort(arr, left, position - 1) or quicksort([4, 8, 15, 42, 16, 23], 0, -1). this will not run as right is less than left
  * call quicksort(arr, position + 1, right) or quicksort([4, 8, 15, 42, 16, 23], 1, 1). this will not run as left and right are equal

* call quicksort(arr, position + 1, right) or quicksort([4, 8, 15, 42, 16, 23], 3, 5)
  * define the position. partition([4, 8, 15, 42, 16, 23], 3, 5)
    * pivot is set to arr[5] which is 23
    * low is set to left-1 which is 2
    * for i in range left to right (3 to 5)
      * loop 1: arr[3] `42` is greater than pivot `23`. so doesn't run
      * loop 2: arr[4] `16` is less than the pivot `23`
        * low + 1 = 3
        * swap([4, 8, 15, 42, 16, 23], 4, 3)
        * arr = [4, 8, 15, 16, 42, 23]
    * swap(arr, right, low+1) or swap(arr, 5, 4)
      * arr = [4, 8, 15, 16, 23, 42]
    * return low + 1 or 4
  * call quicksort(arr, left, position - 1) or quicksort([4, 8, 15, 16, 23, 42], 3, 3). does not run
  * call quicksort(arr, position + 1, right) or quicksort([4, 8, 15, 16, 23, 42], 4, 5)
    * position = partition([4, 8, 15, 16, 23, 42], 4, 5)
      * pivot is 42
      * low is left - 1 or 3
      * for i range 4 to 5
        * loop 1: arr[4] `23` is less than the pivot `42`
          * low + 1 = 4
          * swap([4, 8, 15, 16, 23, 42], 4, 4)
          * arr = [4, 8, 15, 16, 23, 42]
      * swap(arr, right, low+1) or swap(arr, 5, 5)
        * arr = [4, 8, 15, 16, 23, 42]
      * return low + 1 = 5
    * call quicksort(arr, left, position - 1) or quicksort([4, 8, 15, 16, 23, 42], 4, 4). does not run
    * call quicksort(arr, position + 1, right) or quicksort([4, 8, 15, 16, 23, 42],5, 5). does not run

final: [4, 8, 15, 16, 23, 42]

