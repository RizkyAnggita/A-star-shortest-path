import os
import math
from queue import PriorityQueue
class Graph():
    def __init__(self, nNodes):
        self.nodes = []
        self.adj_matrix = []

        # Initialize Weighted Graph Adjacency Matrix
        for i in range(nNodes):
            col = []
            for j in range(nNodes):
                col.append(0)
            self.adj_matrix.append(col)

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, u, v, weight):
        index_u = self.nodes.index(u)
        index_v = self.nodes.index(v)
        self.adj_matrix[index_u][index_v] = weight
    
    def print_node(self):
        for node in self.nodes:
            print(node, end=" ")
        print()

    def print_graph(self):
        nNodes = len(self.nodes)
        print("  " *len(self.nodes[0]), end="" )
        self.print_node()
        for i in range (nNodes):
            for j in range (nNodes):
                if(j==0):
                    print(self.nodes[i], end=" ")
                print(self.adj_matrix[i][j], end=" ")
            print()
            """
    def BFS(self, s):
        edge_list = []
        for i in (self.nodes):
            for j in (self.nodes):
                if (i != j):
                    edge_list.append((i,j))
                        
        visited = [False] * (nNodes+1)
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            
            for i in edge_list[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    """

def add_graph_from_txt(g, nodeCoordinate, file):
    nodeCoordinate = []

    for i in range (nNodes):
        temp = file.readline()
        temp = temp.rsplit(" ")
        nodeCoordinate.append((int(temp[0]), int(temp[1])))
        g.add_node(temp[2].rstrip("\n"))

    for i in range (nNodes):
        j = 0
        temp = file.readline().rsplit(" ")
        
        for weight in temp:
            g.add_edge(g.nodes[i], g.nodes[j], int(temp[j].rstrip("\n")))
            j+= 1
    
    return nodeCoordinate

def euclidean_dist(pointA, pointB):
    # Menghitung jarak dua buah titik
    xKuad = (pointA[0] - pointB[0])**2
    yKuad = (pointA[1] - pointB[1])**2
    return math.sqrt(xKuad + yKuad)

# filename = input("Masukkan nama file: ")
filename = "input1.txt"
a = os.path.abspath(os.curdir)


if os.name=='nt':
    file_path = os.path.join(filename)
else:
    file_path = os.path.join(a, filename)

print(file_path)
f = open(file_path, "r")

nNodes = int(f.readline())
nodeCoordinate = []
g2 = Graph(nNodes)
nodeCoordinate = add_graph_from_txt(g2, nodeCoordinate, f)
"""
print("\nGRAPH: ")
g2.print_graph()
print()
print(nodeCoordinate)
print()
print(nodeCoordinate[0])
print(nodeCoordinate[1])

# Penggunaan euclidean_dist dan nodeCoordinate
a = euclidean_dist(nodeCoordinate[0], nodeCoordinate[1])
print(a)

"""
print(nodeCoordinate)
print(g2.nodes)
print(g2.adj_matrix[0])
Test = []
"""
From = input(str())
To = input(str())
#Dapetin node ke brp From sama To (asumsi node From dan To ada)
for i in range (len(g2.nodes)):
    if (From == g2.nodes[i]):
        FromNode = i
    if (To == g2.nodes[i]):
        ToNode = i
print("Element ke-", FromNode, "dan", ToNode)#TestPrint
"""
#temp_Hn = euclidean_dist(nodeCoordinate[FromNode], nodeCoordinate[ToNode])

#Hn Gn nya belom, prionya masih 0 semua ini
def BFS (g, From, To):
    #untuk mendapat yang belom ditelusuri
    def getAdjUnvisited():
        for i in range(len(g.nodes)):
            if (g.adj_matrix[idxFrom][i] > 0 and visitedVertices[i] == False):
                return (i)
    idxFrom = -1
    idxTo = -1
    pathFound = False
    visitedVertices = [False for i in range (len(g.nodes))]
    q = PriorityQueue()
    for i in range (len(g.nodes)):
        if (From == g.nodes[i]):
            idxFrom = i
        if (To == g.nodes[i]):
            idxTo = i
    visitedVertices[idxFrom] = True
    q.put((0, From))

    Pembangkit = [0 for i in range (len(g.nodes))]
    while(not q.empty() and not pathFound):
        temp = q.get()
        print(temp[0])
        print(temp[1])
        idxUnv = getAdjUnvisited()
        if (getAdjUnvisited() != -1):
            q.put((2, temp[1]+'-'+(g.nodes[idxUnv])))
            visitedVertices[idxUnv] = True
            Pembangkit[idxUnv] = True
            if(idxUnv == idxTo):
                #print(q.get())
                pathFound = True
        while(idxUnv != -1 and not pathFound):
            idxUnv = getAdjUnvisited()
            if (getAdjUnvisited() != -1):
                q.put((2, temp[1]+'-'+(g.nodes[idxUnv])))
                visitedVertices[idxUnv] = True
                Pembangkit[idxUnv] = True
                if(idxUnv == idxTo):
                    #print(q.get())
                    pathFound = True
    
    
    
BFS(g2, 'A', 'B')

#q = PriorityQueue()
#q.put((1, 'From'))


