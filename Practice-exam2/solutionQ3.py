import csv

# we didn't learn csv, apparently not on the exam. 
# Aimee & Serhat better not be lying

# Step 1
total_time = {}

# Step 2
with open('input.txt', 'r') as input_file:
    lines = csv.reader(input_file)
    for line in lines:
        # Step 3
        surname, firstname, competition, result, time = line
        # Step 4
        cyclist = f"{surname},{firstname}"
        # Step 5
        total_time[cyclist] = total_time.get(cyclist, 0) + float(time)

# Step 6
with open('totale_tijd.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    for cyclist, time in total_time.items():
        surname, firstname = cyclist.split(',')
        writer.writerow([surname, firstname, time])