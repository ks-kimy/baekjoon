'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''
import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def dfs(v): # v는 시작정점을 의미한다. 
    st = []
    visited_dfs[v] = 1

    answer_dfs.append(v)
    while True:
        for w in stack[v]:
            if visited_dfs[w] == 0:
                st.append(v)
                v = w
                visited_dfs[v] =1
                answer_dfs.append(v)
                break
        else:
            if st:
                v = st.pop()
            else:
                break
def dfs_recursion(v):
    visited_recursion[v] = 1
    answer_dfs.append(v)
    for w in stack[v]:
        if visited_recursion[w] == 0:
            dfs_recursion(w)
    
def bfs(v):
    q =deque([v])
    visited_q[v] =1
    while q:
        v = q.popleft()
        answer_bfs.append(v)
        for i in stack[v]:
            if not visited_q[i]:
                q.append(i)
                visited_q[i] = 1
    

N, M, V = map(int,input().split())

visited_recursion = [0]*(N+1) 
visited_q = [0] * (N+1)
visited_dfs = [0] * (N+1)
answer_bfs = []
answer_dfs = []
stack = [[] for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    stack[i].append(j)
    stack[j].append(i)
for i in range(1,N+1):
    stack[i].sort()
# print(stack)
dfs(V)
bfs(V)
print(*answer_dfs)
print(*answer_bfs)