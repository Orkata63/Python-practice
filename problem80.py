#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr = []
    for _ in range(list(map(int, input().split()))[0]):
        arr.append(list(map(int, input().split())))
    arr = np.array(arr, int)
    print(arr.transpose())
    print(arr.flatten())

