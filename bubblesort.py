'''
9
5 0 8 1 3 6 7 0 4 2 3 6 5 4 5 9 4 5 3 1
'''


def counting_sort():
    for i in range(10):
        for j in arr:
            if i == j:
                counting[i] += 1
    for i in range(1,10):
        counting[i]+=counting[i-1]
    
    for i in range(19,-1,-1):
        counting[arr[i]] -= 1
        data[counting[arr[i]]] = arr[i]
 

N = int(input())    
arr = list(map(int, input().split()))

# data = [0]*(20) #data 에 대한 정보 입력        
counting = [0] * (N+1) #카운팅에 대한 정보 입력  인덱스에 대한 것은 입력 받는 값에 대한 정보. 내부 정보는 그 인덱스 숫자에 대한 값의 횟수
counting_sort()
print(counting)
print(data)