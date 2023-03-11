#https://www.hackerrank.com/challenges/apple-and-orange/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s ---> house start
#  2. INTEGER t ---> house ends
#  3. INTEGER a ---> apple tree
#  4. INTEGER b ---> orange tree
#  5. INTEGER_ARRAY apples ---> where apples fall compared to a
#  6. INTEGER_ARRAY oranges ---> where oranges fall comparedd to b
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    print("".join(str(sum(1 if x in range(s,t+1) else 0 for x in [x+a for x in apples]))))
    print("".join(str((sum(1 if x in range(s,t+1) else 0 for x in [x+b for x in oranges])))))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
