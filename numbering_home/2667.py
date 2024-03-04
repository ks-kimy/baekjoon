import sys
sys.stdin = open("input.txt", "r")
def dfs(row,col):
    global result

    if visited[row][col] == 0 and matrix[row][col] == 1:
        visited[row][col] = 1
        result += 1
        for drow, dcol in direction:
            nrow = row + drow
            ncol = col + dcol
            if 0<=nrow<N and 0<=ncol<N and visited[nrow][ncol] == 0 \
                    and matrix[nrow][ncol] == 1:
                dfs(nrow,ncol)



    else:
        return



N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
result_arr = []
for row in range(N):
    for col in range(N):
        result = 0
        dfs(row,col)
        if result != 0:
            result_arr.append(result)
result_arr.sort()
length = len(result_arr)
print(length)
for i in result_arr:
    print(i)