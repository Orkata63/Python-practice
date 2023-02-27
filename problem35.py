#https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

import itertools


if __name__ == "__main__":
    permStr,  N = map(str, input().split(" "))
    [print ("".join(x)) for x in sorted(list(itertools.permutations(permStr, int(N))))]
