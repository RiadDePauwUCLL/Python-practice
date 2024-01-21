# Bank Account

# The concept of a bank account in a program makes a good candidate for a class. 
# A bank account typically has the following properties (attributes): the name of the account holder, the account number and 
# the current amount of money in the account. We can execute three actions on a bank account: withdraw money, 
# deposit money and display the particulars of the account. 

# Assignment
# Your assignment consists of making a class BankAccount with the following methods:

# The initializing method __init__ takes the name of the account holder, 
# the account number and an initial amount of money as parameters. 
# The initial amount given is an optional parameter and gets standard value 0.

# The method __str__ prints a string representation of a bank account. 
# Use the example below as a base for the format in which your data will be printed.

# The method __repr__ also prints a string representation of a bank account. 
# Where the method __str__ is used to obtain a representation of an object that can easily be read for the user, 
# the method __repr__ prints a representation that can only be read by the python interpreter. 
# The method __repr__ gives a syntactical correct Python expression, 
# that — if it were evaluated — creates an object that is equal to the object that was initially given to __repr__.

# Two methods deposit(n) and withdraw(n). The parameter of these methods is the amount of money that is withdrawn or deposited.




class BankAccount:
    def __init__(self, name, account_number, amount=0):
        self.name = name
        self.account_number = account_number
        self.amount = amount
    
    def __str__(self):
        return f'{self.name}, {self.account_number}, amount: {self.amount}'

    
    def __repr__(self):
        return f"BankAccount('{self.name}', '{self.account_number}', {self.amount})"


    def deposit(self, n):
        self.amount += n

    
    def withdraw(self, n):
        self.amount -= n


me = BankAccount('Riad', '1337', 1)
me.deposit(1336)
print('\n' + str(me)+'\n')
print(repr(me)+'\n')

DELIGHT = BankAccount('Riad', '4008', 6500)
DELIGHT.withdraw(3400)
print(str(DELIGHT)+'\n')
DELIGHT.deposit(200)
print(repr(DELIGHT))