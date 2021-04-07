import os
import folium
from folium import plugins
from Graph import Graph
from Utility import add_graph_from_txt, SearchIdxNode

# A* Algorithm for Shortest Path Finding
# Author    :
#               Rizky Anggita S Siregar - 13519132
#               Wilson Tandya           - 13519228
# Date      :   04-03-2021


# Install this dependency if it's not installed
# Install numpy -> pip3 install numpy
# Install matplotlib -> pip3 install matplotlib
# Install networkx -> pip3 install networkx
# Install decorator v4.4.2 -> pip install decorator==4.4.2
# Install folium -> pip3 install folium

# ------Main Program-------

filename = input(str("Masukkan nama file: "))
filename = filename+".txt"
a = os.path.abspath(os.curdir)

if os.name=='nt':
    file_path = os.path.join("..\\test", filename)
else:
    file_path = os.path.join(a, "test", filename)

f = open(file_path, "r")

nNodes = int(f.readline())
nodeCoordinate = []
g2 = Graph(nNodes)
nodeCoordinate = add_graph_from_txt(g2, nodeCoordinate, f, nNodes)
daftarNode = g2.nodes

print("Daftar Titik yang dapat dikunjungi: ")
print(daftarNode)

From = input(str("Asal  : "))
To = input(str("Tujuan  : "))

while (From not in daftarNode or To not in daftarNode):
    print("Node tidak terdapat pada graph, silahkan input ulang!")
    From = input(str("Asal:"))
    To = input(str("Tujuan:"))

found, solusi, gn = g2.AStar(From, To, nodeCoordinate)

if not found:
    print("Lintasan tidak dapat ditemukan!")
else:
    print("Solusi A*: ", end = "")
    for i in range (len(solusi)):
        if (i != len(solusi) - 1):
            print(solusi[i], end = " → ")
        else:
            print(solusi[i])
    print("Jarak tempuh: ", gn[g2.nodes.index(To)], " meter")
    g2.visualize_graph(solusi)

    # Visualizing route with Folium
    # Use the Jupyter Notebook version of this program to see this

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
    for i in range (len(solusi)):
        mapHasil.append(nodeCoordinate[SearchIdxNode(solusi[i], g2)])
        

    visualisasiMap = folium.Map(location=coordinates[0], zoom_start=16)
    for index,lat in enumerate(latitude):
        folium.Marker([lat,
        longitude[index]],
        popup=('{} \n'.format(name[index])),
        icon = folium.Icon(color='blue'), tooltip=name[index]).add_to(visualisasiMap)
        #Buat Ant Path dari jalur yang ditempuh
        plugins.AntPath(locations=mapHasil,weight=5, color = "green").add_to(visualisasiMap)
    #Menampilkan visualisasi peta pada jupyter notebook, ada animasi jalannya :)
    visualisasiMap

