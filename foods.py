'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
def food_num(row,col):
    nrow = row
    ncol = col
    global cntㄹㄹ
    
    for drow, dcol in direction:
        nrow = row + drow12bb
        ncol = col + dcol
        if [nrow,ncol] in arr and matrix[nrow][ncol] == 0:
            cnt += 1
            matrix[nrow][ncol] = 1
            food_num(nrow,ncol)
        



N, M, K = map(int, input().split())
arr = []    
for _ in range(K):
    i,j = map(int, input().split())
    arr.append([i-1,j-1])
# print(arr)
cnt_arr = []
direction = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(K):
    cnt = 0 
    matrix = [[0]* M for _ in range(N)] 
    food_num(arr[i][0],arr[i][0])
    cnt_arr.append(cnt)
result = max(cnt_arr)
print(result)