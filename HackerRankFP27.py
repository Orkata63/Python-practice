#https://www.hackerrank.com/challenges/strange-advertising/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    likes = 2
    cumulative = 2
    for i in range(2, n + 1):
        shared = likes * 3
        likes = math.floor(shared / 2)
        cumulative += likes
    return cumulative
    #return 2 if n == 1 else math.floor((viralAdvertising(n-1)*3)/2) only works for current likes, in interest of not changing the method but easily fixed with viralAdvertising(n, total)


if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
