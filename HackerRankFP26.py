#https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i --->start
#  2. INTEGER j ---> end
#  3. INTEGER k ---> division
#

def beautifulDays(i, j, k):
    # Write your code here
    return sum(1 if abs(x - int(str(x)[::-1])) % k == 0 else 0 for x in range(i,j+1))

if __name__ == '__main__':
    fptr = sys.stdout   #open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
