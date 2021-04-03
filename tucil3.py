import os
import math
import queue
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

def add_graph_from_txt(g, nodeCoordinate, file):
    nodeCoordinate = []

    for i in range (nNodes):
        temp = file.readline()
        temp = temp.rsplit(" ")
        nodeCoordinate.append((float(temp[0]), float(temp[1])))
        g.add_node(temp[2].rstrip("\n"))

    for i in range (nNodes):
        j = 0
        temp = file.readline().rsplit(" ")
        
        for weight in temp:
            g.add_edge(g.nodes[i], g.nodes[j], float(temp[j].rstrip("\n")))
            j+= 1
    
    return nodeCoordinate

def rad (x):
    return x*math.pi / 180

def haversin (p1, p2):
    R = 6378137 #Radius Bumi dalam meter
    dLat = rad(p2[0] - p1[0])
    dLong = rad(p2[1] - p1[1])
    a = (math.sin (dLat / 2))**2 + math.cos (rad(p1[0])) * math.cos (rad(p2[0])) * (math.sin(dLong / 2))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    res = R * c
    return res

def euclidean_dist(pointA, pointB):
    # Menghitung jarak dua buah titik
    xKuad = (pointA[0] - pointB[0])**2
    yKuad = (pointA[1] - pointB[1])**2
    return math.sqrt(xKuad + yKuad)

# filename = input("Masukkan nama file: ")
filename = "BuahBatu.txt"
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

#Hn Gn nya belom, prionya masih 0 semua ini
def AStar (g, From, To):
    #untuk mendapat yang belom ditelusuri
    def getAdjUnvisited(visitedVertices):
        for i in range(len(g.nodes)):
            if (g.adj_matrix[idxFrom][i] > 0 and visitedVertices[i] == False):
                return (i)
        return -1
    
    def newVisitedVertices():
        newVisitedVertices = [False for i in range(len(g.nodes))]
        
        for i in range (len(currNode)):
            newVisitedVertices[SearchIdxNode(currNode[i])] = True
        #print(visitedVertices)
        return newVisitedVertices
    
    def SearchIdxNode(N):
        for i in range(len(g.nodes)):
            if (N == g.nodes[i]):
                return i
        return -1
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
        #dequeue yang ditelusuri
        print("LOOP BESAR")
        temp = q.get()
        currNode = temp[1].split('-')
        print("temp[1]:",temp[1])
        #print(currNode[-1])
        From = str(currNode[-1])
        idxFrom = SearchIdxNode(From)
        print(currNode)
        #G(n) : jarak yang telah ditempuh sampai ke simpul tersebut
        Gn = 0
        for i in range(len(currNode)-1):
            a = SearchIdxNode(currNode[i])
            b = SearchIdxNode(currNode[i+1])
            Gn += g.adj_matrix[a][b]
        print("G(n):",Gn)
        #H(n) : jarak garis lurus titik sekarang ke tujuan
        Hn = haversin(nodeCoordinate[SearchIdxNode(currNode[-1])], nodeCoordinate[SearchIdxNode(To)])
        print("H(n):",Hn)

        Fn = Gn + Hn
        print("F(n):", Fn)

        visitedVertices = newVisitedVertices()
        print(visitedVertices)

        idxUnv = getAdjUnvisited(visitedVertices)
        print("Indeks:", idxUnv)
        
        if (getAdjUnvisited(visitedVertices) != -1):
            q.put((Fn, temp[1]+'-'+(g.nodes[idxUnv])))
            visitedVertices[idxUnv] = True
            Pembangkit[idxUnv] = True
            if(SearchIdxNode(currNode[-1]) == idxTo):
                print("KETEMU")
                #print(q.get())
                pathFound = True
        while(idxUnv != -1 and not pathFound):
            idxUnv = getAdjUnvisited(visitedVertices)
            if (getAdjUnvisited(visitedVertices) != -1):
                q.put((Fn, temp[1]+'-'+(g.nodes[idxUnv])))
                visitedVertices[idxUnv] = True
                Pembangkit[idxUnv] = True
                if(SearchIdxNode(currNode[-1]) == idxTo):
                    print(q.get())
                    print("KETEMUBWAH")
                    pathFound = True
    print(currNode)
    


From = input(str("Asal:"))
To = input(str("Tujuan:"))
AStar(g2, From, To)

print("KODE VERSI 2")
print()
print()
def isInPrioQueue(prioQueue, node):
    for item in prioQueue.queue:
        if(item[1] == node):
            return True
    return False
openSet = queue.PriorityQueue()
path = []

# titikA = nodeCoordinate[g2.nodes.index("A")]
# titikB = nodeCoordinate[g2.nodes.index("B")]
# titikC = nodeCoordinate[g2.nodes.index("C")]
# titikD = nodeCoordinate[g2.nodes.index("D")]
# titikE = nodeCoordinate[g2.nodes.index("E")]

idxFrom = g2.nodes.index(From)
idxTo = g2.nodes.index(To)

f2 = 0 + haversin(nodeCoordinate[idxFrom], nodeCoordinate[idxTo])
openSet.put((f2, From))

# // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
gScore = []

# // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
# // how short a path from start to finish can be if it goes through n.
fScore = []
cameFrom = []

for node in g2.nodes:
    if (node==From):
        gScore.append(0)
        fScore.append(haversin(nodeCoordinate[idxFrom], nodeCoordinate[idxTo]))
    else:
        gScore.append(999)
        fScore.append(999)
    cameFrom.append("")

g2.print_graph()
while (not openSet.empty()):
    print("Kondisi PrioQueue: ", end ="")
    print(openSet.queue)
    current = openSet.get()
    currentIdx = g2.nodes.index(current[1])
    print("Current Node:" + g2.nodes[currentIdx])
    if(current[1] == To):
        print("DONE")
        break
    print()
    # Foreach neighbour of current
    # neighbour is every node that connected with current node
    # with weight > 0
    for i in range(nNodes):
        if (g2.adj_matrix[currentIdx][i] > 0):
            #  tentative_gScore is the distance from start to the neighbor through current
            # d jarak dari node current ke tetangganya (weigthnya)
            d = g2.adj_matrix[currentIdx][i]
            tentative_gScore = gScore[currentIdx] + d
            
            # kalau kita mengunjungi node yang sama dua kali, kita cek apakah gScore node ini
            # lebih pendek jika dibandingkan dengan tentative_gscore, yaitu dikunjungi melalui node lain
        
            if (tentative_gScore < gScore[i]):
                cameFrom[i] = current[1]
                gScore[i] = tentative_gScore
                titikNeighbour = nodeCoordinate[i]
                hn = haversin(titikNeighbour, nodeCoordinate[idxTo])
                fScore[i] = gScore[i] + hn

                if not (isInPrioQueue(openSet, g2.nodes[i])):
                    openSet.put((fScore[i], g2.nodes[i]))

for i in range(5):
    print(haversin(nodeCoordinate[i], nodeCoordinate[4]))

print(openSet.queue)
# Ini tinggal di traceback gitu
print("Tinggal di-traceback dari node tujuan ke awal")
print(cameFrom)

print("Jarak : " , gScore[idxTo])