#problem from https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
xlist = list(range(x+1))
ylist = list(range(y+1))
zlist = list(range(z+1))
fullList = []
for a in xlist:
    for b in ylist:
        for c in zlist:
            if (a+b+c) != n:
                fullList.append([a,b,c])
print(fullList)


"""pa = []  # list with max values
for a in range(x+1):
    for b in  range(y+1):
        for c in range (z+1):
            pa.append([a,b,c])
output=""
for t in range(len(pa)):
    if (pa[t][0]+pa[t][1]+pa[t][2]) != n and t!=len(pa)-1:
        output=output+str(pa[t])+", "
    if t==len(pa)-1:
        output=output+str(pa[t])
print("["+ output + "]")"""
# this got 1 fail on tests
# now with learning lists


