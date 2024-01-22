# Lists

# Tuples are immutable: once created, they cannot be changed: we cannot remove, add or 
# overwrite elements. This immutability can be a strength, but in other cases it can be quite an 
# impediment. Lists are very much like tuples, except they can be modified.


# Literals
# A list literal has the following syntax:
lst = [1, 2, 3, 4]

# As you can see, the only difference lies in the brackets: square brackets for lists, round brackets 
# for tuples. The list with one item also requires no trickery: [1] works just fine.
    
# List Functionality
# All functionality available on tuples also works on lists: 
# len, indexing, slicing, sum, min, max, iteration, destructuring, etc. all work without change. 
# Actually, all code you write that interacts with tuples will behave the same if given lists. 
# Tuples have a subset of the functionality of lists.
sum([1, 2, 3, 4])
10
max([4, 1, 7, 5, 2, 3])
7

# Updating
# Accessing the items of a list is done the same way as with tuples, i.e., by indexing.
lst = ["a", "b", "c", "d"]
# Fetch first item, which has index 0
lst[0]
"a"
# Fetch last item, which has index -1
lst[-1]
"d"

# Using the syntax lst[index] = x you can overwrite the item at the given index.
lst = [7, 4, 1, 9, 3]
# Overwrite first item
lst[0] = 100
lst
[100, 4, 1, 9, 3]
# Double the last item
46
lst[-1] *= 2
lst
[100, 4, 1, 9, 6]



# Adding Items within lists or modifying lists to be more precise.

# Append

# lst.append(x) adds an extra element to the end of the list.
xs = [1, 2, 3]
xs.append(4)
xs
[1, 2, 3, 4]


# Insert

# If you need to add an element somewhere else than at the end, you can rely on the insert 
# method. lst.insert(index, x) adds an element x so that its index equals index. 
# All subsequent elements are shifted one position.
xs = [1, 2, 3, 4]
xs.insert(0, 9)
xs
[9, 1, 2, 3, 4]


# Removing Items

# There are two ways to remove items from lists:
# Either you specify the index of the item to be removed, or
# You specify the value of the item to be removed.

# pop(index)

# lst.pop(index) removes the item at the given index. 
               # You can omit index in which case the last element will be removed.
xs = [1, 2, 3, 4, 5]
xs.pop(1)
xs
[1, 3, 4, 5]
xs.pop()
xs
[1, 3, 4]



# del (index or slice)

# del is a keyword and has a syntax of its own. 
# Functionality-wise it is a more powerful version of pop. 
# del lst[index] does the same as lst.pop(index): it removes the item with the given index. 
# However, del also works with slices: del lst[start:stop] removes all items from start to stop.
xs = [1, 2, 3, 4, 5]
del xs[-1]
xs
[1, 2, 3, 4]
del xs[:2]
xs
[3, 4]

# remove(value)

# Lastly, we have lst.remove(item) which removes the first occurrence of item.
xs = [6, 4, 2, 3, 4, 9, 4]
xs.remove(2)
xs
[6, 4, 3, 4, 9, 4]
xs.remove(4)
xs
[6, 3, 4, 9, 4]

