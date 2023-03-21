#https://www.hackerrank.com/challenges/extra-long-factorials/problem?isFullScreen=true


# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
# Write your code here
    return(1 if n==1 else n * extraLongFactorials(n-1)) # recursion solution
    #return math.factorial(n) # easy python solution


if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
