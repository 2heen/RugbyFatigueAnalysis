import csv
import math
from array import *
import numpy as np

with open('gps.csv', mode='r') as infile:
    file = csv.DictReader(infile)
    totals = [ [ 0 for i in range(4) ] for j in range(21) ]
    player = totals
    count = [0] * 21
    game = 1
    lineNum = 0
    for row in file:
    	if int(row["GameID"]) == game:
    		totals[int(row["PlayerID"]) - 1][0] += abs(float(row["Speed"]))
    		totals[int(row["PlayerID"]) - 1][1] += abs(float(row["AccelImpulse"]))
    		totals[int(row["PlayerID"]) - 1][2] += abs(float(row["AccelLoad"]))
    		totals[int(row["PlayerID"]) - 1][3] += abs(math.sqrt(float(row["AccelX"])**2 + float(row["AccelY"])**2 + float(row["AccelZ"])**2))
    		count[int(row["PlayerID"]) - 1] += 1
    	else:
            f = open("./Games/Game%d.txt" %game, "w+")
            f.write("\n\nGame %d:\n\n" %game)
            for x in range(0, 21, 1):
                if count[x] != 0:
                    for y in range(0, 4, 1):
                        player[x][y] = totals[x][y] / count[x]
                f.write("\nPlayer %d: \n" %int(x+1))
                for a in player[x]:
                    f.write("%f\n" %a)
            f.write("Count:\n")
            for b in count:
                f.write("%f\n" %b)

            totals = [ [ 0 for i in range(4) ] for j in range(21) ]
            game += 1
            player = totals
            count = [0] * 21
            f.close()
            lineNum += 1

    f = open("./Games/Game38.txt", "w+")
    f.write("\n\nGame38:\n\n")
    for x in range(0, 21, 1):
        if count[x] != 0:
            for y in range(0, 4, 1):
                player[x][y] = totals[x][y] / count[x]

        f.write("\nPlayer %d: \n" %int(x+1))
        for a in player[x]:
            f.write("%f\n" %a)
    f.write("\n\nCount:\n")
    for b in count:
        f.write("%f\n" %b)
    f.close()
