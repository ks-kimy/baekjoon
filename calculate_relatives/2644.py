import sys
from collections import deque
sys.stdin = open("input.txt", "r")
def bfs(start, end):
    cnt = 0
    q = deque([])
    q.append([start,cnt])
    while q:
        node, num = q.popleft()
        if node == end:
            return num
        for connect in relatives[node]:
            if visited[connect] == 0:
                visited[connect] = 1
                q.append([connect,num+1])
    else:
        return -1

N = int(input())
x, y = map(int, input().split())
M = int(input())
relatives = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    i, j = map(int,input().split())
    relatives[i].append(j)
    relatives[j].append(i)
result = bfs(x,y)
print(result)