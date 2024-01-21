def index_smallest(lst, i):
    if i in lst:
        for index in range(len(lst)):
            if lst[index] == i:  # always make use of variable with for loops. check the lst[index] with == i, not i == lst[index]
                return index
    else:
        return -1
    

print(index_smallest([1,5,4,8,2,9],3))
print(index_smallest([1,5,4,8,2,9],2))
print(index_smallest([1,5,4,8,2,9],0))
print(index_smallest([1,5,4,8,2,9],-5))


def swap(lst, i):
    smallest_index = index_smallest(lst, i)
    if smallest_index != -1:
        lst[smallest_index], lst[i] = lst[i], lst[smallest_index]
        return lst
    else:
        return lst
    
print(swap([1,5,4,8,2,9], 2))
print(swap([1,5,4,8,2,9],-5))


def sort(lst):
    for i in range(len(lst)):
        smallest_index = index_smallest(lst[i:], 0) + i
        # 0 is the placeholder in regard to the index.
        if smallest_index != -1:
            lst = swap(lst, smallest_index)
        else:
            return lst

print(swap([1,5,4,8,2,9],2))