# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:26:50 2023

@author: cgkve
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:58:58 2023

@author: cgkve
"""

import random
from matplotlib import pyplot as plt
import time

# Set the pseudo-random seed for reproducibility
random.seed(0)

def get_distance(x0, y0, x1, y1):
    """
    Calculates the distance between coordinates (x0,y0) and (x1,y1) and returns
    the result.

    Parameters
    ----------
    x0 : Number
        An x coordinate.
    y0 : Number
        An y coordinate.
    x1 : Number
        An x coordinate.
    y1 : Number
        An y coordinate.

    Returns
    -------
    Number
        Distance between coordinates (x0,y0) and (x1,y1).

    """
    dx = x0 - x1 
    dy = y0 - y1
    return ((dx * dx ) + (dy * dy)) ** 0.5 

# Test get_distance
x0 = 0
y0 = 0
x1 = 3
y1 = 4
print(get_distance(x0,y0,x1,y1))

def get_max_distance(agents):
    """
    Calculates the maximum distance between coordinates and returns the result. 

    Parameters
    ----------
    agents : List 
        List of coordinate pairs.

    Returns
    -------
    max_distance : Number 
        Returns the maximum distance between coordinates.

    """
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
                #if i > j:
                #print(i, j)    
                b = agents[j]
                distance = get_distance(a[0], a[1], b[0], b[1])
                #print("distance between", a, b, distance)
                max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
    return max_distance 

# Create run_times list to store the time it takes to calculate distance as agents increase 
# Expect run times to increase with increase number of agents
run_times = [] 
startr = 500
stopr = 3001
stepr = 500
n_agents_range = range(startr, stopr, stepr)
print("n_agents_range", n_agents_range)
for n_agents in n_agents_range:
    # Initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
    # Time calculating the maximum distance between agents
    start = time.perf_counter()
    print("Maximum distance between all agents", get_max_distance(agents))
    end = time.perf_counter()
    run_time = end - start 
    print("Time taken to calculate maximum distance", run_time)
    run_times.append(run_time)
print(run_times)

# Plot
plt.title("Time taken to calculate maximum distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Time")
j = 0
for i in n_agents_range:
    plt.scatter(i, run_times[j], color='black')
    j = j + 1
plt.show() 










        
        

      

    

      
     
      
    