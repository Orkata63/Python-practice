#https://www.hackerrank.com/challenges/saveprincess?isFullScreen=true


def displayPathtoPrincess(n,grid):
#print all the moves here
    for x in range(0, n):
        for y in range(n):
            if grid[x][y] == "m":
                botposition = (x, y)
            if grid[x][y] == "p":
                princessPos = (x, y)
    print("DOWN\n" * (princessPos[0] - botposition[0]), end='')
    print("UP\n" * (botposition[0] - princessPos[0]), end='')
    print("LEFT\n" * (botposition[1] - princessPos[1]), end='')
    print("RIGHT\n" * (princessPos[1] - botposition[1]), end='')

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)