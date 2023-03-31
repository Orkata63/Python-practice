#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(float,input().split())))
    arr = np.array(arr)
    print(round(np.linalg.det(arr),2))