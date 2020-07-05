import csv

with open('gps2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row["PlayerID"] != 2:
        	line_count = row;
        	break
print(line_count)