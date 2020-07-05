import csv
import math
from array import *
import numpy as np

if __name__ == 'main':
    totals = [ [ 0 for i in range(4) ] for j in range(21) ]
    playerDict = {}
    player = totals
    count = [0] * 21
    totalData = []
    data = {}
    game = 1
    lineNum = 0
    speedDev = 0
    impulseDev = 0
    loadDev = 0
    magDev = 0
    main()

def zScore2():
    stdDev = [ [ 0 for i in range(4) ] for j in range(21) ]
    zScore = stdDev
    for row in file:
        if int(row["GameID"]) == game:
            stdDev[int(row["PlayerID"]) - 1][0] += (abs(float(row["Speed"])) - player[int(row["PlayerID"]) - 1][0])**2
            stdDev[int(row["PlayerID"]) - 1][1] += (abs(float(row["AccelImpulse"])) - player[int(row["PlayerID"]) - 1][1])**2
            stdDev[int(row["PlayerID"]) - 1][2] += (abs(float(row["AccelLoad"])) - player[int(row["PlayerID"]) - 1][2])**2
            stdDev[int(row["PlayerID"]) - 1][3] += (abs(math.sqrt(float(row["AccelX"])**2 + float(row["AccelY"])**2 + float(row["AccelZ"])**2)) - player[int(row["PlayerID"]) - 1][3])**2
    for i in range(0, 21, 1):
        for j in range(0, 4, 1):
            stdDev[i][j] = math.sqrt(stdDev[i][j] / count[i])
    for row in file:
        if int(row["GameID"]) == game:
            zScore[int(row["PlayerID"]) - 1][0] += (float(row["Speed"]) - player[int(row["PlayerID" - 1])][0]) / stdDev[int(row["PlayerID"]) - 1][0]
            zScore[int(row["PlayerID"]) - 1][2] += (float(row["AccelImpulse"]) - player[int(row["PlayerID" - 1])][0]) / stdDev[int(row["PlayerID"]) - 1][0]
            zScore[int(row["PlayerID"]) - 1][3] += (float(row["AccelLoad"]) - player[int(row["PlayerID" - 1])][0]) / stdDev[int(row["PlayerID"]) - 1][0]
            zScore[int(row["PlayerID"]) - 1][4] += (abs(math.sqrt(float(row["AccelX"])**2 + float(row["AccelY"])**2 + float(row["AccelZ"])**2))) / stdDev[int(row["PlayerID"]) - 1][0]

    for i in range(0, 21, 1):
        for j in range(0, 4, 1):
            zScore[i][j] = math.sqrt(zScore [i][j] / count[i])

    for i in range(0, 21, 1):
        playerDict["PlayerID"] = i + 1
        playerDict["Speed"] = player[i][0]
        playerDict["AccelImpulse"] = player[i][1]
        playerDict["AccelLoad"] = player[i][2]
        playerDict["Magnitude"] = player[i][3]
        playerDict["StdSpeed"] = stdDev[i][0]
        playerDict["StdImpulse"] = stdDev[i][1]
        playerDict["StdLoad"] = stdDev[i][2]
        playerDict["StdMag"] = stdDev[i][3]
        playerDict["ZSpeed"] = zScore[i][0]
        playerDict["ZImpulse"] = zScore[i][1]
        playerDict["ZLoad"] = zScore[i][2]
        playerDict["ZMag"] = zScore[i][3]
        totalData.append(playerDict)
        playerDict = {}



def main():
    with open('gps.csv', mode='r') as infile:
        file = csv.DictReader(infile)
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

                zScore2()
                #reset data
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
