import queue

class Graph:
    def __init__(self,n):
        self.nodes=n

        self.edgelist=[]
        self.distances={}
        self.visited={}
        self.mapping={}
        self.distances[0]=-1
        i=1
        while(i<=self.nodes+1):
            self.edgelist.append([])
            i=i+1
    def connect(self,edge1,edge2):

        self.edgelist[edge1+1].append(edge2+1)
        self.edgelist[edge2+1].append(edge1+1)
    def getedgelist(self):
        print(edgelist)
    def find_all_distances(self,index):
        index=index+1
        q= queue.Queue()
        q.put(index)

        dist=0
        self.distances[index]=0
        self.visited[index]=1
        while(not q.empty()):
            ele=0
            ele = q.get()

            for edge in self.edgelist[ele]:

                try:
                    if(self.visited[edge]==1):
                        continue
                except KeyError:

                              self.visited[edge]=1
                              self.distances[edge]=self.distances[ele]+6
                              q.put(edge)

        i=1

        while(i<=self.nodes):
            if(i==index):
                i=i+1
                continue
            try:
                if(self.distances[i]>0):
                    print(self.distances[i],end=' ')
            except KeyError:
                    print(-1,end=' ')

            i=i+1
        print()






t = int(input())

for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
