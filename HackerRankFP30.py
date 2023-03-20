#https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a ---> len of array
#  2. INTEGER k ---> number of moves
#  3. INTEGER_ARRAY queries ------> array of index to prove
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    return [(a[len(a) - k % len(a):]+a[:len(a) - k % len(a)])[x] for x in queries]
"""    realMoves = k % len(a)
    leftSide = a[:len(a)-realMoves]
    rightSide = a[len(a)-realMoves:]
    newArr = rightSide+leftSide
    return [newArr[x] for x in queries]"""
# note that if we make changes equal to the array len it remains the same array

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
