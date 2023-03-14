#https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n ---> starting page
#  2. INTEGER p ---> end page
#

def pageCount(n, p):
    # Write your code here
    return min([int(abs(n-p)/2)+1 if n%2==0 and n-p==1 else int(abs(n-p)/2), int(p/2)]) #makes a 2 element list 1st element is from page n to page p other is from start to p page
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
