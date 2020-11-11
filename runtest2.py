# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 05:51:35 2020

@author: r2d2go
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:11:39 2020

@author: r2d2go
"""

import newRun as NR

import time
start = time.process_time()

import matplotlib.pyplot as plt

winrates = [[.5,.25,1],
            [.75,.5,.25],
            [0,.75,.5]]

loserates = [[0, 1, 0],
             [0, 0, 1],
             [1, 0, 0]]

counterrates = [[0, 1, 0],
                [0, 0, 1],
                [1, 0, 0]]

initialDist = [.33,.33,.34]

nState = NR.Rat(3, winrates, loserates, counterrates, 100, initialDist)
aThing1 = nState.average(initialDist, 40, 30000, .1)


x = range(0,40)
y = aThing1
plt.xlabel("Time")
plt.ylabel("Distribution")
plt.title("Rock Paper Scissors")
plt.plot(x,[pt[0] for pt in y],label = 'Rock')
plt.plot(x,[pt[1] for pt in y],label = 'Paper')
plt.plot(x,[pt[2] for pt in y],label = 'Scissors')
plt.legend(loc='upper right')
plt.show()


stop = time.process_time()
print(str(stop-start))