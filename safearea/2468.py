import sys
from collections import deque
sys.stdin = open("input.txt","r")

def bfs():
   while q:
        row, col = q.popleft()
        for drow, dcol in direction:
           nrow = row + drow
           ncol = col + dcol
           if 0 <= nrow < N and 0 <= ncol < N and not visited[nrow][ncol] and \
            areas[nrow][ncol] > height:
                q.append([nrow, ncol])
                visited[nrow][ncol] = cnt


N = int(sys.stdin.readline())
areas = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
height = 1
result = 0
while height <= 100:
    q = deque([])
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if areas[row][col] > height and visited[row][col] == 0:
                cnt += 1
                visited[row][col] = cnt
                q.append([row,col])
                bfs()
    height += 1
    if result < cnt:
        result = cnt
    if result == 0:
        result = 1


    if cnt == 0:
        break
print(result)
