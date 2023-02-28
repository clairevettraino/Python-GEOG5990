# -*- coding: utf-8 -*-

import random
from matplotlib import pyplot as plt
import statistics 

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 10

# distance
def get_distance(x0, y0, x1, y1):
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    return (ssd ** 0.5) 



# function to get mean distance 
def get_sorted_distance(i):
    # Loop through and calculate distances
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i + 1, len(agents)):
            b = agents[j]
            distance = get_distance(a[0], a[1], b[0], b[1])
    return distance



# init agents because the function above needs to be called (after the function)
agents = []
for i in range(n_agents):
         agents.append([random.randint(0, 99), random.randint(0, 99)])
#print(agents)


# gets results for each agent in n_agents 
for i in range(n_agents):
    r = get_sorted_distance(i)
    print(r)
 
    
 
# store distances
# A list to store items 
distances = []
n_agents_range = range(5, 50, 5)
for n_agents in n_agents_range:
    # Initialise agents
    agents = []
    for i in range(n_agents):
        agents.append([random.randint(0, 99), random.randint(0, 99)])
    #print(agents)
    # Print the maximum distance between all the agents
    print("The distance is", get_sorted_distance(i))
    distances.append(get_sorted_distance(i))
    
#sort the list 
distances.sort() 
print(distances) 
print(statistics.median(distances)) 
print(statistics.mode(distances)) 

    

# Plot
plt.title("Median distance for different numbers of agent")
plt.xlabel("Number of agents")
plt.ylabel("Median distance")
j = 0
for i in n_agents_range:
    plt.scatter(i, distances[j], color='black')
    j = j + 1
plt.show()

