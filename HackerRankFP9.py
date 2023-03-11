#https://www.hackerrank.com/challenges/kangaroo/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1 ---> starting position of 1st kangaroo
#  2. INTEGER v1 ---> distance the 1st kangaroo jumps
#  3. INTEGER x2 ---> starting position of 2nd kangaroo
#  4. INTEGER v2 ---> distance the 2nd kangaroo jumps
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    return "YES" if v1>v2 and any((x1+v1*i) == (x2+v2*i) for i in range(10000)) else "NO"
    # ideally script would stop when 1st kangaroo overtakes 2nd kangaroo
"""
for i in range(10000):
    if (x1 + v1 * i) == (x2 + v2 * i):
        return "YES"
    elif (x1 + v1 * i) > (x2 + v2 * i):
        break
return "NO"
"""
#the code below the return would be more effective 
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
