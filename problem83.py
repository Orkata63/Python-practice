#https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    np.set_printoptions(legacy='1.13') # for correct print provided in notes
    N,M = list(map(int,input().split()))
    print(np.eye( N,M, 0))