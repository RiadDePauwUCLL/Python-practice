#how to use the filter buit-in function in python

nums=range(1,150)
print(list(nums))

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

primes=list(filter(is_prime, nums))

print(f'{primes}' + '\n' + f'Prime numbers' + '\n\n')

# is_prime is a function that takes a number and returns True if the number is prime and False otherwise.
# filter takes a function and a collection. It returns a collection of every item for which the function returned True.
# The filter resembles a for loop but it is a builtin function and faster.
# The filter function is used to create a list of elements for which a function returns True.
# list makes a list out of the result of filter.


# The filter function in Python is a built-in function that constructs an iterator from elements of an iterable for which a function returns true.

# Here's how it works:

# filter takes two arguments: a function and an iterable.
# It applies the function to each element in the iterable.
# If the function returns True for an element, filter includes that element in the new iterator.
# If the function returns False for an element, that element is not included.
# In the provided code, filter is used with the is_prime function and the nums iterable. The is_prime function checks if a number is prime. So, filter(is_prime, nums) creates a new iterator that includes only the numbers in nums that are prime.

# The list function is then used to convert this iterator into a list, which is assigned to the primes variable. So, primes is a list of all the prime numbers in nums.

# Here's a simple example of using filter:

def is_even(num):
    return num % 2 == 0

nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(is_even, nums))

print(f'Even number' + '\n' f'{even_nums}')  # Output: [2, 4, 6]

# In this example, filter is used to create a list of the even numbers in nums.