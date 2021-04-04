import queue
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Utility import haversin, rad

# Self-made Graph Class
# Graph implemented with list of nodes and adjacency weigted matrix
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

    # A* method
    def AStar(self, From, To, nodeCoordinate):
        def construct_path(cameFrom, From, To, self):
            path = []
            idxFrom = self.nodes.index(From)
            idxTo = self.nodes.index(To)

            i = idxTo
            path.append(self.nodes[idxTo])
            while(i != idxFrom):
                path.append(cameFrom[i])
                i = self.nodes.index(cameFrom[i])
            
            path.reverse()
            return path

        def isInPrioQueue(prioQueue, node):
            for item in prioQueue.queue:
                if(item[1] == node):
                    return True
            return False

        found = False
        openSet = queue.PriorityQueue()
        idxFrom = self.nodes.index(From)
        idxTo = self.nodes.index(To)

        f2 = 0 + haversin(nodeCoordinate[idxFrom], nodeCoordinate[idxTo])
        openSet.put((f2, From))

        # // For node n, gn[n] is the cost of the cheapest path from start to n currently known.
        gn = []
        
        # // For node n, fn[n] := gn[n] + h(n). fn[n] represents our current best guess as to
        # // how short a path from start to finish can be if it goes through n.
        fn = []
        cameFrom = []

        for node in self.nodes:
            if (node==From):
                gn.append(0)
                fn.append(haversin(nodeCoordinate[idxFrom], nodeCoordinate[idxTo]))
            else:
                gn.append(99999)
                fn.append(99999)
            cameFrom.append("")

        while (not openSet.empty() and not found):
            current = openSet.get()
            currentIdx = self.nodes.index(current[1])

            if(current[1] == To):
                print("FOUND\n")
                found = True
            
            # Foreach neighbour of current
            # neighbour is every node that connected with current node
            # with weight > 0
            for i in range(len(self.nodes)):
                if (self.adj_matrix[currentIdx][i] > 0):
                    #  tentative_gn is the distance from start to the neighbor through current
                    # d jarak dari node current ke tetangganya (weigthnya)
                    d = self.adj_matrix[currentIdx][i]
                    tentative_gn = gn[currentIdx] + d
                    
                    # kalau kita mengunjungi node yang sama dua kali, kita cek apakah gn node ini
                    # lebih pendek jika dibandingkan dengan tentative_gn, yaitu dikunjungi melalui node lain
                
                    if (tentative_gn < gn[i]):
                        cameFrom[i] = current[1]
                        gn[i] = tentative_gn
                        titikNeighbour = nodeCoordinate[i]
                        hn = haversin(titikNeighbour, nodeCoordinate[idxTo])
                        fn[i] = gn[i] + hn

                        if not (isInPrioQueue(openSet, self.nodes[i])):
                            openSet.put((fn[i], self.nodes[i]))
        if found:               
            return True, construct_path(cameFrom, From, To, self), gn
        else:
            return False, construct_path(cameFrom, From, To, self), gn

    def visualize_graph(self, solusi):
        g2 = self
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
        nx.draw(G, layout, node_size=1000, width=5, node_color = color_map, edge_color = edge_colors, labels=mylabels, with_labels=True, arrows=False)
        jarak = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=jarak)
        plt.show()