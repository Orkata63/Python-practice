#https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
import itertools

if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*list(itertools.product(A,B)))
