#https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
import numpy as np

if __name__ == "__main__":
    arr = np.array(list(map(int, input().split())))
    print(arr.reshape(3,3))