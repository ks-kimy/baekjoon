import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def bfs(row, col):
    cnt = 1
    q = deque([])
    q.append([row,col,cnt])
    visited_matrix[row][col] = 1
    while q:

        vrow, vcol,vcnt = q.popleft()
        if vrow == N-1 and vcol == M-1 :
            result.append(vcnt)

        for drow,dcol in division:
            nrow = vrow + drow
            ncol = vcol + dcol
            ncnt = vcnt + 1
            if 0 <= nrow < N and 0 <= ncol < M and visited_matrix[nrow][ncol] == 0\
            and matrix[nrow][ncol] == 1:
                
                
                q.append([nrow,ncol,ncnt])
                visited_matrix[nrow][ncol] = 1

    



N, M = map(int,input().split())
matrix = [list(map(int, input())) for _ in range(N)]
# print(matrix)
division = [[1,0],[-1,0],[0,1], [0,-1]]
visited_matrix = [[0]* M for _ in range(N)]
# print(visited_matrix)
result =[]
bfs(0,0)
print(*result)
