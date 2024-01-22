# 6.6.4. Lexicographic Comparison


# Lexicographic comparison actually does what you intuitively would expect s1 < s2 would do: 
# it checks whether s1 would come before s2 in a dictionary.

# >>> "Aaronson" < "Zukowski"
# True

# Remark, however, the following details:
# • Comparison is case sensitive: "B" < "a" evaluates to True, because uppercase letters are 
# considered "smaller" than lowercase letters.

# • Every character (5, @, space, …) has a specific place in the "alphabet". For example, ' ' < 
# 'A'. The actual order is determined by The Unicode Standard.



# 6.6.5. String Length


# Admittedly, len is not an operator but just a function. 
# But do you really want a separate page just for len?
# len hides no surprises: it returns the length of the string.

# >>> len('schnackenpfefferhausen')
# 22
