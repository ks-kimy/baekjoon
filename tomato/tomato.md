# DFS 와 BFS 에 대한 선택
이 문제를 DFS 로 풀 경우에는 며칠이 걸려야 다 익는 지에 대한 day 수 계산이 매우 어려워 진다. 

이 문제를 통해 DFS와 BFS 중 어떤 알고리즘을 선택해야 쉽게 풀리는 지 고민해 볼 수 있는 기회가 되었다.

```python 
import sys
from collections import deque
sys.stdin = open("input.txt","r")
       

def bfs():
    while q:
        floor, row, col = q.popleft()
        for dfloor, drow, dcol in direction:
            nfloor = floor + dfloor
            nrow = row + drow
            ncol = col + dcol
            if 0 <= nfloor < H and 0 <= nrow < N and 0 <= ncol < M:
                if matrix[nfloor][nrow][ncol] == 0:
                    matrix[nfloor][nrow][ncol] = matrix[floor][row][col] + 1
                    q.append([nfloor,nrow,ncol])

M,N,H = map(int,input().split())
matrix = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
# print(matrix[0][0][1]) # [1][2][3]  1번은 높이에 해당되는, 2는 세로에 해당되는 3 은 가로에 해당.
# print(matrix)
direction = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
q = deque()

for floor in range(H):
    for row in range(N):
        for col in range(M):
            if matrix[floor][row][col] == 1:
                q.append([floor,row,col])
    

bfs()
possibility = True
day =  0
for floor in range(H):
    for row in range(N):
        for col in range(M):
            if matrix[floor][row][col] == 0:
                possibility = False
            day = max(day, matrix[floor][row][col])    
if not possibility:
    print(-1)
else:
    print(day-1)
```
이 코드를 보면 tabulation 기법이 사용되었다. 

## DP
1.`Tabulation`
도표 작성 , 표, 목록

상향식 접근 방식.

ex) 
```python
#fibonacci

def fibonacci(n):

  table = [0,1] 

  for i in range(2, n+1):
    table.append(table[i-1] + table[i-2])

  return table[n]
```
이와 같이 상향식 접근이 가능하다.

2.`Memoization`
memorization - 기억, 암기
재귀를 이용하여 콜스택을 통해 갑을 위에서부터 아래로 계산하기 때문에 하향식 접근을 하는 방식입니다. 

ex)
```python
# fibonacci
def fibonacci(n,memo):
  if n < 3:
    memo[n] = 1
    return memo[n] 
  
  if memo[n]:
    return memo[n]

  memo[n] = fibonacci(n-1,memo) + fibonacci(n-2,memo)

  return memo[n]


```
다음과 같이 n 이 1, 2 가 될 때까지 위에서부터 아래로 내려오는 방식. 하나의 배열에 각 n 번째에 해당하는 정보들을 기록해두어 불필요한 메모리를 줄일 수 있는 방법이다. 