#Assignment 1
#soln 5
import math
#create a for loop
for i in range(0, 346, 15):
    #then print the sine and cosine of the angles
     print(i, ' ', round(math.sin(math.radians(i)), 4),round(math.cos(math.radians(i)),4))
