def selectionsort(array):
    n = len(array)
    for i in range(n):
        minimum = i
        for j in range(i + 1, n):
            if (array[j] < array[minimum]):
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array
        
#make an example by swapping them one by one, it's clearer on practice.
print(selectionsort([49, 23, 45, 19]))
print(selectionsort([49, 23, 45, 19, 504, 18, 32]))