def booleans():
    x = 0
    y = 1

    if x == True:
        return True
    return f'False because x = 0'   

    
print(booleans())

# Basically checking with conditionals & booleans if x == True.
# False always is 0 and under. True is the opposite; 1 and above.
# But the thing is with booleans, we compare the values.

# Also, keep in mind : a string boolean is not the same as an actual boolean.

#       >>> bool('True')
#       True

#       >>> bool('False')
#       True # !!!
