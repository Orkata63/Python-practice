#https://www.hackerrank.com/challenges/permutation-equation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    return [p.index(p.index(x)+1)+1 for x in range(1,len(p)+1)]
# since we need to find the permutation of the permutation for the values, we double index and we increment for 1 since its natural numbers

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
