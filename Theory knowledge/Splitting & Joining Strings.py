# Splitting Strings

# Converting a string to a list works on the level of single characters:
list("abcd")
["a", "b", "c", "d"]

# Typically, we want something "smarter". 
# Say we have the string "Blondie,Angel Eyes,Tuco" and want to extract the three names. 
# More specifically, we want to construct the list ["Blondie", "Angel Eyes", "Tuco"]. 

# The string method split does exactly that: string.split(separator) will cut 
# string into pieces, where each piece is delimited by separator.
"a,b,c".split(",")
["a", "b", "c"]

# Be careful with spaces
"one, two, three".split(",")
["one", " two", " three"]
"one, two, three".split(", ")
["one", "two", "three"]

# Joining Strings

# The opposite operation separator.join(strings) can also come in handy: given a tuple/list of strings strings, 
# we want to join them together into a single string. The different strings are "glued" together using separator.
", ".join(["a", "b", "c"])
"a, b, c"
" and ".join(["Mac", "Charlie", "Dennis", "Dee"])
'Mac and Charlie and Dennis and Dee'