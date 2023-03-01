#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import combinations_with_replacement

if __name__ == "__main__":
    word, maxC = input().split()
    [print("".join(x)) for x in combinations_with_replacement(sorted(word), int(maxC))]