import sys
from collections import deque
from copy import deepcopy
sys.stdin = open("input.txt", "r")

def overtwice():
    while q:
        r, c = q.popleft()
        for drow, dcol in direction:
            nrow = r + drow
            ncol = c + dcol
            if 0 <= nrow < rows and 0 <= ncol < cols and not matrix[nrow][ncol] == 0 and not visited[nrow][ncol]:
                q.append([nrow,ncol])
                visited[nrow][ncol] = memo

def melting(row,col):
    cnt = 0 
    for drow, dcol in direction:
        nrow = row + drow
        ncol = col + dcol
        if 0 <= nrow < rows and 0 <= ncol < cols and copy_matrix[nrow][ncol] == 0:
            cnt += 1
    return cnt


rows, cols = map(int,sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(rows)]    
time = 0
direction = [[1,0],[-1,0],[0,1],[0,-1]]

while True:
    visited = [[0]*cols for _ in range(rows)]
    q = deque([])
    memo = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] and not visited[row][col]:
                memo += 1
                q.append([row,col])
                visited[row][col] = memo
                overtwice()
            elif  not matrix[row][col] or visited[row][col]:
                continue

    if max(map(max,visited)) >= 2:
        break

    elif max(map(max,visited)) == 0:
        time = 0
        break
    
    copy_matrix = deepcopy(matrix)
    for row in range(rows):
        for col in range(cols):
            if copy_matrix[row][col]:
                cnt = melting(row,col)
                matrix[row][col] -= cnt
                if matrix[row][col] < 0:
                    matrix[row][col] = 0 
    time += 1
print(time)