import sys
from collections import deque
def bfs():
    q = deque([])
    q.append([N,0])
    while q:
        current, cnt = q.popleft()
        if current == K:
            return cnt

        if 0 <= current-1 <= 100000 and current-1 not in visited:
            visited.add(current-1)
            q.append([current-1, cnt+1])
        if 0 <= current+1 <= 100000 and current+1 not in visited:
            visited.add(current+1)
            q.append([current+1, cnt+1])
        if 0 <= current*2 <= 100000 and current*2 not in visited:
            visited.add(current*2)
            q.append([current*2, cnt+1])
    
N, K = map(int,sys.stdin.readline().split())
visited = set()
visited.add(N)
result = bfs()
print(result)