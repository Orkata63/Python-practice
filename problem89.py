#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr1 = []
    arr2 = []
    N = int(input())
    for x in range(2*N):
        if x < N:
            arr1.append(list(map(int,input().split())))
        else:
            arr2.append(list(map(int,input().split())))
    print(np.dot(arr1,arr2))