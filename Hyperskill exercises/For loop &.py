string = ""
for i in range(1, 20, 4):
    string += "&" * i

print(string)


# This exercise has helped me understand for loops better.
# What this does: It will print out an iteration of "&" 5 times, then 9 times, then 13 times, then 17 times.
# basically, 1 + 4 = 5, 5 + 4 = 9, 9 + 4 = 13, 13 + 4 = 17 (as we have to add 4 to the previous number to get the next number)
# The range function is used to specify the start(1), stop(20) and step(4) value.

# for i in range(xs): This will raise an error if xs is not an integer. range() function generates a sequence of numbers starting from 0 up to but not including the number provided.

# for i in xs: This will iterate over each element in the iterable xs. xs could be a list, tuple, string, etc.

# for i in range(0, xs): This is similar to for i in range(xs). It generates a sequence of numbers starting from 0 up to but not including xs. xs must be an integer.

# for i in len(xs): This will raise an error because len(xs) returns an integer and you cannot iterate over an integer.

# for i in range(len(xs)): This will generate a sequence of numbers starting from 0 up to but not including the length of xs. This is commonly used to iterate over the indices of a list.

# for i in range(len(xs), -1): This will raise an error because range() function with two arguments generates a sequence of numbers starting from the first argument up to but not including the second argument. In this case, it will try to generate a sequence starting from the length of xs down to -1, which is not valid. If you want to generate a sequence in reverse order, you should use range(len(xs)-1, -1, -1).

# Remember, the range() function generates a sequence of numbers and does not modify the actual iterable you are looping over. On the other hand, for i in xs directly iterates over the elements in the iterable.