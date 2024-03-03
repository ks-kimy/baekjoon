import sys
sys.stdin = open("input.txt", "r")

def dfs(row, col, cnt):
    global result
    if result <= cnt:
        return

    if row == N-1 and col == M-1:
        if result > cnt:
            result = cnt
        return
    for drow, dcol in division:
        nrow = row + drow
        ncol = col + dcol
        if 0<= nrow < N and 0<= ncol < M:
            if matrix[nrow][ncol] == 1 and visited_matrix[nrow][ncol] == 0:
                cnt +=1
                visited_matrix[row][col] = 1
                dfs(nrow, ncol, cnt)
                cnt -=1
                visited_matrix[row][col] = 0

N, M = map(int,input().split())
matrix = [list(map(int, input())) for _ in range(N)]
# print(matrix)
division = [[1,0],[-1,0],[0,1], [0,-1]]
visited_matrix = [[0]* M for _ in range(N)]
# print(visited_matrix)
result = 1000000
dfs(0,0,1)
print(result)