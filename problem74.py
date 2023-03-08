#https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.              Format of input: Day dd Mon yyyy hh:mm:ss +xxxx
def time_delta(t1, t2):
    date1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z") #https://docs.python.org/3/library/datetime.html
    date2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs((date2 - date1)).total_seconds()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

       # fptr.write(delta + '\n')

    fptr.close()