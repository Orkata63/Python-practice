#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    #The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
    return(len(word) * max(h[x] if list(string.ascii_lowercase)[x] == y else 0 for x in range(26) for y in word ))

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
