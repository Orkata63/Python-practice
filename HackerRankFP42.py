#https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0]) # number of rows , columns
    newMatrix = [[0] * n for _ in range(m)]
    # We make an array that will have the outer and inner lines of text that we shift by ,Decides the number of arrays needed by dividing the smaller number between M x N of the matrix
    for x in range(int(min(m,n)/2)):
        thisLayerValues = []
        for row in range(x, m - x - 1):
            thisLayerValues.append((row, x))
        for col in range(x, n - x - 1):
            thisLayerValues.append((m - x - 1, col))
        for row in range(m - x - 1, x, -1):
            thisLayerValues.append((row, n - x - 1))
        for col in range(n - x - 1, x, -1):
            thisLayerValues.append((x, col))
        # we rotate the layers by the r%len(arr) so not to go out of index
        rotatedLayer = thisLayerValues[-(r%len(thisLayerValues)):] + thisLayerValues[:-(r%len(thisLayerValues))]
        # changes the 0s in the new Matrix to the Values that are on the rotated layer
        for i in range(len(thisLayerValues)):
            newMatrix[thisLayerValues[i][0]][thisLayerValues[i][1]] = matrix[rotatedLayer[i][0]][rotatedLayer[i][1]]

    #the return Matrix
    for row in newMatrix:
        print(" ".join(str(x) for x in row))

"""
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
"""

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
