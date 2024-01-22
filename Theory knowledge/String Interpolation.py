item_count = 5
day = 23
month = 5
message = f'Your items: {item_count}, arrival: {day}/{month}'
price = 23.545

print(message)

# formatting is the key to making your strings being correctly added
# within ur code.


# Decimals, formats??

pricey = f'The price of your item is {price:.2f}'
discount = f'The price of your item is {int(price)}'

print(pricey)
print(discount)


# You can also format decimals just like this.

# Time formatting

h = 13
m = 37
s = 1

time = f'{h:02}:{m:02}:{s:02}'

print(time)

# Time formatting is also possible. It's beautiful, isn't it?


# Now, imagine you want to add "css" within ur python, is that possible? Well, yes.
# With this format specification, you can proceed with alignment for the strings. 
# Useful.

text = "gamer"
gamer = f'{text:^10}|{text:<10}|{text:>10}'

print(gamer)