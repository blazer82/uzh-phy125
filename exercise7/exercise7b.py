"""
    Exercise 7a: XKCD problem
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg


# Size of the grid n x n
n = 4

# Build sparse matrix
R = sparse.lil_matrix((n**2, n**2))

# Fill in connections
for x in range(n):
    for y in range(n):
        if x-1 >= 0:
            R[x*n+y,n*(x-1)+y] -= 1
        if x+1 < n:
            R[x*n+y,n*(x+1)+y] -= 1
        if y-1 >= 0:
            R[x*n+y,n*x+y-1] -= 1
        if y+1 < n:
            R[x*n+y,n*x+y+1] -= 1

# Fill in main diagonal
for i in range(n**2):
    R[i,i] = np.abs(np.sum(R[i]))

# Define current vector
I = np.zeros(n**2)
I[0] = 1
I[-1] = -1

# Calculate
V = linalg.lsqr(R, I)
R_total = (V[0][0]-V[0][-1])

print(R.toarray())

print("\nTotal resistance: {r:0.3f}".format(r=R_total))
