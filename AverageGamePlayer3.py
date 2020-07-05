import csv
import math
from array import *
import numpy as np

with open('gps.csv', mode='r') as infile:
    file = csv.DictReader(infile)
    totalData = []
    playerDict = {}
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
            for x in range(0, 21, 1):
                if count[x] != 0:
                    for y in range(0, 4, 1):
                        player[x][y] = totals[x][y] / count[x]

            for i in range(0, 21, 1):
                playerDict["GameID"] = game
                playerDict["PlayerID"] = i + 1
                playerDict["Speed"] = player[i][0]
                playerDict["AccelImpulse"] = player[i][1]
                playerDict["AccelLoad"] = player[i][2]
                playerDict["Magnitude"] = player[i][3]
                totalData.append(playerDict)
                playerDict = {}
            #reset
            totals = [ [ 0 for i in range(4) ] for j in range(21) ]
            game += 1
            player = totals
            count = [0] * 21
            lineNum += 1
            playerDict = {}


    for x in range(0, 21, 1):
        if count[x] != 0:
            for y in range(0, 4, 1):
                player[x][y] = totals[x][y] / count[x]
    for i in range(0, 21, 1):
        playerDict["GameID"] = game
        playerDict["PlayerID"] = i + 1
        playerDict["Speed"] = player[i][0]
        playerDict["AccelImpulse"] = player[i][1]
        playerDict["AccelLoad"] = player[i][2]
        playerDict["Magnitude"] = player[i][3]
        totalData.append(playerDict)
        playerDict = {}
    with open('./Games/data.csv' , mode='w+') as outFile:
            fields = ["GameID", "PlayerID", "Speed", "AccelImpulse", "AccelLoad", "Magnitude"]
            writer = csv.DictWriter(outFile, fieldnames = fields)
            writer.writeheader()
            for row in totalData:
                writer.writerow(row)
            outFile.close()
