#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    N,M = map(int,input().split())
    arr1 = []
    for _ in range(N):
        arr1.append(list(map(int, input().split())))
    arr1 = np.array(arr1)
    arr2 = []
    for _ in range(N):
        arr2.append(list(map(int, input().split())))
    print(np.add(arr1,arr2),np.subtract(arr1,arr2),np.multiply(arr1,arr2),np.floor_divide(arr1,arr2),np.mod(arr1,arr2),np.power(arr1,arr2), sep="\n")