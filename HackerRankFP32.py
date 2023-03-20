#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
#   c ---> path
#   k ---> jump size
def jumpingOnClouds(c, k):
    energy = 100
    currentL = k
    while currentL != 0:
        if currentL>=len(c):
            currentL-=len(c)
        if c[currentL] == 1:
            energy-=3
        else:
            energy-=1
        if currentL == 0:
            break
        currentL+=k
    return energy
    #return 100 - sum(1 if c[(x*k)%len(c)] != 1 else 3 for x in range(0,len(c)))
#we jump until we get to the starting cloud, dont lose energy if we start on a thunder
# tried a one liner but too confusing for this problem 


"""
10 3
1 1 1 0 1 1 0 0 0 0
"""

"""
8 2
0 0 1 0 0 1 1 0
"""
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
