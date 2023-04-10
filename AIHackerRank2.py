#https://www.hackerrank.com/challenges/saveprincess2?isFullScreen=true
def nextMove(n,r,c,grid):
    for x in range(0, n):
        for y in range(0, n):
            if grid[x][y] == "p":
                princessPos = (x, y)
    if  c - princessPos[1] >= 1:
        return "LEFT"
    if c - princessPos[1] <= -1:
        return "RIGHT"
    if r - princessPos[0] >= 1:
        return "UP"
    if r - princessPos[0] <= -1:
        return "DOWN"




n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))