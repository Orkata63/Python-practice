#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true


if __name__ == "__main__":
    first = int(input())
    firstG = set(map(int, input().split()))
    second = int(input())
    secondG = set(map(int, input().split()))
    print(len(firstG.symmetric_difference(secondG)))
    #solution from 46