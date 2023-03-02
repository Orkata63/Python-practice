#https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == "__main__":
    first = int(input())
    firstG = set(map(int, input().split()))
    second = int(input())
    secondG = set(map(int, input().split()))
    print(len(firstG.union(secondG)))
