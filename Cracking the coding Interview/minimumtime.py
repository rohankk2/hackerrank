

import math
import os
import random
import re
import sys
# Complete the minTime function below.
def minTime(machines, goal):
    machines.sort()


    start=machines[0]
    end=goal*machines[-1]

    flag=0
    mid=0
    days=0
    nooftasks=0
    i=0

    while(end>start):
        mid=int((start+end)/2)
        nooftasks=0
        print('mid')
        print(mid)
        for ele in machines:
            nooftasks = nooftasks+ int(mid/ele);
        print('tasks')
        print(nooftasks)
        if(nooftasks>=goal):
            end=mid

        else:
            start=mid+1


    return start
