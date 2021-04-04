import os
import math
import queue
from queue import PriorityQueue
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import folium
from folium import plugins


# Install numpy -> pip3 install numpy
# Install matplotlib -> pip3 install matplotlib
# Install networkx -> pip3 install networkx
# Install decorator v4.4.2 -> pip install decorator==4.4.2
# Install folium -> pip install folium
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
                #if(j==0):
                #    print(self.nodes[i], end=" ")
                print(self.adj_matrix[i][j], end=" \t")
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


filename = input(str("Masukkan nama file: "))
filename = filename+".txt"
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


def SearchIdxNode(N, g):
        for i in range(len(g.nodes)):
            if (N == g.nodes[i]):
                return i
'''
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
        temp = q.get()
        currNode = temp[1].split('-')
        #print("temp[1]:",temp[1])
        From = str(currNode[-1])
        idxFrom = SearchIdxNode(From)
        #print(currNode)

        #G(n) : jarak yang telah ditempuh sampai ke simpul tersebut
        Gn = 0
        for i in range(len(currNode)-1):
            a = SearchIdxNode(currNode[i])
            b = SearchIdxNode(currNode[i+1])
            Gn += g.adj_matrix[a][b]
        #print("G(n):",Gn)
        #H(n) : jarak garis lurus titik sekarang ke tujuan
        Hn = haversin(nodeCoordinate[SearchIdxNode(currNode[-1])], nodeCoordinate[SearchIdxNode(To)])
        #print("H(n):",Hn)

        Fn = Gn + Hn
        #print("F(n):", Fn)

        visitedVertices = newVisitedVertices()
        #print(visitedVertices)

        idxUnv = getAdjUnvisited(visitedVertices)
        #print("Indeks:", idxUnv)
        
        if (getAdjUnvisited(visitedVertices) != -1):
            q.put((Fn, temp[1]+'-'+(g.nodes[idxUnv])))
            visitedVertices[idxUnv] = True
            Pembangkit[idxUnv] = True
            if(SearchIdxNode(currNode[-1]) == idxTo):
                pathFound = True
        while(idxUnv != -1 and not pathFound):
            idxUnv = getAdjUnvisited(visitedVertices)
            if (getAdjUnvisited(visitedVertices) != -1):
                q.put((Fn, temp[1]+'-'+(g.nodes[idxUnv])))
                visitedVertices[idxUnv] = True
                Pembangkit[idxUnv] = True
                if(SearchIdxNode(currNode[-1]) == idxTo):
                    pathFound = True
    return (currNode)
'''

def AStarV2(g, From, To):
    def construct_path(cameFrom, From, To, g):
        path = []
        idxFrom = g.nodes.index(From)
        idxTo = g.nodes.index(To)

        i = idxTo
        path.append(g.nodes[idxTo])
        while(i != idxFrom):
            print(i)
            path.append(cameFrom[i])
            i = g.nodes.index(cameFrom[i])
        
        path.reverse()
        return path

    def isInPrioQueue(prioQueue, node):
        for item in prioQueue.queue:
            if(item[1] == node):
                return True
        return False

    openSet = queue.PriorityQueue()
    idxFrom = g.nodes.index(From)
    idxTo = g.nodes.index(To)

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
            gScore.append(99999)
            fScore.append(99999)
        cameFrom.append("")

    while (not openSet.empty()):
        print("Kondisi PrioQueue: ", end ="")
        print(openSet.queue)
        current = openSet.get()
        currentIdx = g.nodes.index(current[1])
        print("Current Node:" + g.nodes[currentIdx])
        if(current[1] == To):
            print("DONE")
            break
        print()
        # Foreach neighbour of current
        # neighbour is every node that connected with current node
        # with weight > 0
        for i in range(nNodes):
            if (g.adj_matrix[currentIdx][i] > 0):
                #  tentative_gScore is the distance from start to the neighbor through current
                # d jarak dari node current ke tetangganya (weigthnya)
                d = g.adj_matrix[currentIdx][i]
                tentative_gScore = gScore[currentIdx] + d
                
                # kalau kita mengunjungi node yang sama dua kali, kita cek apakah gScore node ini
                # lebih pendek jika dibandingkan dengan tentative_gscore, yaitu dikunjungi melalui node lain
            
                if (tentative_gScore < gScore[i]):
                    cameFrom[i] = current[1]
                    gScore[i] = tentative_gScore
                    titikNeighbour = nodeCoordinate[i]
                    hn = haversin(titikNeighbour, nodeCoordinate[idxTo])
                    fScore[i] = gScore[i] + hn

                    if not (isInPrioQueue(openSet, g.nodes[i])):
                        openSet.put((fScore[i], g.nodes[i]))

    return construct_path(cameFrom, From, To, g), gScore
    
def visualize_graph(g2, solusi):

    adj_np = np.array(g2.adj_matrix)
    namaNode = g2.nodes
    mylabels = {}
    for i in range (len(namaNode)):
        mylabels[i] = namaNode[i]
 
    G = nx.from_numpy_matrix(adj_np, create_using=nx.DiGraph)
    color_map = []
    edge_colors = []    
    solusi_idx = []

    for i in range (len(solusi)):
        a = g2.nodes.index(solusi[i])
        solusi_idx.append(a)
        
    for node in G.nodes:
        if node in solusi_idx:
            color_map.append("green")
        else:
            color_map.append("red")

    for edges in G.edges:
        if(edges[0] in solusi_idx and (edges[1] in solusi_idx) ):
            edge_colors.append("green")
        else:
            edge_colors.append("red")

    layout = nx.spring_layout(G)
    nx.draw(G, layout, node_size=1000, node_color = color_map, edge_color = edge_colors, labels=mylabels, with_labels=True, arrows=False)
    jarak = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=jarak)
    plt.show()

# -----MAIN------
g2.print_graph()
From = input(str("Asal:"))
To = input(str("Tujuan:"))
#solusi = AStar(g2, From, To)
solusi2, gScore = AStarV2(g2, From, To)



for i in range(5):
    print(haversin(nodeCoordinate[i], nodeCoordinate[4]))

#print("Solusi A* V1: ", solusi)

print("Solusi A* V2: ", solusi2)
print("Jarak tempuh: ", gScore[g2.nodes.index(To)])

visualize_graph(g2, solusi2)

#Koordinat lokasi dari file eksternal
coordinates = []  
for i in (nodeCoordinate):
    coordinates.append(i)

name = []
for i in (g2.nodes):
    name.append(i)

latitude = []
longitude = []
for i in range(len(coordinates)):
    latitude.append(coordinates[i][0])
    longitude.append(coordinates[i][1])

#Koordinat jalur shortest path
mapHasil = []
for i in range (len(solusi2)):
    mapHasil.append(nodeCoordinate[SearchIdxNode(solusi2[i], g2)])
      

visualisasiMap = folium.Map(location=coordinates[0], zoom_start=16)
for index,lat in enumerate(latitude):
    folium.Marker([lat,
    longitude[index]],
    popup=('{} \n'.format(name[index])),
    icon = folium.Icon(color='blue'), tooltip=name[index]).add_to(visualisasiMap)
    #Buat Ant Path dari jalur yang ditempuh
    plugins.AntPath(locations=mapHasil,weight=5, color = "green").add_to(visualisasiMap)
visualisasiMap

