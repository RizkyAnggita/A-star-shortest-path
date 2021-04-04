import math

def add_graph_from_txt(g, nodeCoordinate, file, nNodes):
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

def SearchIdxNode(N, g):
    for i in range(len(g.nodes)):
        if (N == g.nodes[i]):
            return i