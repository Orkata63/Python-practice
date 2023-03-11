#https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    return [x if x < 38 or x % 5 <= 2 else x + (5 - x % 5) for x in grades]
"""    returnArr = []
    for x in grades:
        if x < 38:
            returnArr.append(x)
        else:
            if x % 5 <= 2:
                returnArr.append(x)
            elif x % 5 >= 3:
                returnArr.append(x+(5 - (x%5)))
    return returnArr"""



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
