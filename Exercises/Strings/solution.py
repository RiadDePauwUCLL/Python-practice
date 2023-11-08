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








# Write ur code here:
