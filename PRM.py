import PRM_Functions
import random

def PRM(N,dmax,occ_grid):
    xmax = occ_grid.shape[0]-1
    ymax = occ_grid.shape[1]-1
    V = set()
    flag_sampling_vertex = 0    # Flag that keeps the status of the first sampled point. 
    while flag_sampling_vertex == 0:
        vnew = (random.randint(0,xmax),random.randint(0,ymax))   # Sampling the first point
        if occ_grid[vnew[0],vnew[1]] == 1 and vnew not in V:
            flag_sampling_vertex = 1   
    V.add(vnew)    # vnew added to the set V      
    neighbor = dict()
    for k in range(1,N+1):
        flag = 0
        while flag == 0:

            flag_sampling_vertex = 0    # Flag that keeps the status of the sampled point. 
            while flag_sampling_vertex == 0:
                vnew = (random.randint(0,xmax),random.randint(0,ymax))   # Newly sampled point
                if occ_grid[vnew[0],vnew[1]] == 1:
                    flag_sampling_vertex = 1  
                   # After the above while loop ends, we are certain that the newly sampled point lies in the unoccupied zone  
            (V,neighbor,flag) = PRM_Functions.add_vertex(V,neighbor,vnew,dmax,occ_grid)
 
    print("PRM Successful")
    return V,neighbor








