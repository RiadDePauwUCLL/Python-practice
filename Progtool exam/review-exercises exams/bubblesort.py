def bubblesort(array):
    n = len(array)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if swap == False:
            break
    return array
# for in range(n) is the number of times we iterate through the array.
# for in range(n - i - 1) is the number of times we iterate 
# through the array minus the number of times we have already iterated.
# if array[j] > array[j + 1], it will swap the two integers.
# if swap == False, it will break the loop.
# if swap == True, it will continue the loop.

print(bubblesort([1, 5, 4, 8]))

# different way of returning this:

def bubblesort_2(array):
    n = len(array)
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if swap == False:
            break


elements = [8, 9, 28, -34]
print(elements)
bubblesort_2(elements)
print(elements)