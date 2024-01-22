def mastermind(code, guess):
    correct = 0
    wrong_pos = 0
    if code == guess:
        print("You guessed it right!")
    else:
        print("You guessed it wrong!")
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct += 1
            wrong_pos -= 1
        if guess[i] in code:
            wrong_pos += 1
    return (correct, wrong_pos)

code = [1,2,5,6]
guess = [1,2,5,6]
print(mastermind(code, guess))