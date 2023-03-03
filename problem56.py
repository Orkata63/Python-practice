#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        sizeA = int(input())
        A = set(map(int, input().split()))
        sizeB = int(input())
        B = set(map(int, input().split()))
        print(True if A.issubset(B) else False)