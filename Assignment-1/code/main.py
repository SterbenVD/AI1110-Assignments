import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def line_gen(bool_line,*points):
    arr_x = [p[0] for p in points]
    arr_y = [p[1] for p in points]
    if bool_line == "points":
        plt.plot(arr_x,arr_y,'o')
    elif bool_line == "lines":
        plt.plot(arr_x,arr_y,marker = 'o')

def centroid(*points):
    arr_x = [p[0] for p in points]
    arr_y = [p[1] for p in points]
    num_points = len(points)
    centroid_x = sum(arr_x)/num_points
    centroid_y = sum(arr_y)/num_points
    return [centroid_x, centroid_y]

def line_slope(p1,p2):
    slope = (p2[1] - p1[1])/(p2[0] - p1[0])
    return slope

A = np.array([-1, 3])
B = np.array([4, 2])
C = np.array([3, -2])

# Finding centroid
G = np.array(centroid(A,B,C))

# Draw the traingle and centroid
line_gen("lines",A,B,C,A)
line_gen("points",G)

# Draw Line parallel to AC through G
plt.axline(G , slope = line_slope(A,C))

# Labelling on graph
plt.title("Fig 9.2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points")
plt.annotate("G",G,xytext=(0,5),textcoords="offset points")
plt.grid()

plt.savefig("../figs/9.2.png")
plt.show()
