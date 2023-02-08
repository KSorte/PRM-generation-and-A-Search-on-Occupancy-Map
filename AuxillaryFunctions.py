import numpy as np
from numpy import linalg as LA

def N(v,occ_grid):
    neighbor_set = set()
    
    i = v[0]
    j = v[1]
    for p in range(-1,2): # three rows it will check. The upper row, the lower row and the current row
        #print(p)
        for q in range(-1,2):
            #print(q)
            if p==0 and q==0:   
                continue
            elif i+p>=0 and i+p<=occ_grid.shape[0]-1 and j+q>=0 and j+q<=occ_grid.shape[1]-1 :  # Inside the square. 
                #print("Inside square IF")
                if occ_grid[i+p,j+q] == 1 :
                    neighbor_set.add((i+p,j+q))  
            else : continue 
    # print("Output of neighbor function N :")
    # print(neighbor_set)
    return neighbor_set

def w(v1,v2):
    return LA.norm([v2[0]-v1[0],v2[1]-v1[1]])

def RecoverPath(s,g,pred): # Takes in the predecessor dictionary
    list = [g]
    v = g   # Setting v as the goal node. 
    while v!=s:
        list.insert(0,pred[v])
        v = pred[v]   # Setting v as the predecessor
    return list


def pathlength(path):
    length = 0
    for i in range(0,len(path)-1):
        length = length + w(path[i],path[i+1])
    return length
