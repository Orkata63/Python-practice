#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true

if __name__ == "__main__":
    first = int(input())
    firstG = set(map(int, input().split()))
    second = int(input())
    secondG = set(map(int, input().split()))
    print(len(firstG.intersection(secondG))) #used code from problem46