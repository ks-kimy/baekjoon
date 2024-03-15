import sys
sys.setrecursionlimit(10000000)
N= int(sys.stdin.readline())
def dfs(start,length):
    global result
    if result < length:
        result = length

    visited[start] = 1
    for root in trees[start]:
        if visited[root[0]]:
            continue
        visited[root[0]] = 1
        dfs(root[0],length+root[1])
        visited[root[0]] = 0


trees = [[] for _ in range(N+1)]
visited = [0] * (N+1)
result = 0
for _ in range(N-1):
    a,b,c = map(int, sys.stdin.readline().split())
    trees[a].append([b,c])
    trees[b].append([a,c])

dfs(1,0)
print(result)