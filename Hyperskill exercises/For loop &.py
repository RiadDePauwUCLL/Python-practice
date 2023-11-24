string = ""
for i in range(1, 20, 4):
    string += "&" * i

print(string)


# This exercise has helped me understand for loops better.
# What this does: It will print out an iteration of "&" 5 times, then 9 times, then 13 times, then 17 times.
# basically, 1 + 4 = 5, 5 + 4 = 9, 9 + 4 = 13, 13 + 4 = 17 (as we have to add 4 to the previous number to get the next number)
# The range function is used to specify the start(1), stop(20) and step(4) value.