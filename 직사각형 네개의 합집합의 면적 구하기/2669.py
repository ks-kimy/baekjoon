import sys
sys.stdin = open("input.txt", "r")  
sum_area = 0
coordinate = [] #좌표
matrix =[[0]*100 for _ in range(100)]
for _ in range(4):
    x1, y1, x2,y2 = map(int, input().split())
    for col in range(y1,y2):
        for row in range(x1,x2):
            matrix[row][col] = 1

for arr in matrix:
    sum_area += arr.count(1)

print(sum_area)