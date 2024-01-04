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
# Write ur code here:

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
    








# Remove every other within a list! AKA slicing.
# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!
# Write ur code here:

def remove_every_other(my_list):
    optimus_prime = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            optimus_prime.append(my_list[i])
    return optimus_prime

# If you want a more pythonic way of doing it, you can use list slicing:
def remove_every_other(my_list):
    return my_list[::2]

# list slicing is a way to extract a portion of a list.
# list slicing is done by defining the start, stop, and step values.
# list slicing is done by using the colon operator.







# How 2 filter a list!
# In this kata you will create a function that takes a list of non-negative integers 
# and strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
# Write ur code here:

def filter_list(l):
    filter = []
    for num in l:
        if isinstance(num, int):
            filter.append(num)
    return filter







# Square Digits
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# Happy Coding!
# Write ur code here:

def square_digits(num):
    str_num = str(num)
    squared_digits = [str(int(digits) ** 2) for digits in str_num]
    result = ''.join(squared_digits)
    return int(result)

# You got two ways of doing it. The first one is the one I did, which is the most clever one. The other one is more simple:

def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)





# Prime numbers
# In this Kata we are passing a number (n) into a function.

# Your code will determine if the number passed is even (or not).

# The function needs to return either a true or false.

# Numbers may be positive or negative, integers or floats.

# Floats with decimal part non equal to zero are considered UNeven for this kata.
# Write ur code here:

def is_even(n): 
    if n % 2 == 0:
        return True
    else:
        return False
    
# this makes it clearer on how it works. But you can also do it like this, just less readable:
    
def is_even(n): 
    return n % 2 == 0






# Move the zeros!
# Write an algorithm that takes an array and moves all of the zeros to the end, 
# preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
# Write ur code here:

def move_zeros(lst):
    new_lst = []
    zero = []
    for i in range(len(lst)):
        if lst[i] > 0:
            new_lst.append(lst[i])
        elif lst[i] < 1:
            zero.append(lst[i])
    new_lst.extend(zero)
    return new_lst


# There is obviously a much more pythonic way of doing it, which is this one:

def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array








# Ingredients & Cakes
# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
# Can you help him to find out, how many cakes he could bake considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) 
# and returns the maximum number of cakes Pete can bake (integer). 

# For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
# Ingredients that are not present in the objects, can be considered as 0.

# Examples:

#  must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
#  must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

# Write ur code here:

def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
    
# here, we are using try and except.
# try and except are used to prevent the code from crashing.
# return min() returns the smallest number from the list.
# available[a] / recipe[a] returns the number of servings for each ingredient.
# recipe[a] returns the amount of each ingredient needed.
# available[a] returns the amount of each ingredient available.
# it returns 0 if there is not enough ingredients to make the cake.

# There is also a different way of doing it, but it's a bit more complex:

def cakes(recipe, available):
    max_servings = float('inf')
    for ingredient, amount in recipe.items():
        if ingredient in available:
            servings = available[ingredient] // amount
            max_servings = min(max_servings, servings)
        else:
            return 0
    return max_servings

# In Python, float('inf') represents positive infinity, which is a mathematical concept indicating an unbounded positive value. 
# It is a special floating-point representation that is greater than any finite floating-point number.

# Here's a breakdown of the expression float('inf'):

# float: This is a built-in function in Python that converts a number or a string to a floating-point number. 
# In this case, it's used to explicitly convert the string 'inf' to a floating-point representation.

# 'inf': This is a string representing infinity. The use of 'inf' is a convention in Python to denote positive infinity.

# So, float('inf') creates a floating-point representation of positive infinity. 
# This is commonly used in situations where you want to initialize a variable to a value that is guaranteed to be greater than any finite number. 
# In the context of the previous code snippets, max_servings is initialized to positive infinity so that, during the iteration over ingredients, 
# it can be updated with the minimum of the current value and the calculated servings, ensuring it eventually holds the smallest possible number of servings.








# Count all characters within string
# The main idea is to count all the occurring characters in a string. 
# If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.
# Write ur code here:

def count(s):
    return {x : s.count(x) for x in set(s)}

# here, we are using set(s) to store the unique values from s.
# then, we are using count(x) to count the number of times each character appears in s thanks to the for loop.








# IPs between eachother
# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246
# Write ur code here:

def ips_between(start, end):
    def ip_to_int(ip):
        return sum(int(part) * 256 ** i for i, part in enumerate(reversed(ip.split('.'))))
    
    return ip_to_int(end) - ip_to_int(start)

# alternative & faster method:

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))








# Find odd number
# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# Write ur code here:

def find_it(seq):
    for odd in seq:
        if seq.count(odd) % 2 != 0:
            return odd
        






# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"
# Write ur code here:

def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == p2:
        return "Draw!"
    else:
        return "Player 2 won!"
    
# Dictionaries exist and they make our lives easier:
    
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"









# Disemvowel Trolls
# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels 
# from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and 
# return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" 
# would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.
# Write ur code here:

def disemvowel(string_):
    vowels = "aeuioAEUIO"
    for vowel in vowels:
        string_ = string_.replace(vowel, '')
    return string_








# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]
# Write ur code here:

def digitize(n):
    return [int(digit) for digit in str(n)[::-1]]

# Pretty much self-explanatory.






# Grasshopper - Grade book
# Complete the function so that it finds the average of the three scores 
# passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. 
# Theres is no need to check for negative values or values greater than 100.
# Write ur code here:

def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return "F"
    





# Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.
# Write ur code here:

def invert(lst):
    return [-x for x in lst]


# This one seems so stupid yet so simple... clean.





# Century From Year
# The first century spans from the year 1 up to and including the year 100, 
# the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# Write ur code here:

from math import ceil

def century(year):
    return ceil(year / 100)


# Extremely efficient.





# Break the camelCase
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# Write ur code here:

def solution(s):
    result = ''
    for char in s:
        if char.isupper():
            result += ' ' + char
        else:
            result += char
    return result

# just read the code, it's that simple lol. Thought it was more complex than that.






# Remove the minimum
# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. 
# Miriam, the interior architect, comes up with a plan to remove the most boring 
# exhibitions. She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibitions, she's off to an important fair, 
# so she asks you to write a program that tells her the ratings 
# of the items after one removed the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
# If there are multiple elements with the same value, remove the one with a lower index. 
# If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples:
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]
# Write ur code here:

def remove_smallest(numbers):
    if numbers:
        small_pp = numbers.copy()
        small_pp.remove(min(small_pp))
        return small_pp
    else:
        return []
    





# Lost Without a Map

# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]
# Write ur code here:
    
def maps(a):
    return [x * 2 for x in a]

# alternative way

def maps(a):
    result = []
    for x in a:
        result.append(x * 2)
    return result



# Counting Duplicates
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters 
# and numeric digits that occur more than once in the input string. 
# The input string can be assumed to contain only alphabets 
# (both uppercase and lowercase) and numeric digits.

# Example:

# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
# Write ur code here:

def duplicate_count(text):
    text = text.lower()
    dupes = 0
    for char in set(text):
        if text.count(char) > 1:
            dupes += 1
    return dupes

# Simplistic code, you don't have to make it more complex than that.








# Remove first & last character
# It's pretty straightforward. Your goal is to create a function 
# that removes the first and last characters of a string. 
# You're given one parameter, the original string. 
# You don't have to worry with strings with less than two characters.
# Write ur code here:

def remove_char(s):
    return s[1:-1]