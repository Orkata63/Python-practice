#https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    timeG = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return timeG.strftime("%H:%M:%S")
    #https://docs.python.org/3/library/datetime.html Format codes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
