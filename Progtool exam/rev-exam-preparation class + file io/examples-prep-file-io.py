#File-IO Sample exercise

with open('C:\Users\lalad\course-material\exercises\exam-preparation\input.txt', 'r') as input_file:
    lines = input_file.readlines()
    max_age = 0
    min_age = 100
    sum_age = 0
    oldest_person = ''
    youngest_person = ''
    for line in lines:
        name, age = line.split()
        age = int(age)                  # lol
        sum_age += age

        if age > max_age:
            max_age = age               # name, age does the magic hehe funny
            oldest_person = name        # line.split() is the one that splits the line into two parts, name and age.
        elif age < min_age:
            min_age = age
            youngest_person = name      # read above, same thing but just the opposite ain't it easy

average_age = int(sum_age/len(lines))   # do you really need explanation for that one?

with open('output.txt', 'w') as output_file:
    output_file.write(f'average age: {average_age}\n')
    output_file.write(f'oldest person: {oldest_person}\n')
    output_file.write(f'youngest person: {youngest_person}\n')          # the wonders of formatting strings, ain't it beautiful?