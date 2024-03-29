import sys
sys.setrecursionlimit(1000000000)
sys.stdin = open("input.txt","r")
#F = 총 층수, S = 현재 층 G = 스타트링크 장소 층 U = 위로 갈 때 층 D = 아래로 갈 때

def dfs(level,cnt):
    global result
    global flag
    if level in visited:
        return
    if level == G:
        if cnt < result:
            result = cnt
            flag = True
        return
    elif level > F or level < 1:
        return
    
    if level-D <= G:
        visited.add(level)
        dfs(level+U,cnt+1)
    if level+U > G :
        visited.add(level)
        dfs(level-D, cnt+1)

F, S, G, U, D = map(int, sys.stdin.readline().split())
result = 1000000
flag = False
visited = set()
upanddown = [U,D]
dfs(S,0)
if not flag:
    print('use the stairs')
else:
    print(result)