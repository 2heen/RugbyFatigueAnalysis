import csv
import math

with open('gps.csv', mode='r') as infile:
    file = csv.DictReader(infile)

    magnitude = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    numberOfLines = 0;
    for row in file:
	    magnitude[int(row["PlayerID"]) - 1] += math.sqrt(float(row["AccelX"])**2 + float(row["AccelY"])**2 + float(row["AccelZ"])**2)
	    count[int(row["PlayerID"]) - 1] += 1
	    numberOfLines += 1
    
    for x in range(0, 20, 1):
    	if count[x] != 0:
    		magnitude[x] /= count[x] 

    print(magnitude)
    print(numberOfLines)

