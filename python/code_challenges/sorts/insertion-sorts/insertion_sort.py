def insertion_sort(array):

    for i in range(len(array)):
        j = i - 1
        temp = array[i]
        
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        
        array[j + 1] = temp

    return array