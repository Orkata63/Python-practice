#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    returnS = ''
    for x in s.split(" "):
        returnS = returnS + str(x).capitalize()+" "
    return returnS
    #return ' '.join([word.capitalize() for word in s.split()]) as  1 liner
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
