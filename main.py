from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import AuxillaryFunctions
import A_star_search
import PRM
import PRM_Functions
import networkx as nx


# Accessing the occupancy grid
image = Image.open("YOUR PATH/occupancy_map.png")
occ_grid_orig = np.asarray(image)   # This gives a non-mutable numpy array. 
occ_grid = occ_grid_orig.copy()     # Copying this to another array which is mutable
for i in range(occ_grid.shape[0]):
    for j in range(occ_grid.shape[1]):
        if occ_grid[i,j]!=0 :
            occ_grid[i,j] = 1         # Getting a binary occupancy grid map


s = (635,140)    # Start node
g = (350,400)    # End node
V= set()  # Set of vertices
neighbor = dict()  # dictiionary to store set of neighbors

for i in range(occ_grid.shape[0]):
    for j in range(occ_grid.shape[1]):
        if occ_grid[i,j] == 1:
            v = (i,j)
            V.add(v)
            neighbor[v] = AuxillaryFunctions.N(v,occ_grid)  

# Applying A*
path = A_star_search.A_star(V,neighbor,s,g)
print("Length of path for A* on grid map is :")
print(AuxillaryFunctions.pathlength(path))
occ_grid1 = occ_grid_orig.copy()     # Copying this to another array which is mutable
array = np.random.randint(255, size=(700, 700),dtype=np.uint8)
print("Number of nodes on the path found by A*")
print(len(path))
# Darkening the pixels that lie on the path found by A*
for i in path:
    occ_grid1[i[0]][i[1]]=0
image = Image.fromarray(occ_grid1)
image.show()

X = []
Y = []
for i in path:
    X.append(i[1])
    Y.append(i[0])
plt.imshow(image)
plt.plot(X,Y)
plt.show()
######################## PRM ##################################
N = 2500
dmax = 75
V1,neighbor1 = PRM.PRM(N,dmax,occ_grid)
occ_grid1 = occ_grid_orig.copy()     # Copying this to another array which is mutable
array = np.random.randint(255, size=(700, 700),dtype=np.uint8)


# Darkening the pixels sampled by the PRM algorithm
for i in V1:
     occ_grid1[i[0]][i[1]]=0
image = Image.fromarray(occ_grid1)
image.show()

(V1,neighbor1,start_flag) = PRM_Functions.add_vertex(V1,neighbor1,s,dmax,occ_grid)     # Adding start node to the PRM graph
(V1,neighbor1,end_flag) = PRM_Functions.add_vertex(V1,neighbor1,g,dmax,occ_grid)       # Adding the end node to the PRM graph
path = A_star_search.A_star(V1,neighbor1,s,g)
occ_grid1 = occ_grid_orig.copy()     # Copying this to another array which is mutable
print("Number of nodes on the path found by A*")
print(len(path))

print("Length of path for A* on PRM is :")
print(AuxillaryFunctions.pathlength(path))
# Darkening the pixels that lie on A* path found on PRM graph. 
for i in path:
    for p in range(-4,4):    # delta x
         for q in range(-4,4):   # delta y
             occ_grid1[i[0]+p][i[1]+q]=0
image = Image.fromarray(occ_grid1)
image.show()


# G = nx.Graph()
# for v in V1:
#     G.add_node(v)

# for v in neighbor1.keys():
#     for n in neighbor1[v]:
#         if G.has_edge(v,n) or G.has_edge(n,v):
#         #if n in G[v] or v in G[n]:
#             continue
#         else :
#             G.add_edge(v,n)
#             G.edges[v,n]['weight'] = AuxillaryFunctions.w(v,n)

# pos=nx.spring_layout(G)
# nx.draw(G,pos)
# edge_labels=dict([((fe,se,),e['egdes'])
#             for fe,se,e in G.edges(data=True)])

# nx.draw_networkx_edge_labels(G,pos,edge_labels)
#pylab.show()
# Final plotting. A bit more decent method than just darkening pixels
# pos = {}
# for i in G.nodes():
#     pos[i] = (i[1],i[0])
# nx.draw_networkx(G,pos=pos,node_size=1.5,with_labels=0,width=0.2,node_color='blue',edge_color='orange')
X = []
Y = []
for i in path:
    X.append(i[1])
    Y.append(i[0])
    plt.plot(i[1],i[0],'bo')
plt.imshow(image)
plt.plot(X,Y)
xV = []
yV = []
for i in V1:
    xV.append(i[1])
    yV.append(i[0])
plt.scatter(xV,yV,c ="red",s = 5)
plt.show()

