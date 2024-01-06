#Party time
# James is hosting a party today. He decided to welcome all new guests personally. To remember their names, James kindly asks you to write them in a list. Read the names from the input, each on a new line, and stop at a single period . that denotes the end of the sequence.

# Print your list and its length (the number of guests) for James.

# Use list.append(new_element) method to add new elements to a list.
# Sample Input 1:

# Katja
# Adam
# Eva
# Nicholas
# .
# Sample Output 1:

# ['Katja', 'Adam', 'Eva', 'Nicholas']
# 4

def get_guest_list():
    guest_list = []
    while True:
        name = input()
        if name == '.':
            break
        guest_list.append(name)
    print(guest_list)
    print(len(guest_list))

get_guest_list()