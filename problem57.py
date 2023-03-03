#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true


if __name__ == "__main__":
    A = set(map(int, input().split()))
    N = int(input())
    Check = list()
    for _ in range(N):
        B = set(map(int, input().split()))
        Check.append(True) if A.issuperset(B) else Check.append(False)
    print(True if all(Check) == True else False)