#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n ----> length of array
#  2. INTEGER k ----> the divisible amount
#  3. INTEGER_ARRAY ar ----> the numbers
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    return len(set((x, y) for x in range(n) for y in range(x+1, n) if (((ar[x] + ar[y]) % k == 0))))
"""total = set()
    for x in range(n):
        for y in range(x+1,n):
            if ((ar[x]+ar[y]) % k == 0):
                total.add((x,y))
    return len(total)"""





if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
