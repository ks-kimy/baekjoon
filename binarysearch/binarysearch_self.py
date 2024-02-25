'''
2 4 7 9 11 19 23
'''


def binarysearch2(n,low,high):
    if low > high:
        return -1
    else:
        middle = (low+ high) //2
        if n == arr[middle]:
            return middle
        elif n < arr[middle]:
            binarysearch2(n,low,middle-1) # return 의 역할은 binarysearch2(n,low,middle-1) 에서의 콜스택 맨 위의 값에서 반환하는 것들을 계속 반환해주는 것
        elif n > arr[middle]:
            binarysearch2(n,middle+1,high)

arr = list(map(int, input().split()))
result = binarysearch2(19,0,len(arr)-1)
print(result)


