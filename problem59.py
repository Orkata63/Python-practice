#https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true


if __name__ == "__main__":
    N, X = map(int, input().split())
    marks = []
    for x in range(X):
        marks.append(list(map(float, input().split())))
    [print(sum(n)/X) for n in list(zip(*marks))]
