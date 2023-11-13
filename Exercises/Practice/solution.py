import math

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
# Freestyle Sparring
# Take turns remixing and refactoring others code through Kumite
# COMMUNITY
# Leaderboards
# Achieve honor and move up the global leaderboards
# Chat
# Join our Discord server and chat with your fellow code warriors
# Discussions
# View our Github Discussions board to discuss general Codewars topics
# ABOUT
# Docs
# Learn about all of the different aspects of Codewars
# RiadDePauwUCLL Avatar
# 7 kyu
# 55
# 7 kyu
# You're a square!
# 203938888% of 20,90273,011 of 243,101bkaes
#  Python
# 3.11
# VIM
# EMACS
# Instructions
# Output
# A square of squares
# You like building blocks. You especially like building blocks that are squares. And what you even like more, is to arrange them into a square of square building blocks!

# However, sometimes, you can't arrange them into a square. Instead, you end up with an ordinary rectangle! Those blasted things! If you just had a way to know, whether you're currently working in vain… Wait! That's it! You just have to check if your number of building blocks is a perfect square.

# Task
# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

# The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

def is_square(n):
    if n < 0:
        return False
    square_root = int(math.sqrt(n))
    square_number = square_root * square_root
    if square_number == n:
        return True
    else:
        return False
    













# Write ur code here:
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    result = []
    
    for member in data:
        age, handicap = member
        
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
        
    return result













# Write ur code here:
# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    return min(arr)