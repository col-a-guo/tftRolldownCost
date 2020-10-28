# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 06:59:58 2020

@author: r2d2go
"""
import random
import math
import matplotlib.pyplot as plt

def run(winrate, startstreak, startgold):   
    gold = startgold
    lostGold = 0
    winstreak = startstreak
    for i in range (10):
        winvar = random.uniform(0,1)
        if winvar < winrate:
            gold += 1
            if winvar > 0:
                winstreak += 1
            else:
                winstreak = 1
        else:
            if winvar < 0:
                winstreak -= 1
            else:
                winstreak = -1
        if gold > 50:
            return lostGold
        else:
            lostGold += 5-math.floor(gold/10)
            if winstreak > 4:
                gold += 3
            elif winstreak < -4:
                gold += 3
            elif winstreak > 3:
                gold += 2
            elif winstreak < -3:
                gold += 2
            elif winstreak > 1:
                gold += 1
            elif winstreak < -1:
                gold += 1
            gold += math.floor(gold/10)+5

def averageRun(winrate, startstreak, startgold, runs):
    totalLostGold = 0.0
    for i in range (runs):
        totalLostGold += run(winrate, startstreak, startgold)
    return(totalLostGold/runs)


runList = []

runs = 1000

for i in range(50):
    runList.append([])
    startgold = i
    for j in range(3):
        startstreak = -4 + 4*j
        winrate = .1+.4*j
        runList[i].append(averageRun(winrate, startstreak, startgold, runs))
    
xList = []    
for i in range(26):
    xList.append(2*i)

x = range(len(runList))
y = runList
plt.xlabel("Ending Gold")
plt.ylabel("Gold Lost")
plt.title("Rolldown Total Costs")
for i in range(len(y[0])):
    plt.plot(x,[pt[i] for pt in y],label = "starting streak = " + str(-4+4*i) + " wins, winrate = " + str((1+4*i)/10))
plt.legend()
plt.show()


bigList = [['Start Gold', '10% WR', '50% WR', '90% WR']]
for i in range(52):
    bigList.append([i])
    

for mCostRun in range(3):
    marginalCostList = []
    for i in range(len(runList)-2):
        marginalCostList.append([runList[i][mCostRun]-runList[i+2][mCostRun]])
    marginalCostList.append([runList[48][mCostRun]])
    marginalCostList.append([runList[49][mCostRun]])
    marginalCostList = [[0],[0]]+marginalCostList
    

    x = range(len(marginalCostList))
    y = marginalCostList
    plt.xlabel("Starting Gold")
    plt.ylabel("Cost of Rolling Once")
    plt.title("Rolldown Individual Roll Costs")
    plt.xticks(ticks=xList)
    for i in range(len(y[0])):
        plt.bar(x,[pt[i] for pt in y],label = "starting streak = " + str(-4+4*mCostRun) + ", winrate = " + str((1+4*mCostRun)/10))
    plt.legend()
    plt.show()
    for i in range(len(marginalCostList)):
        bigList[i+1] = bigList[i+1]+[round(marginalCostList[i][0],4)]


plt.title('Cost of Rolling Once', pad = 650)
plt.table(bigList, loc='top')
plt.show()
