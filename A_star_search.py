import AuxillaryFunctions

def A_star(V,neighbor,s,g):
    path = []     # Initializing an empty path     
    EstTotalCost = dict()
    CostTo = dict()
    h = dict() # Dictionary to store heuristic
    EstTotalCost[s] = AuxillaryFunctions.w(s,g)   # Cost for start node to reach goal 
    pred = dict() # Dictionary to store the predecessors. 
    for v in V:
        CostTo[v] = float('inf')
        EstTotalCost[v] = float('inf')
        h[v] = AuxillaryFunctions.w(v,g)  
    CostTo[s] = 0  # Cost to s is zero
    EstTotalCost[s] = h[s]    # Setting heuristic for start node as the estimated total cost for the node.
    Q = dict()    # Initializing the queue dictionary
    Q[s] = EstTotalCost[s]
    while len(Q)>0 :
        v = list(Q.keys())[0]    # Getting the vertex with the smallest estimated total cost. The dictionary is sorted by value of est total cost. 
        del Q[v]  # Removing that vertex from the dictionary
        if v==g:
            print('Recovering path ... ')
            path = AuxillaryFunctions.RecoverPath(s,g,pred)
            print("Path Recovered : A* successful")
            return path
        for i in neighbor[v]:
            pvi = CostTo[v] + AuxillaryFunctions.w(v,i)  # Represents the total cost to get TO THE NODE i
            if pvi < CostTo[i] :
                pred[i] = v 
                CostTo[i] = pvi
                EstTotalCost[i] = pvi + h[i]
                Q[i] = EstTotalCost[i]    # Updating the estimated total cost of the vertex in the dictionary
                dict(sorted(Q.items(), key=lambda item: item[1]))   # Sorting the dictionary. 

    return path



