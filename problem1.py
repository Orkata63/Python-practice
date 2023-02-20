#!/bin/python3

import math
import os
import random
import re
import sys
#hackerrank problem https://www.hackerrank.com/challenges/py-if-else/problem


if __name__ == '__main__':
    n = int(input().strip())
if n > 20 and n % 2==0:
    print("Not Weird")
if n in range(2,6) and n % 2==0:
    print("Not Weird")
if n in range(6,21) and n % 2==0:
    print("Weird")
if n % 2 == 1:
    print("Weird")

""" if n is in range (2,6) &&
    print("Not Weird")
else:
    print("Weird") """
