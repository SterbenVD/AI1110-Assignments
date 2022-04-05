import matplotlib.pyplot as plt
import numpy as np

# Assigning the points
A = np.array([-1, 3])
B = np.array([4, 2])
C = np.array([3, -2])
O = np.array([0,0])

def line_gen(type_of_line,*points):
    arr_x = [p[0] for p in points]
    arr_y = [p[1] for p in points]
    if type_of_line == "points":
        plt.plot(arr_x,arr_y,'o')
    elif type_of_line == "lines":
        plt.plot(arr_x,arr_y,marker = 'o')

def centroid(*points):
    arr_x = [p[0] for p in points]
    arr_y = [p[1] for p in points]
    num_points = len(points)
    centroid_x = sum(arr_x)/num_points
    centroid_y = sum(arr_y)/num_points
    return [centroid_x, centroid_y]

def line_slope(p1,p2):
    diff_points = p2 - p1
    slope = diff_points[1] / diff_points[0]
    return slope

# Finding centroid
G = np.array(centroid(A,B,C))

# Draw the triangle and centroid,origin
line_gen("lines",A,B,C,A)
line_gen("points",G,O)

# Draw Line parallel to AC through G
m = line_slope(A,C)
plt.axline(G , slope = m, c = "#008000")

# Labelling on graph
plt.title("Fig 9.2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.annotate("A",A,xytext=(0,5),textcoords="offset points")
plt.annotate("B",B,xytext=(0,5),textcoords="offset points")
plt.annotate("C",C,xytext=(0,5),textcoords="offset points")
plt.annotate("G",G,xytext=(0,5),textcoords="offset points")
plt.annotate("O",O,xytext=(0,5),textcoords="offset points")
plt.grid()

plt.savefig("../figs/9.2.png")
plt.show()
