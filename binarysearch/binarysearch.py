'''
2 4 7 9 11 19 23
'''
def binarysearch(n,low,high): # n의 인덱스의 위치를 찾는다
    length = len(arr)
    start = 0
    end = length -1
    while start <=end: # 반드시 종료 조건 설정을 제대로 해야한다.
        standard = (start + end) //2 # 이렇게 기준 값을 재설정을 해줘야 한다. 

        if arr[standard] < n: # 중간값이 찾고자 하는 값보다 작을 때 -> 오른쪽으로 탐색
            start = standard+1
        elif arr[standard] > n:
            end = standard-1
        elif arr[standard] == n:
            return standard
    return -1
        


arr = list(map(int, input().split()))

result = binarysearch(4)
print(result)



