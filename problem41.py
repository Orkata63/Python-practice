#https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true

from itertools import combinations

if __name__ == "__main__":
    word, maxC = input().split()
    for y in range(1,int(maxC)+1):
        [print("".join(x)) for x in combinations(sorted(word), y)]