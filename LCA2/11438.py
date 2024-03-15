import sys
from collections import deque
sys.setrecursionlimit(200000)
sys.stdin = open("input.txt", "r")

def ancestors_log():
    for k in range(1,max):
        for n in range(1,N+1):
            ancestors[k][n] = ancestors[k-1][ancestors[k-1][n]]

def bfs(parent):
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        visited[node] = 1
        for i in trees[node]:
            if visited[i]:
                continue
            q.append(i)
            ancestors[0][i] = node
            depth[i] = depth[node] + 1


def LCA2(a,b):
    if depth[a] < depth[b]:
        a,b = b,a

    for i in range(max-1,-1,-1):
        if depth[a] - depth[b] >= (1<<i):
            a= ancestors[i][a]

    if a == b:
        return a
    for k in range(max-1,-1,-1):
        if ancestors[k][a] != ancestors[k][b]:
            a = ancestors[k][a]
            b = ancestors[k][b]
        if k == 0:
            return ancestors[0][a]


N = int(sys.stdin.readline()) 
max = 21
trees = [[] for _ in range(N+1)]
depth = [0] * (N+1)
visited= [0 for _ in range(N+1)]
ancestors = [[0]*(N+1) for _ in range(max)]
for _ in range(N-1):
    i, j = map(int, sys.stdin.readline().split())
    trees[i].append(j)
    trees[j].append(i)
M = int(sys.stdin.readline())

bfs(1)
ancestors_log()
# print(ancestors)
# print(depth)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    result = LCA2(i,j)
    print(result)