#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
edgelist=[]
visited={}
ans =1000000000
def DFS(root,val,curr):
    global edgelist,visited,ans
    visited[root]=1
    for edge in edgelist[root]:
        try:
            if(visited[edge]==1):
                continue

        except KeyError:
            curr=curr+1
            if(ids[edge-1]==val):
                print('entered')
                ans=min(ans,curr)
                print('ans')
                print(ans)
                curr=0

            curr = DFS(edge,val,curr)


    return curr


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    i=1
    global edgelist,visited,count,path,flag,ans
    edgelist.clear()
    visited.clear()
    curr=0
    ans=1000000000
    dfsstart=0
    cnt=0
    while(i<=graph_nodes+1):
        edgelist.append([])
        if(i-1<graph_nodes and ids[i-1]==val):

            cnt=cnt+1

            dfsstart=i
        i=i+1
    i=1


    while(i<=len(graph_from)):

        edgelist[graph_from[i-1]].append(graph_to[i-1])
        edgelist[graph_to[i-1]].append(graph_from[i-1])
        i=i+1

    if(dfsstart==0 or cnt<2 ):
        return -1
    else:
        DFS(dfsstart,val,curr)
        return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
