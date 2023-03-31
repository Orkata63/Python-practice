#https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr1 = np.array(list(map(int, input().split())))
    arr2 = np.array(list(map(int, input().split())))
    print(np.inner(arr1,arr2), np.outer(arr1,arr2), sep="\n")