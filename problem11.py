#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
a=[]
arr=[]
for x in range(N):
    y = input()
    a = y.split(" ")
    if a[0] == "insert":
        arr.insert(int(a[1]),int(a[2]))
    if a[0] == "print":
        print(arr)
    if a[0] == "remove":
        arr.remove(int(a[1]))
    if a[0] == "append":
        arr.append(int(a[1]))
    if a[0] == "sort":
        arr.sort()
    if a[0] == "pop":
        arr.pop(-1)
    if a[0] == "reverse":
        arr.reverse()

