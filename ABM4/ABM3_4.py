import random
import matplotlib.pyplot as plt
import operator
import agentframework as af

# Set the pseudo-random seed for reproducibility
random.seed(0)

# A variable to store the number of agents
n_agents = 100

n_iterations = 10

# Initialise agents
agents = []
for i in range(n_agents):
    # Create an agent
    agents.append(af.Agent(i))
    print(agents[i])


#initialise the movement variables 
# The minimum x coordinate.
x_min = 0
# The minimum y coordinate.
y_min = 0
# The maximum x coordinate.
x_max = 99
# The maximum y coordinate.         
y_max = 99


def get_distance(x0, y0, x1, y1):
    """
    Calculate the Euclidean distance between (x0, y0) and (x1, y1).

    Parameters
    ----------
    x0 : Number
        The x-coordinate of the first coordinate pair.
    y0 : Number
        The y-coordinate of the first coordinate pair.
    x1 : Number
        The x-coordinate of the second coordinate pair.
    y1 : Number
        The y-coordinate of the second coordinate pair.

    Returns
    -------
    distance : Number
        The Euclidean distance between (x0, y0) and (x1, y1).
    """
    # Calculate the difference in the x coordinates.
    dx = x0 - x1
    # Calculate the difference in the y coordinates.
    dy = y0 - y1
    # Square the differences and add the squares
    ssd = (dx * dx) + (dy * dy)
    # Calculate the square root
    distance = ssd ** 0.5
    return distance

def get_max_distance():
    """
    Calculate and return the maximum distance between all the agents

    Returns 
    -------
    max_distance : Number
        The maximum distance betwee all the agents.

    """
    # Loop through and calculate distances
    max_distance = 0
    for i in range(len(agents)):
        a = agents[i]
        for j in range(i+ 1, len(agents)):
            #print("i", i, "j", j)
            b = agents[j]
            distance = get_distance(a.x, a.y, b.x, b.y)
                #print("distance between", a, b, distance)
            max_distance = max(max_distance, distance)
                #print("max_distance", max_distance)
    return max_distance


# Move agents
agents[i].move(x_min, y_min, x_max, y_max)


# Plot the coordinate with the largest x red
lx = max(agents, key=operator.attrgetter('x'))
plt.scatter(lx.x, lx.y, color='red')
# Plot the coordinate with the smallest x blue
sx = min(agents, key=operator.attrgetter('x'))
plt.scatter(sx.x, sx.y, color='blue')
# Plot the coordinate with the largest y yellow
ly = max(agents, key=operator.attrgetter('y'))
plt.scatter(ly.x, ly.y, color='yellow')
# Plot the coordinate with the smallest y green
sy = min(agents, key=operator.attrgetter('y'))
plt.scatter(sy.x, sy.y, color='green')









