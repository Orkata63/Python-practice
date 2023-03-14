#https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# A valley begins from n >= 0 and ends when n E ( -infinity, 0) gets to 0

def countingValleys(steps, path):
    # Write your code here
    currentAltitude = 0 # since we always start from sea level
    returnInt = 0
    for x in path:
        pastAltitude = currentAltitude
        if x == "D":
            currentAltitude-=1
        elif x == "U":
            currentAltitude+=1
        if pastAltitude==-1 and currentAltitude==0:
            returnInt+=1
    return returnInt
    # dont think a readable one liner is possible for this problem




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
