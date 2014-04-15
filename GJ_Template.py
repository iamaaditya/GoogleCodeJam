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
    strList = strInput.split("\n")
    numT = int(strList[0])
    
    for i in range(numT):
        llIn = strList[i+1]
        res = Strategy(llIn)
        strOutput.append("Case #" + str(i+1) + ": " + str(res))
    
    fileOut = file("X-OUT.txt", "w")
    for item in strOutput:
        print>>fileOut, item
    fileOut.close()
    
def Strategy(llIn):
    
    
    return 0
    

fInput = file("X-small.in", "r")
strIn = fInput.read()
timeStart = time.clock()

fun__(strIn)

print('Time (sec):' + str(time.clock() - timeStart))




