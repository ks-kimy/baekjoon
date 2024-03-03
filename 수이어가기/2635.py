import sys
sys.stdin = open("input.txt", "r")
N = int(input())
answer = 0

second_num = 0 # 두 번째 숫자 초기 설정
for i in range(1,N+1): # 1부터 검사하여 N까지
    start_num = 2 # 2번 인덱스 부터 시작
    result_arr = [] 
    result_arr.append(N) # 첫 번째 숫자
    second_num = i
    result_arr.append(second_num)
    while True:
        next_num = result_arr[start_num-2] - result_arr[start_num-1]
        if next_num < 0:
            break
        result_arr.append(next_num)
        start_num += 1
    length = len(result_arr)
    if answer <= length:
        answer = length
        answer_list = result_arr
print(answer)
print(*answer_list)