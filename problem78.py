#https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true

import numpy as np

def arrays(arr):
    # complete this function
    # use numpy.array
    return np.array(arr, float)[::-1]

if __name__ == "__main__":
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)