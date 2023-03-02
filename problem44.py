#https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true


if __name__ == "__main__":
    N = int(input())
    stamps = set(str(input()) for _ in range(N))
    print(len(stamps))
