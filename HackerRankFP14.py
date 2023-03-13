#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def migratoryBirds(arr):
    # Write your code here
    return Counter(sorted(arr)).most_common(1)[0][0]
#return (sorted(Counter(arr).most_common(1)[0]))[0]


if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
