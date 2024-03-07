import sys
sys.stdin = open("input.txt", "r")
def rotation_matrix(r,c,s):
    start_row = r-s-1
    start_col = c-s-1
    end_row = r+s-1
    end_col = r+s-1
    




# 행렬에서 최솟값 반환
def min_in_matrix():
    min_result = 100000
    for arr in matrix:
        temp = sum(arr)
        if min_result > temp:
            min_result = temp
    
    return temp


N,M,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]

result = min_in_matrix()
print(result)