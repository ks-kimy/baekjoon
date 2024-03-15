import sys
from itertools import permutations
from copy import deepcopy
sys.stdin = open("input.txt", "r")

def rot_recur(row,col,length):
    if length == 1:
        return
    
    while True:
        
        rotation_matrix(row,col,length)
        row += 1
        col += 1
        length -= 2
        if length == 1:
            return

def rotation_matrix(row,col,length): # r은 행에 대한  c 는 열에 대한 s는 기준

    temp = copy_matrix[row][col]
    
    for i in range(1,length):
        nrow = row
        ncol = col +1
        temp2 = copy_matrix[nrow][ncol]
        copy_matrix[nrow][ncol] = temp
        temp = temp2
        row = nrow
        col = ncol 
    for i in range(1,length):
        nrow = row + 1
        ncol = col 
        temp2 = copy_matrix[nrow][ncol]
        copy_matrix[nrow][ncol] = temp
        temp = temp2
        row = nrow
        col = ncol 
    for i in range(1,length):
        nrow = row
        ncol = col -1
        temp2 = copy_matrix[nrow][ncol]
        copy_matrix[nrow][ncol] = temp
        temp = temp2
        row = nrow
        col = ncol 
    for i in range(1,length):
        nrow = row -1
        ncol = col 
        temp2 = copy_matrix[nrow][ncol]
        copy_matrix[nrow][ncol] = temp
        temp = temp2
        row = nrow
        col = ncol 
    


# 행렬에서 최솟값 반환
def min_in_matrix():
    min_result = 100000
    for arr in copy_matrix:
        temp = sum(arr)
    
        if min_result > temp:
            min_result = temp
    
    return min_result


N,M,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
rotation_arr = [list(map(int,input().split())) for _ in range(K)]
result = 10000000
for case in permutations(rotation_arr,K):
    copy_matrix = deepcopy(matrix)
    for r,c,s in case:
        start_row = r-s-1
        start_col = c-s-1
        end_row = r+s-1
        end_col = r+s-1
        middle_row = start_row + s
        middle_col = start_col + s
        length = end_row-start_row+1
        rot_recur(start_row,start_col,length)
        temp =  min_in_matrix()
    if result > temp:
        result = temp
print(result)
