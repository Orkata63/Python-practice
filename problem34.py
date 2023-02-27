#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

import collections

if __name__ == "__main__":
    X = int(input())
    Shoes = collections.Counter(list(map(str, input().split(" "))))
    N = int(input())
    Earned = 0
    for x in range(N):
        newInput = list(map(int, input().split()))
        if str(newInput[0]) in Shoes and Shoes[str(newInput[0])] > 0:
            Shoes.subtract({ str(newInput[0]): 1 })
            Earned +=newInput[1]

    print(Earned)


