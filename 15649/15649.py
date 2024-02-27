
def permutation(level):
    if level >= M:
        print(*result)
        # arr_list.append(result) # 이렇게 하면 얕은 복사가 되어 40번째 줄의 0으로의 값 변경으로 인해 0으로 변한다.
        # arr_list.append(result.copy) # 이것도 얕은 복사지만 iterable 내의 iterable 만 얕은 복사가 되는 구조이므로 리스트의 값 변경은
        # 일어나지 않는다.
        return

    for i in range(N):
        if visited[i] : continue
        visited[i] = 1
        result[level] = arr[i]
        permutation(level+1)
        result[level] = 0
        visited[i] = 0

N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
visited = [0] * N
result =[0] * M
permutation(0)