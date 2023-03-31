#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true

import numpy as np


if __name__ == "__main__":
    np.set_printoptions(legacy="1.13")
    arr = np.array(list(map(float, input().split())))
    print(np.floor(arr), np.ceil(arr), np.rint(arr), sep="\n")