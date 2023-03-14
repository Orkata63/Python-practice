#https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    dateT = datetime.datetime.strptime(str(year),"%Y")
    timeDelta = datetime.timedelta(days=255)
    if year == 1918:
        timeDelta = datetime.timedelta(days=268)
    if year < 1918 and year % 100 == 0:
        timeDelta = datetime.timedelta(days=254)
    returnDate = dateT + timeDelta
    return str(returnDate.strftime("%d.%m.%Y"))
# not the most sophisticated solutions based on trial and error on my part that does meet conditions partly do that datetime doesnt differ julian and gredorian calendars
if __name__ == '__main__':
    fptr = sys.stdout #(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
