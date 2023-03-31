#https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    dimensions = list(map(int, input().split()))
    print(np.zeros(dimensions, dtype=int))
    print(np.ones(dimensions, dtype=int))