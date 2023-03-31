#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr = []
    for _ in range(list(map(int, input().split()))[0]):
        arr.append(list(map(int, input().split())))
    arr = np.array(arr)
    print(arr.mean(axis=1), arr.var(axis=0), round(arr.std(axis=None),11), sep="\n")
