# Project Name
> Shortest Path with A* Algorithm <br>
> Built with Python3, Jupyter Notebook, Networkx, and Folium

## Table of contents
* [General Info](#general-info)
* [Screenshots](#screenshots)
* [Dependencies](#dependencies)
* [Setup](#setup)
* [Features](#features)
* [Author](#author)

## General Info
The A * (or A star) algorithm can be used to determine the shortest path from a point
to another point. In this project, the program will determine the shortest path based on the
Google Map of several location. From the road sections in the form of a graph. Node represent
a road crossing or the end of a road or a place. Assume the road is walkable from two directions. Weight
graph expresses the distance (m or km) between vertices. The distance between two vertices can be calculated from
coordinates of both vertices using the Euclidean distance formula (based on coordinates), or Haversine distance
(based on latitude and longitude) or using the ruler on Google Map, or other means provided by Google Map.

In this project, the graph built from txt file that contains number of nodes, latitude,longitude and node's name,
and weighted adjancency matrix. The weigted edges means the real distance between the two nodes (g(n) in A* algorithm).
The heuristic function (h(n)) will be calculated with the haversine formula between two nodes. The txt file used for testing is
located in the test folder.

Program written in Python3 (.py) and Jupyter Notebook (.ipynb) to visualize animated route with Folium library.
To visualize graph, this project use Networkx Library. All the dependencies needed will be written down below on the Dependencies section.

## Screenshots
<a href="https://imgbb.com/"><img src="https://i.ibb.co/kytY6XM/3394567-LINE.jpg" alt="3394567-LINE" border="0" title="test"></a> <br>
<a href="https://ibb.co/wQKDQBz"><img src="https://i.ibb.co/vdJ2dVj/Snip20210404-18.png" alt="Snip20210404-18" border="0"></a> <br>
<a href="https://ibb.co/G9zRr9d"><img src="https://i.ibb.co/ScFBZc6/Snip20210404-19.png" alt="Snip20210404-19" border="0"></a>

## Dependencies
```
Python 3.x
Numpy 1.20.2
Matplotlib 3.4.1
Networkx 2.5
Jupyter Notebook (or use Jupyter Extension in VSCode)
```
Install Dependencies <br>
You can run the first cell in the main.ipynb file. Or simply use pip3 to install
```
pip3 install numpy
pip3 install matplotlib
pip3 install networkx
pip3 install decorator==4.4.2
pip3 install folium
```
Note: The decorator v.4.4.2 is optional. If error happened while visualizing the networkx graph, you may try install this.

## Setup
There are several things that must be installed before running this program. We use the Visual Studio Code text-editor in the development process, here is an installation that is done to run the program via VSCode

1. Install Python version 3.8 or later, via VSCode. <br>
    Link: https://code.visualstudio.com/docs/python/python-tutorial

2. Install Jupyter Extension, via VSCode or install Jupyter Notebook <br>
Link: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

3. Install all dependencies needed on the Dependencies section before.
4. Program is ready to run


## Features
* Read a txt file (format like in test folder), and make a Graph with adjacency weigted matrix from it.
* A* Algorithm to find the shortest path (distance) between two nodes inside a graph
* Visualized the graph, with node, edges, and the shortest path. Green nodes and edges mean the path, while red aren't
* Visualized and animate the shortest path inside the real world map (Folium)

## Author
Created by :
- Rizky Anggita S Siregar (13519132)
- Wilson Tandya (13519228) <br>
Institut Teknologi Bandung <br>
2021