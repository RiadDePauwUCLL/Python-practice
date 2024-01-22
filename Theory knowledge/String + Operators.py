# Operators, how do they work with strings????
# Fear not, this part is actually simple to understand.


#         Syntax       |      Result      |     Description
#    -----------------------------------------------------------------------
#        ab" + "cd"          "abcd"              Concatenation
#        "ab" * 3            "ababab"            Repetition
#        "a" in "abc"          True              Membership
#        "a" == "a"            True              Equality
#        "a" != "a"            False             Inequality
#        "a" < "b"             True              Lexicographic comparison
#        "a" <= "b"            True              Lexicographic comparison
#        "a" > "b"             False             Lexicographic comparison
#        "a" >= "b"            False             Lexicographic comparison
#        len("abc")              3               Length
#       Within len(x), you start counting from 1 obviously.

# A few examples:

x = "1" + "0"
print(x)

password = '*' * len(x)
print(password)

# Notice what makes it only 2 "*"? The length, not the integer itself!
# If you want it be the same length as the actual integer, you do it this way:

y = "1" + "0"
int_y = int(y)
real_password = '*' * int(y)
print(real_password)