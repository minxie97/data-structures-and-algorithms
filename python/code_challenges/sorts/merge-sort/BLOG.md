# Merge Sort

## Pseudo Code
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace
sample array: [8, 4, 23, 42, 16, 15]

### mergesort([8, 4, 23, 42, 16, 15])
* n is set to arr.length `6`
* n is greater than 1 so continue
* mid = 6//2 = 3
* left is set to [8, 4, 23]
* right is set to [42, 16, 15]

* mergesort(left) or mergesort([8, 4, 23])
  * n is set to arr.length `3`
  * mid = 3//2 = 1
  * left is set to [8]
  * right is set to [4, 23]

  * next comes mergesort(left) or mergesort([8])
    * n is set to arr.length `1`
    * n is not greater than 1 so does not run

  * next comes mergesort(right) mergesort([4, 23])
    * n is set to arr.length 2
    * mid = 2//2 = 1
    * left is set to [4]
    * right is set to [23]

    * mergesort(left) or mergesort([4])
      * n is set to arr.length `1`
      * n is not greater than 1 so does not run
    * mergesort(right) or mergesort([23])
      * n is set to arr.length `1`
      * n is not greater than 1 so does not run

    * merge(left, right, arr) or merge([4], [23], [4, 23])
      * i is set to 0
      * j is set to 0
      * k is set to 0
      * while i < left.length `1` (TRUE) && j < right.length `1` (TRUE)
        * if left[i] `4` <= right[j] `23` (TRUE)
          * arr[k] is set to left[i] `4`
          * i = i + 1 `1`
        * k = k + 1 `1`
      * while loop ends as i < left.length is no longer true
      * i is equal to left.length so remaining values in right are appended to arr
      * arr is set to [4, 23] and is returned

  * merge(left, right, arr) or merge([8], [4, 23], [8, 4, 23])
    * i is set to 0
    * j is set to 0
    * k is set to 0
    * while i < left.length `1` (TRUE) && j < right.length `2` (TRUE)
      * if left[i] `8` <= right[j] `4` (FALSE)
      * else runs
        * arr[k] is set to right[j] `4`
        * j = j + 1 `1`
      * k = k + 1 `1`
      * arr looks like [4, 4, 23]
    * while i < left.length `1` (TRUE) && j < right.length `2` (TRUE)
      * if left[i] `8` <= right[j] `23` (TRUE)
        * arr[k] is set to left[i] `8`
        * i = i + 1 `1`
      * k = k + 1 `2`
      * arr looks like [4, 8, 23]
    * while i < left.length `1` (FALSE) && j < right.length `2` (TRUE)
    * while loop ends as i < left.length is no longer true
    * i is equal to left.length so remaining values in right are appended to arr
    * arr is set to [4, 8, 23] and is returned

* mergesort(right) or mergesort([42, 16, 15])
  * n is set to arr.length `3`
  * n is greater than 1 so continue
  * mid = 3//2 = 3
  * left is set to [42]
  * right is set to [16, 15]
  
  * mergesort(left) or mergesort([42])
    * n is set to arr.length `1`
    * n is not greater than 1 so does not run
  
  * mergesort(right) or mergesort([16, 15])
    * n is set to arr.length `2`
    * n is greater than 1 so continue
    * mid = 2//2 = 1
    * left is set to [16]
    * right is set to [15]
  
    * mergesort(left) or mergesort([16])
      * n is set to arr.length `1`
      * n is not greater than 1 so does not run
  
    * mergesort(right) or mergesort([15])
      * n is set to arr.length `1`
      * n is not greater than 1 so does not run

    * merge(left, right, arr) or merge([16], [15], [16, 15])
      * i is set to 0
      * j is set to 0
      * k is set to 0
      * while i < left.length `1` (TRUE) && j < right.length `1` (TRUE)
        * if left[i] `16` <= right[j] `15` (FALSE)
        * else runs
          * arr[k] is set to right[j] `15`
          * j = j + 1 `1`
        * k = k + 1 `1`
        * arr is currently [15, 15]
      * while loop ends since j is no longer less than right.length
      * since i is not equal to left.length else runs
        * remaining entries in arr set to remaining in left
        * arr is now [15, 16] and is returned

  * merge(left, right, arr) or merge([42], [15, 16], [42, 16, 15])
    * i is set to 0
    * j is set to 0
    * k is set to 0
    * while i < left.length `1` (TRUE) && j < right.length `2` (TRUE)
      * if left[i] `42` <= right[j] `15` (FALSE)
      * else runs
        * arr[k] is set to right[j] `15`
        * j = j + 1 `1`
      * k = k + 1 `1`
      * arr is currently [15, 16, 15]
    * while i < left.length `1` (TRUE) && j < right.length `2` (TRUE)
      * if left[i] `42` <= right[j] `16` (FALSE)
      * else runs
        * arr[k] is set to right[j] `16`
        * j = j + 1 `1`
      * k = k + 1 `1`
      * arr is currently [15, 16, 15]
    * while loop ends since j is no longer less than right.length
    * since i is not equal to left.length else runs
      * remaining entries in arr set to remaining in left
      * arr is now [15, 16, 42] and is returned
  
* merge(left, right, arr) or merge([4, 8, 23], [15, 16, 42], [8, 4, 23, 42, 16, 15])
  * i is set to 0
  * j is set to 0
  * k is set to 0
  * while i < left.length `3` (TRUE) && j < right.length `3` (TRUE)
    * if left[i] `4` <= right[j] `15` (TRUE)
      * arr[k] is set to left[i] `4`
      * i = i + 1 `1`
    * k = k + 1 `1`
    * arr is currently [4, 4, 23, 42, 16, 15]
  * while i < left.length `3` (TRUE) && j < right.length `3` (TRUE)
    * if left[i] `8` <= right[j] `15` (TRUE)
      * arr[k] is set to left[i] `8`
      * i = i + 1 `2`
    * k = k + 1 `2`
    * arr is currently [4, 8, 23, 42, 16, 15]
  * while i < left.length `3` (TRUE) && j < right.length `3` (TRUE)
    * if left[i] `23` <= right[j] `15` (FALSE)
    * else runs
      * arr[k] is set to right[j] `15`
      * j = j + 1 `1`
    * k = k + 1 `3`
    * arr is currently [4, 8, 15, 42, 16, 15]
  * while i < left.length `3` (TRUE) && j < right.length `3` (TRUE)
    * if left[i] `23` <= right[j] `16` (FALSE)
    * else runs
      * arr[k] is set to right[j] `16`
      * j = i + 1 `2`
    * k = k + 1 `4`
    * arr is currently [4, 8, 15, 16, 16, 15]
  * while i < left.length `3` (TRUE) && j < right.length `3` (TRUE)
    * if left[i] `23` <= right[j] `42` (TRUE)
      *  arr[k] is set to left[i] `23`
      *  i = i + 1 `3`
   *  k = k + 1 `5`
   *  arr is currently [4, 8, 15, 16, 23, 15]
  * while loop ends as i is no longer greater than left.length
  * since is `3` is equal to left.length `3`
    * the remaining entries in arr is set the remaining values in right
    * arr is now [4, 8, 15, 16, 23, 42] and is returned

end state: [4, 8, 15, 16, 23, 42]

## Visual
