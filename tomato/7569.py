import sys
from collections import deque
sys.stdin = open("input.txt","r")
       

def bfs():
    while q:
        floor, row, col = q.popleft()
        for dfloor, drow, dcol in direction:
            nfloor = floor + dfloor
            nrow = row + drow
            ncol = col + dcol
            if 0 <= nfloor < H and 0 <= nrow < N and 0 <= ncol < M:
                if matrix[nfloor][nrow][ncol] == 0:
                    matrix[nfloor][nrow][ncol] = matrix[floor][row][col] + 1
                    q.append([nfloor,nrow,ncol])

M,N,H = map(int,input().split())
matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
# print(matrix[0][0][1]) # [1][2][3]  1번은 높이에 해당되는, 2는 세로에 해당되는 3 은 가로에 해당.
# print(matrix)
direction = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
q = deque()

for floor in range(H):
    for row in range(N):
        for col in range(M):
            if matrix[floor][row][col] == 1:
                q.append([floor,row,col])
    

bfs()
possibility = True
day =  0
for floor in range(H):
    for row in range(N):
        for col in range(M):
            if matrix[floor][row][col] == 0:
                possibility = False
            day = max(day, matrix[floor][row][col])    
if not possibility:
    print(-1)
else:
    print(day-1)
