# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:51:19 2014

@author: aaditya prakash
"""

import math
import time
import numpy as np
import scipy as sc
from itertools import permutations
from itertools import combinations


def fun__(strIn):
    strOutput = []
    strList = strIn.split("\n")
    numT = int(strList[0])
    
    for i in range(numT):
        llIn = strList[i+1]
        res = Strategy(llIn)
        strOutput.append("Case #" + str(i+1) + ": " + str(res))
    
    fileOut = file("B-small-OUT.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    
def Strategy(llIn):
    ll = llIn.split(' ')
    N = int(ll[0])
    Surprise = int(ll[1])
    bestScore = int(ll[2])
    llScores = map(int, ll[3:])
    #print N, Surprise, bestScore, llScores
    defaulter = 0
    for lS in llScores:
        
        diff = lS - bestScore*3
        #print N, Surprise, bestScore, llScores, diff        
        if(lS == 0):
            N -= 1
            continue
        if(diff < -2): 
            defaulter -= 1
    return N + min(defaulter + Surprise, 0)
    

fInput = file("B-small-practice.in", "r")
strIn = fInput.read()
timeStart = time.clock()

fun__(strIn)
#print(Strategy('3 1 5 15 13 11'))
#print(Strategy('3 0 8 23 22 21'))
#print(Strategy('2 1 1 8 0'))
#print(Strategy('6 2 8 29 20 8 18 18 21'))
print('Time (sec):' + str(time.clock() - timeStart))




