#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minP , maxP = scores[0], scores[0]
    minMaxArr = [ 0, 0 ]
    for x in range(1, len(scores)):
        if scores[x] < minP:
            minP = scores[x]
            minMaxArr[1] += 1
        if scores[x] > maxP:
            maxP = scores[x]
            minMaxArr[0] += 1
    return minMaxArr
    #find this solution being clearer for reading purposes so wont attemp to make a one liner 

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
