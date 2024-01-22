def count_lines_in_file(path):
    with open (path) as count_lines:
        count_lines = count_lines.readlines()

    return len(count_lines)



def remove_empty_lines(source, destination):
    with open(source, 'r') as file:
        lines = file.readlines()

    strings = [line for line in lines if line.strip('\n') != '']

    with open(destination, 'w') as file:
        file.writelines(strings)



def remove_duplicate_lines(source, destination):
    with open(source, 'r') as file:
        lines = file.readlines()

    with open(destination, 'w') as file:
        if lines:
            file.write(lines[0])
            for i in range(1, len(lines)):
                if lines[i] != lines[i-1]:
                    file.write(lines[i])

# Reads all lines from the source file & proceeds to write the unique lines to the destination file.
# We write the first line, no comparation needed.
# The loop goes through the rest of the list within the lines and starts at index [1].
# "if lines[i] != lines[i-1]:" Check if the iteration if the same as the previous line.
# If it is, it iterates over it and proceeds to the next line.
# "file.write(lines[i])" If it isn't a duplicate, it will proceed with writing the line.