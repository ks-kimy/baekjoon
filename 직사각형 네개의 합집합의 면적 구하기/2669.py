import sys
sys.stdin = open("input.txt", "r")  
sum_area = 0
coordinate = [] #좌표
for _ in range(4):
    x1, y1, x2,y2 = map(int, input().split())

    coordinate.append([[x1,y1],[x2,y2]])


for p1, p2 in coordinate: #p1 은 왼쪽 아래 점에 대한 정보, p2 는 오른쪽 위 점에 대한 정보.
    pass


asd =  [[[2,3],[3,4]],[[[2,3],[3,4]]]]
print(set(asd))