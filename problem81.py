#https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true

import numpy as np

if __name__ == "__main__":
    arr1 = []
    arr2 = []
    nmp = list(map(int, input().split()))
    for _ in range(nmp[0]):
        arr1.append(list(map(int,input().split())))
    for _ in range(nmp[1]):
        arr2.append((list(map(int,input().split()))))
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    print(np.concatenate((arr1,arr2),axis=0))
    #axis is 0 representing the number of columns that are the same for these 2 arrays the problem doesnt require it to be automated
    #so in turn im not automating it which is easily checked depending in if colums or rows are same 0 for columns 1 for rows
