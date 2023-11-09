#
#        Feel free to make this your playground, have fun coding Python.
#   
#        Count sheep
#        If you can't sleep, just count sheep!!
#
#        Task:
#        Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.
#Write ur code here:
def count_sheep(n):
    return ''.join(f'{n} sheep...' for n in range(1, n + 1))










#        Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
#        
#        Reverse words
#        Examples
#        "This is an example!" ==> "sihT si na !elpmaxe"
#        "double  spaces"      ==> "elbuod  secaps"
#Write ur code here:
def reverse_words(text):
    words = text.split(' ')
    word = [words[::-1] for word in words]
    reversed_text = ' '.join(word)
    return reversed_text








# Write ur code here:           XD
#           In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
#           Make number negative
#
#           Examples
#           make_negative(1);  # return -1
#           make_negative(-5); # return -5
#           make_negative(0);  # return 0
#           Notes
#           The number can be negative already, in which case no change is required.
#           Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number










# Write ur code here:
