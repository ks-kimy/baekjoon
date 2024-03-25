import sys


def dfs(row, col, cnt):
    global result

    result = max(result, cnt)
    history[ord(matrix[row][col])-65] = 1

    for d in direction:
        nrow = row + d[0]
        ncol = col + d[1]
        if 0 <= nrow < R and 0 <= ncol < C  and not history[ord(matrix[nrow][ncol])-65]:
            dfs(nrow,ncol,cnt+1)
            history[ord(matrix[nrow][ncol])-65] = 0
            
          

R, C = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline()) for _ in range(R)]
history = [0] * 26
history[(ord(matrix[0][0])-65)] = 1
result = 0
direction = [[1,0],[-1,0],[0,1],[0,-1]]
dfs(0,0,1)
print(result)