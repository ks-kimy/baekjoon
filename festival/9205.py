import sys
from collections import deque
sys.stdin = open("input.txt",'r')

# 상근이는 50m 마다 맥주 쳐마심. 얜 알콜 중독자임 그냥.
def bfs():
    global flag
    q = deque()
    q.append([home_x,home_y])
    while q:
        x, y =  q.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            flag = True
        for convenience_x, convenience_y  in conveniences_pos:
            move_x = abs(convenience_x-x)
            move_y = abs(convenience_y -y)
            if move_x+move_y <= 1000 and (convenience_x,convenience_y) not in visited:
                q.append([convenience_x,convenience_y])
                visited.add((convenience_x,convenience_y))


T= int(sys.stdin.readline())
for tc in range(1,T+1):
    flag = False
    visited = set()
    conveniences = int(sys.stdin.readline())

    home_x, home_y = map(int, sys.stdin.readline().split())

    conveniences_pos = []
    for _ in range(conveniences):
        x,y = map(int, sys.stdin.readline().split())
        conveniences_pos.append([x,y])
    festival_x, festival_y = map(int,sys.stdin.readline().split())
    bfs()
    if flag:
        print('happy')
    else:
        print('sad')
    # print(distances_convenience)
    # print(distance)
    