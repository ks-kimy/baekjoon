import sys
sys.stdin = open("input.txt", "r")
def dfs(v):
    global result
    visited[v] = 1
    # print(v)
    for w in computers[v]:
        if not visited[w]:
            result +=1
            dfs(w)


N = int(input())
M = int(input())
computers= [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    computers[i].append(j)
    computers[j].append(i)
result = 0
# print(computers)

dfs(1)
print(result)