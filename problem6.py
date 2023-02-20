#!/bin/python3

import math
import os
import random
import re
import sys
#problem @https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def is_leap(year):
    leap = False

    # Write your logic here
    if year%400==0:
        leap = True
    if year%100==0 and year%400!=0:
        leap = False
    if year%4==0 and year%100!=0 and year%400!=0:
        leap = True

    return leap


year = int(input())
print(is_leap(year))

