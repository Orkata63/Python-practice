#https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    results = []
    place = 1
    y = 0
    for x in player[::-1]:
        while y < len(ranked):
            if x >= ranked[y]:
                break
            elif ranked[y] == ranked[y-1]:
                y+=1
            else:
                y+=1
                place+=1
        results.append(place)
    return results[::-1]
# O(nlogn) solution 
"""
7
100 100 50 40 40 20 10
4
5 25 50 120
"""


if __name__ == '__main__':
    fptr = sys.stdout         #open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
