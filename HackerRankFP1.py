#https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#problem is easy with python since we dont need to declare long for 64 bit 

def miniMaxSum(arr):
    # Write your code here
    print(str(sum(arr)-max(arr))+" "+str(sum(arr)-min(arr)))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)