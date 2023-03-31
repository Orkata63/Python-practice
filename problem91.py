#https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    print(np.polyval(list(map(float,input().split())),int(input()) ))