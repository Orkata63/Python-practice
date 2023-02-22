#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    M=int(input())
    mstr = list(map(int,input().split(" ")))
    N=int(input())
    nstr = list(map(int,input().split(" ")))
    nSet = set(nstr)
    mSet = set(mstr)
    newSet = nSet.symmetric_difference(mSet)
    for x in sorted(newSet):
        print(x)

