#!/bin/python3

import math
import os
import random
import re
import sys
import queue
visited={}
edgelist=[]
count=0
# Complete the roadsAndLibraries function below.
def DFS(root,c_road,c_lib):
        global edgelist,visited,count
        visited[root]=1
        for edge in edgelist[root]:


                try:
                     if(visited[edge]==1):
                              continue
                except KeyError:

                    count=count+min(c_road,c_lib)
                    DFS(edge,c_road,c_lib)










def roadsAndLibraries(n, c_lib, c_road, cities):
    global edgelist,visited
    edgelist.clear()
    visited.clear()

    i=1
    global count
    count=0
    while(i<=n+1):
        edgelist.append([])
        i=i+1

    for city in cities:
        edgelist[city[0]].append(city[1])
        edgelist[city[1]].append(city[0])
    print(edgelist)
    i=1
    while(i<=n):
        try:
            if(visited[i]==1):
                i=i+1
                continue
        except KeyError:
                         print('entered')
                         print(count)
                         count = count+c_lib

                         DFS(i,c_road,c_lib)
                         print('exit count')
                         print(count)
                         i=i+1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
