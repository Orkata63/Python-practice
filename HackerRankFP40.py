#https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here
    count = 0
    listOfRem = [0]*k
    #print(listOfRem)
    for x in s:
        rem = x % k
        listOfRem[rem]+=1
    #print(listOfRem)
    # we check the pairs that sum up into k, taking only the largest ones
    for i in range(1, math.ceil(k/2)):
        count+=max(listOfRem[i], listOfRem[-i])
    # in case we only have 1 number that is % k by itself meaning any pair with it is safe
    if listOfRem[0]:
        count+=1
    # in case we have an even number of pairs we miss the middle and 1st char so this checks if the middle char is safe
    if k % 2 == 0 and listOfRem[int(k/2)]:
        count+=1
    return count

"""    listOfRem = Counter(x%k for x in s)
    count = 0
    print(listOfRem)
    for i in range(math.ceil(k/2)):
        print(i)
        print(sorted(listOfRem)
        print(listOfRem.values(), listOfRem[-i])
        count+=max(listOfRem[i], listOfRem[-i])
    return count"""
#was trying this approach but say its weak if we have some elements with 0 representation
"""
15 7
278 576 496 727 410 124 338 149 209 702 282 718 771 575 436
"""
"""
4 3
1 7 2 4
"""
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
