#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true


if __name__ == "__main__":
    first = int(input())
    firstG = set(map(int, input().split()))
    second = int(input())
    secondG = set(map(int, input().split()))
    print(len(firstG.difference(secondG)))
    #solution from 46