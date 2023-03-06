#https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
#challenge to do it in 3 lines or less

if __name__ == "__main__":
    N = int(input())
    line = list(map(int, input().split()))
    print(True if all( x > 0 for x in line) and any( str(x)==str(x)[::-1] for x in line) else False)



