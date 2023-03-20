#https://www.hackerrank.com/challenges/save-the-prisoner/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n --->  the number of prisoners
#  2. INTEGER m --->  the number of sweets
#  3. INTEGER s ---> the chair number to begin passing out sweets from
#

def saveThePrisoner(n, m, s):
    # Write your code here
    return n if (s+m) % n - 1 == 0 or (n - abs((s+m) % n - 1)) == 0  else (s+m) % n - 1 if  (s+m) % n - 1 >  0 else n - abs((s+m) % n - 1)
# the chairs are seated in a circle so we have 1,2,3,4,1,2,3,4 and so on, not the best logic in the solution but gets the job done

"""
2
7 19 2
3 7 3
"""
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
