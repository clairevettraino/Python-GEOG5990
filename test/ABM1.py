# import random 
import random 

# Set the pseudo-random seed for reproducibility
random.seed(0)

# Initialise variable x0
x0 = 0
print("x0", x0)

# Initialise variable y0
y0 = 0 
print("y0", y0)

# Change x0 and y0 randomly
rn = random.random()
print(rn)

# changing x0
if rn < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print("x0", x0)

#changing y0
if rn < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print("y0", y0)

# Initialise variable x1
x1 = 3
print("x1", x1)

# Initialise variable y1
y1 = 4
print("y1", y1)

# Change x1 and y1 randomly
rn2 = random.random()
print(rn2)

# changing x1
if rn2 < 0.5:
    x1 = x1 + 1 
else:
    x1 = x1 -1 
print("x1", x1)

# changing y1
if rn2 < 0.5:
    y1 = y1 +1
else:
    y1 = y1 - 1
print("y1", y1)

# change coordinate initialisation to 0 - 99 
rn3 = random.randint(0, 99)
print(rn3)




# Calculate the Euclidean distance between (x0, y0) and (x1, y1)
# Calculate the difference in the x coordinates.
distx = x1 - x0 
print(distx)

# Calculate the difference in the y coordinates.
disty = y1 - y0
print(disty)

# Square the differences and add the squares
squarex = distx*distx
print(squarex)

squarey = disty*disty
print(squarey)

squares = squarex + squarey 
print(squares)

# Calculate the square root
final = squares**0.5
print(final)






