import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

def planLineLow(v0,v1):           # Takes in tuples of vertices. 
    pixels = []
    dx = v1[0]-v0[0]
    dy = v1[1]-v0[1]
    yi = 1
    if dy<0:
        yi = -1
        dy = -dy
    D = (2 * dy) - dx
    y = v0[1]
    for x in range(v0[0],v1[0]+1):
        pixels.append((x,y))  # Adding the tuple to the list
        if D>0 :
            y = y + yi
            D = D + (2*(dy-dx))
        else :
            D = D + 2*dy
    return pixels


def planLineHigh(v0,v1):           # Takes in tuples of vertices. 
    pixels = []
    dx = v1[0]-v0[0]
    dy = v1[1]-v0[1]
    xi = 1
    if dx<0:
        xi = -1
        dx = -dx
    D = (2 * dx) - dy
    x = v0[0]
    for y in range(v0[1],v1[1]+1):
        pixels.append((x,y))  # Adding the tuple to the list
        if D>0 :
            x = x + xi
            D = D + (2*(dx-dy))
        else :
            D = D + 2*dx
    return pixels


def planLine(v0,v1) :
    pixels = []
    if abs(v1[1]-v0[1])<abs(v1[0]-v0[0]):
        if v0[0]>v1[0] :
            pixels = planLineLow(v1,v0)
        else :
            pixels = planLineLow(v0,v1)
    else :
        if v0[1]>v1[1] :
            pixels = planLineHigh(v1,v0)
        else :
            pixels = planLineHigh(v0,v1)
    return pixels


def check_feasibility(v0,v1,occ_grid):
    pixels = planLine(v0,v1)
    flag = 1
    for v in pixels:
        if occ_grid[v[0],v[1]] == 0:
            flag = 0
            break
    return flag


def add_vertex(V,neighbor,vnew,dmax,occ_grid):
    flag = 0
    nv = set()     # Set of neighbors for vnew
    for v in V:
        dist = LA.norm([v[0]-vnew[0],v[1]-vnew[1]])

        if dist<=dmax :
            if check_feasibility(v,vnew,occ_grid) == 1:
                nv.add(v)
                if v in neighbor.keys():
                    neighbor_set = neighbor[v]
                    neighbor_set.add(vnew)
                    neighbor[v] = neighbor_set
                else :
                    neighbor[v] = {vnew}       # Creating a new neighbor entry in the dictionary if the vertex didn't exist before in the dictionary. 
                if flag==0:
                    flag=1
    V.add(vnew)
    if flag==1:
        neighbor[vnew] = nv
    
    return V,neighbor,flag      # Returning V, neighbors with the appropriate changes. 