#https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s ---> Value of the chocolate squares
#  2. INTEGER d ---> the sum of the squares needs to be d
#  3. INTEGER m ---> the amount of squares we look at
#

def birthday(s, d, m):
    # Write your code here
    return sum(1 if sum(s[x:x+m]) == d  else 0 for x in range(len(s)-m + 1))

"""
6
1 1 1 1 1 1
3 2
"""

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
