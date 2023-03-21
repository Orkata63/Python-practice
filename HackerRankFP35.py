#https://www.hackerrank.com/challenges/append-and-delete/problem?isFullScreen=true


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    counter = 0
    i = 0
    word = ""
    while 1<2:
        try:
            if s[i] == t[i]:
                word += s[i]
                i += 1
                continue
            else:
                counter += len(t) - i + len(s) - i
                break
        except IndexError:
            counter += abs(len(t) - len(s))
            break
    # in case we have 0 matches and we have more moves than delete all + add all since we can delete "empty" words
    if word == '':
        return "Yes" if len(s) + len(t) < k or counter == k else "No"
    # in case we have a matching word where we just add and delete until we get to k
    if counter == 0:
        return "Yes" if len(s) + len(t) < k or k%2 == 0 else "No"
    # if we over exceed the allowed number of moves
    if counter > k:
        return "No"
    # if we have a short word that we can delete till we get exact number of remaining moves to make the word
    if len(word) <= (k - counter)/2:
        return "Yes"
    # cases were were below the counter and we have the word we do the same as the if counter == 0, have it separately for clarity
    return "Yes" if (counter % 2 == 0 and k % 2 == 0) or (counter % 2 == 1 and k % 2 == 1) else "No"
#test were rigorous so ended up maaking changes to pass them

"""
            if len(s) > len(t):
                counter += abs(len(t) - len(s))
            else:
                counter += 2*abs(len(s) - len(t))

"""
"""    counter = 0
    i = 0
    word = ""
    while word != t or word != s:
        if word == t:
            counter+=len(s) - len(t)
            break
        try:
            if s[i] == t[i]:
                word += s[i]
                i+=1
                continue
            else:
                word+=t[i]
                counter+=2
        except IndexError:
            counter+=len(t) - len(s)
            break
        i+=1

    return "Yes" if counter<=k else "No"
"""
# was making this solution if we had control over where we can delete and write

if __name__ == '__main__':
    fptr = sys.stdout #open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
