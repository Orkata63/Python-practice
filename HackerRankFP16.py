#https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill ---> item prices
#  2. INTEGER k ---> what item Anna didn`t eat from 0...n
#  3. INTEGER b ---> Brians bill split suggestion
#

def bonAppetit(bill, k, b):
    # Write your code here
    print("Bon Appetit" if (sum(bill) - bill[k])/2 == b else int(b - (sum(bill) - bill[k])/2))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
