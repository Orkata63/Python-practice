#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr = []
    for _ in range(list(map(int,input().split()))[0]):
        arr.append(list(map(int,input().split())))
    arr = np.array(arr)
    print(np.product(np.sum(arr, axis=0)))