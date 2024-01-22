from os.path import exists

pi_string = ""

with open ('pi_million.txt') as line_object:
    lines = line_object.readlines()

for line in lines:
    pi_string += line.strip()

bday = input("Enter your birthday, in the form ddmmyy: ")
with open("bday_results.txt", "a", encoding="utf-8") as output:
    if bday in pi_string:
        output.write("Your birthday appears in the first million digits of pi!")
        position = pi_string.find(bday)
        output.write(position)
    else:
        print("Your birthday does not appear in the first million digits of pi.")


text = open('monke.txt', 'w')
text.writelines(["monke likes banana" "\n", "i like bikes"])
text.close()

text = open('monke.txt', 'a')
addition = input("What do you want to add to the file? ")
text.write ("\n" + addition)
text.close()