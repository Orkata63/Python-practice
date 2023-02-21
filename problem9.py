#problem @https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
realarr = []
highestnumber=-101
for a in arr:
        if a not in realarr:
            realarr.append(a)
        if highestnumber < a:
            highestnumber = a
realarr.sort()
realarr.remove(highestnumber)
if len(realarr)>0:
    print(realarr[-1])
else:
    print(0)

