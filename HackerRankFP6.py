#https://www.hackerrank.com/challenges/insertion-sort/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""def sort(arr):
    global r
    if len(arr) == 1:
        return arr

    middle = int(len(arr)/2)
    leftSide = arr[:middle]
    rightSide = arr[middle:]
    i = 0
    j = 0
    newArr = ()
    while i < len(leftSide) and j < len(rightSide):
        valueL = leftSide[i]
        valueR = rightSide[j]
        if valueL > valueR:
            leftSide[i] = valueR
            rightSide[j] = valueL
            r+=(middle - i)
            j+=1
            if i < middle:
                i+=1
                j+=1
            else:
                j+=1

        thisArr = leftSide+rightSide
        if thisArr == sorted(arr):
            return arr
        if len(leftSide) > 1:
            sort(leftSide)
        if len(rightSide) > 1:
            sort(rightSide)
break
"""



def insertionSort(arr):
    # Write your code here


    returnSum = 0
    if arr == sorted(arr):
        return returnSum
    else:
        for x in range(len(arr)-1):
            for y in range(x+1,len(arr)):
                if arr[x] > arr[y]:
                    returnSum+=1
    return returnSum

"""
    global r
    r = 0
    if arr == sorted(arr):
        return r
    else:
        sort(arr)
        return r
        
"""

#O(n**2) doesnt pass tests will look at the problem again
if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    r = 0

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


"""
def sort(arr):
    global r
    if len(arr) == 1:
        return arr

    middle = int(len(arr)/2)
    leftSide = arr[:middle]
    rightSide = arr[middle:]
    i = j = k = 0
    kArr = []
    newArr = sort(leftSide)+sort(rightSide)
    while i < len(leftSide) and j < len(rightSide):
        if leftSide[i] <= rightSide[j]:
            kArr[k] = leftSide[i]
            i += 1
        else:
            kArr[k] = rightSide[j]
            j += 1
        k += 1

    return kArr
    """