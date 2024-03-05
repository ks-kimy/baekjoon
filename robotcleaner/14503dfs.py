import sys
sys.stdin = open("input.txt", "r")


def rotation(r):
    if r == 0:
        return 3
    if r == 1:
        return 0
    if r == 2:
        return 1
    if r == 3:
        return 2

def moving_2(r,c,d):
    if d == 0: # 2번째 솔루션  북쪽 위를 바라볼 때.
        return r+1, c, d
    if d == 1:    
        return r, c-1, d
    if d == 2:
        return r-1, c , d
    if d == 3:
        return r, c+1, d
def moving_3(r,c,d): # 3번째 솔루션
    if d == 0 :
        return r-1, c
    if d == 1 :
        return r, c+1
    if d == 2 :
        return r+1, c
    if d == 3 :
        return r, c-1



def dfs(r,c,d):
    if matrix[r][c] == 0:
        matrix[r][c] = 2
    method = 2
    for drow, dcol in direction:
        nrow = r + drow
        ncol = c + dcol 
        if matrix[nrow][ncol] == 0:
            method = 3
    if method == 2: # 현 좌표로부터 네 방향에서 모두 청소가 되어 있을 때 
        nrow, ncol, narrow = moving_2(r,c, d)
        if matrix[nrow][ncol] == 1: # 만약에 벽이라면 bfs 정지. 즉 로봇 정지
            return
        else:
            dfs(nrow,ncol,narrow) # 만약 벽이 아니라면 q 로 이동
            return
    if method == 3: # 현 좌표로부터 네 방향에서 청소되지 않은 것이 있을 때
        narrow = rotation(d) # arrow 의 방향 반시계 90도로 회전.
        nrow, ncol = moving_3(r,c,narrow)
        if matrix[nrow][ncol] == 0:
            dfs(nrow,ncol,narrow)
            return
        else:
            dfs(r,c,narrow)
            return


N,M =map(int, input().split())
r,c,d = map(int,input().split()) #d =0 북 , d=1 동 , d=2 남, d=3 서
matrix = [list(map(int,input().split())) for _ in range(N)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]

dfs(r,c,d)
cleans = 0

for row_arr in matrix:
    
    cleans += row_arr.count(2)

print(cleans)

