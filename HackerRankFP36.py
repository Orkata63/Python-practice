#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true

# predecessor of HackerRankFP32 website doesnt give linear problems


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    jumps = 0
    currentLoc = 0
    while currentLoc-1 != len(c):
# Making an exception in case we go out if index sadly if i check if c[currentLoc+1] first it would be the ineffective jump strength
        try:
            if c[currentLoc+2] == 0:
                currentLoc+=2
                jumps+=1
            elif c[currentLoc+1] == 0:
                currentLoc+=1
                jumps+=1
        except IndexError:
            try:
                if c[currentLoc + 1] == 0:
                    currentLoc += 1
                    jumps += 1
            except IndexError:
                break

    return jumps
# we have a jump distance of 1 or 2

if __name__ == '__main__':
    fptr =sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
