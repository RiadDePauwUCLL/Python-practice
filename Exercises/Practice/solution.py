import math

#
# Feel free to make this your playground, have fun coding Python.
#   
# Count sheep
# If you can't sleep, just count sheep!!
#
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.
#Write ur code here:

def count_sheep(n):
    return ''.join(f'{n} sheep...' for n in range(1, n + 1))










# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.
#        
# Reverse words
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
#Write ur code here:

def reverse_words(text):
    words = text.split(' ')
    word = [word[::-1] for word in words]
    reversed_text = ' '.join(word)
    return reversed_text

# EVEN BETTER VERSION AHAHAHAHAHAHA

def reverse_words(text):
    words = text.split(' ')
    XDDDDD = ' '.join(word[::-1] for word in words)
    return XDDDDD









# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Make number negative
#
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
# Notes:
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
# Write ur code here:           XD

def make_negative(number):
    if number > 0:
        return -number
    else:
        return number











# Freestyle Sparring
# Take turns remixing and refactoring others code through Kumite
# A square of squares
# You like building blocks. You especially like building blocks that are squares. 
# And what you even like more, is to arrange them into a square of square building blocks!

# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! 
# Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! 
# You just have to check if your number of building blocks is a perfect square.

# Task
# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer that is the square of an integer; 
# in other words, it is the product of some integer with itself.

# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false
# Write ur code here:

def is_square(n):
    if n < 0:
        return False
    square_root = int(math.sqrt(n))
    square_number = square_root * square_root
    if square_number == n:
        return True
    else:
        return False
    














# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
# They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
# In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. 
# Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) 
# stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
# Write ur code here:

def open_or_senior(data):
    result = []
    
    for member in data:
        age, handicap = member
        
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
        
    return result














# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.
# Write ur code here:

def find_smallest_int(arr):
    return min(arr)









# In a factory a printer prints labels for boxes. 
# For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

# The colors used by the printer are recorded in a control string. 
# For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, 
# four times color b, one time color h then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction 
# and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

# You have to write a function printer_error which given a string will return the error rate of the printer 
# as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. 
# Don't reduce this fraction to a simpler expression.

# The string has a length greater or equal to one and contains only letters from ato z.

# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"

# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"
# Write ur code here:

def printer_error(s):
    printer_error = 0
    
    for i in s:
        if ord(i) > ord('m'):
            printer_error += 1
    return f'{printer_error}/{len(s)}'

# I MADE THIS AND IM SO PROUD I DONT CARE
def printer_error(s):
    yourmommafat = 0
    for char in s:
        if char > "m":
            yourmommafat += 1
    return f"{yourmommafat}/{len(s)}"
# SO FUNNY XSDDD

# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.
# Write ur code here:

def get_count(sentence):
    vowels = 0
    given_vowels = "aeiou"
    for char in sentence:
        if char.lower() in given_vowels:
            vowels += 1
    return vowels





# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.
# Write ur code here:

def high_and_low(numbers):
    numbers = [int(n) for n in numbers.split()]
    max_num = max(numbers)
    min_num = min(numbers)
    return f'{max_num} {min_num}'








# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
# Jaden is also known for some of his philosophy that he delivers via Twitter. 
# When writing on Twitter, he is known for almost always capitalizing every word. 
# For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

# Example:

# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
# Write ur code here:

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())









# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined
# Write ur code here:

def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count

# for this one, there is also a different possibility 
# that may be really useful for string.

def count_sheeps(sheep):
    return sheep.count(True)





# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]
# Write ur code here:

def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]

# enumerate is a built-in function of Python. It returns an enumerate object.
# It allows us to loop over something with an implemented counter & 
# generates an index for each item in the loop.
# counter basically loops itself over the lines, starting from 1.







# Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
# Write ur code here:

def longest(a1,a2):
    combined_set = set(a1 + a2)
    sorted_result = ''.join(sorted(combined_set))

    return sorted_result

#Just found it there's a better way of doing it:
def longest(a1,a2):
    return ''.join(sorted(set(a1 + a2)))

# here, we are using set() to store the unique values from a1 and a2.
# then, we are using sorted() to sort the values from combined_set.
# then, we are using ''.join() to join the sorted values from combined_set.

# set() is an unordered collection of unique items.
# set() is used to store unique values from a string.
# set() is used to remove duplicates from a list.
# set() is mutable, i.e., we can change its elements once it is created.
# set() is unordered, i.e., it doesn't remember the order of insertion.







# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# count_by(1,10) should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) should return [2,4,6,8,10]
# Write ur code here:

def count_by(x, n):
    b_random = []
    user_4chan = x
    while len(b_random) < n:
        b_random.append(user_4chan)
        user_4chan += x
    
    return b_random










# After a hard quarter in the office you decide to get some rest on a vacation. 
# So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    rent = 40
    total = rent * d
    if d >= 7:
        total -= 50
        return total 
    elif d >= 3:
        total -= 20
        return total
    else:
        return total