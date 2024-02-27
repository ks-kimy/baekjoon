A = [1,2,3] # 데이터 집합
N = len(A)  # 데이터 갯수
visited = [0] * N   # 데이터의 사용 여부 - 데이터의 index visited[1] -
arr = [0] * N    # 어떤 데이터를 선택했는가 (순열 정보 저장) arr[1] = 2
arr_list = []
def permutation(level):
    if level >= N:
        # print(arr)
        arr_list.append(arr) # 이렇게 하면 얕은 복사가 되어 40번째 줄의 0으로의 값 변경으로 인해 0으로 변한다. 
        arr_list.append(arr.copy) # 이것도 얕은 복사지만 iterable 내의 iterable 만 얕은 복사가 되는 구조이므로 리스트의 값 변경은
        # 일어나지 않는다. 
        return

    for i in range(N):
        if visited[i] : continue
        visited[i] = 1
        arr[level] = A[i]
        permutation(level+1)
        arr[level] = 0
        visited[i] = 0
permutation(0)
print(arr_list)

# 순열