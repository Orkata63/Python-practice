#https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    return int(math.sqrt(b-1)) - int(math.sqrt(a)) + (2 if math.sqrt(a).is_integer() and math.sqrt(b).is_integer() else 1 if math.sqrt(a).is_integer() or math.sqrt(b).is_integer() else 0)
    #itterative solution
    #return sum(1 if math.sqrt(x).is_integer() else 0 for x in range(a,b+1))

"""
2
3 9
17 24
"""
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
