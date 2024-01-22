# HOW DOES SLICING WORKS???? 
# DO I JSUT SLICE THE CAKE??? OR DO I MAGICALLY MAKE IT SLICE???

# Nah. Slicing is a bit tricky, remember that.
# Here's how it goes:

car = "Lamborghini"
bad_slice = car[3] + car[4] + car[5] + car[6]
good_slice = car[3:7]
print(good_slice)

# Why am I not stopped at the 6th index you think? 
# Simple. 7th index is the stop sign, why should we count that?

# Here's a few more things to know about slicing:
#       s[:j] Same as s[0:j]
#       s[i:] Same as s[i:len(s)]
#       s[:] Same as s[0:len(s)], i.e., returns the whole string



# Within slicing, you can also specify steps! 
# step: s[start:end:step]
# For example:
find = "bad,good/terrible"
step = find[0:-1:5]
print(step)
# Here it takes 5 steps after each index. It can be confusing,
# but it's very useful if you have to find information from a string backwards.
