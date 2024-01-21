
# This was painful to figure out, it somehow works i cba

with open("listofwords_output.txt", 'r') as input_file:
    lines = input_file.readlines()
    vowels = 'aeuio'
    consonants = 'zrtypsdfghjklmwxcvbn'
    vowel_nr = 0
    cons_nr = 0

    word_vowel = ""
    word_consonant = ""
    short_word_v = lines[0].strip().split()[0]
    short_word_c = lines[0].strip().split()[0]

    for line in lines:
        words = line.strip().split()
        for word in words:
            if word[-1] in vowels and len(word) > len(word_vowel):
                word_vowel = word
            if word[-1] in consonants and len(word) > len(word_consonant):
                word_consonant = word
            if word[0] in vowels and len(word) < len(short_word_v):
                short_word_v = word
            if word[0] in consonants and len(word) < len(short_word_c):
                short_word_c = word
            for letter in word:
                if letter in vowels:
                    vowel_nr += 1
                elif letter in consonants:
                    cons_nr += 1



with open('output.txt', 'w') as output_file:
    output_file.write(f'The longest word ending in a vowel is: {word_vowel}\n')
    output_file.write(f'The longest word ending in a consonant is: {word_consonant}\n')
    output_file.write(f'The shortest word that starts with a vowel is: {short_word_v}\n')
    output_file.write(f'The shortest word that starts with a consonant is: {short_word_c}\n')
    output_file.write(f'The number of vowels used is: {vowel_nr}\n')
    output_file.write(f'The number of consonants used is: {cons_nr}\n')