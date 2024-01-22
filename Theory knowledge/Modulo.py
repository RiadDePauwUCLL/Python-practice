def modulo(y):
    modulo = 167 % 20
    true_div = 167 // 20
    return f'modulo: 167 % 20 = {modulo} \ntrue division: 167 // 20 =  {true_div}'

# Now imagine if you want to use the modulo operator. What does it do again?
# Computes the remainder when you divide "x" by "y".
# True division "//" computes the amount of times "y" fits in "x".
print(modulo(20))