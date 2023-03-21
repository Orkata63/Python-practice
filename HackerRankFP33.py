#https://www.hackerrank.com/challenges/find-digits/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    return sum(0 if int(x) == 0 else 1 if n % int(x) == 0 else 0 for x in str(n))
    # checking if its 0 to not make exception for it then just checks if the digit is divisable or not with return 1 or 0 for True or False
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
