"""
    Exercise 7a: Ohm's law
"""

import numpy as np
from scipy.linalg import lstsq

matrix = [
    [3 ,-1, 0,-1, 0,-1, 0, 0],
    [-1, 3,-1, 0, 0, 0,-1, 0],
    [ 0,-1, 3,-1, 0, 0, 0,-1],
    [-1, 0,-1, 3,-1, 0, 0, 0],
    [ 0, 0, 0,-1, 3,-1, 0,-1],
    [-1, 0, 0, 0,-1, 3,-1, 0],
    [ 0,-1, 0, 0, 0,-1, 3,-1],
    [ 0, 0,-1, 0,-1, 0,-1, 3],
]

R = np.matrix(matrix)
I = np.matrix([1, 0, 0, 0, 0, 0, 0, -1]).T
V = lstsq(R, I)
R_total = (V[0][0]-V[0][7])[0]
print("Total resistance of the cube: {r:0.3f}".format(r=R_total))

R1 = 0.37
matrix[0] = [2+(1/R1),-(1/R1), 0,-1, 0,-1, 0, 0]
matrix[1] = [-(1/R1),2+(1/R1),-1, 0, 0, 0,-1, 0]
R = np.matrix(matrix)
V = lstsq(R, I)
R_total = (V[0][0]-V[0][7])[0]
print("Total resistance of the cube (R1={r1:0.2f}): {r:0.3f}".format(r=R_total, r1=R1))
