import csv

# csv bad

total_goals = {}

with open('input.txt', 'r') as input_file:
    lines = csv.reader(input_file, delimiter= ';')
    for line in lines:
        last_name, first_name, country, goals, *rest = line  # *rest or *args, is used for unpacking the remaining values in the list aka the last ";".

        baller = f'{last_name};{first_name}'

        total_goals[baller] = total_goals.get(baller, 0) + int(goals)
    

with open('results.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    for baller, goals in total_goals.items():
        last_name, first_name = baller.split(';')
        writer.writerow([last_name, first_name, goals])

    

# what the fuck did they learn last year ??????????????

def get_countries(excluded_countries):
    with open('input.txt', 'r') as input_file:
        lines = csv.reader(input_file, delimiter=';')
        countries = set()
        for line in lines:
            _, _, country, _, *rest = line # *rest or *args, is used for unpacking the remaining values in the list aka the last ";".
            countries.add(country)
        return countries - set(excluded_countries)
    
excluded_countries = ["Netherlands", "Portugal"]
print(get_countries(excluded_countries))