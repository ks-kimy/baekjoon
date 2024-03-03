import sys
sys.stdin = open("input.txt", "r")


def switch_turn(switch_mod):
    if switch_mod == 0:
        return 1
    if switch_mod == 1:
        return 0


N = int(input())
switch_arr = list(map(int, input().split()))
students = int(input())
length = len(switch_arr)
for _ in range(students):
    sex, switch_num = map(int, input().split())
    multiply = switch_num
    if sex == 1:
        switch_num -= 1 # index 에 맞게 조정
        while True:
            if switch_num >= length: # 변하는 스위치 번호가 스위치 배열의 인덱스를 초과했을 경우.
                break 
            switch_arr[switch_num] = switch_turn(switch_arr[switch_num])
            switch_num += multiply
    if sex == 2:
        different_num = 0 # switch_num 을 기준으로 달라지는 위치.
        switch_num -= 1
        left_num = switch_num
        right_num = switch_num
        # print(left_num, right_num)
        # print(switch_arr[left_num] == switch_arr[right_num])
        while switch_arr[left_num] == switch_arr[right_num]:
            left_num -= 1
            right_num += 1
            # 여기서 많이 해멨다. diffent_num 으로 자르지 말고 -=1 , +=1 로 하는 것이 훨씬 깔끔정확.
            if left_num < 0 or right_num > length-1:
                break
            if switch_arr[left_num] != switch_arr[right_num]: # 왼쪽과 오른쪽의 값이 다르면
                break
            # Break 위치와 Different_num 의 값 변경하는 위치가 다음과 같아야만 한다. 왜냐. 실행이 되어야만 different
            # num 의 값이 변하기 때문이다. 
            different_num +=1
            # print('done')
        # print(different_num)
        for dif in range(0, different_num+1):
            if dif == 0:
                switch_arr[switch_num] = switch_turn(switch_arr[switch_num])    
            else:
                switch_arr[switch_num+dif] = switch_turn(switch_arr[switch_num+dif])
                switch_arr[switch_num-dif] = switch_turn(switch_arr[switch_num-dif])
    # print(switch_arr)
i = 0
while True:
    print(*switch_arr[i:i+20])
    i+=20

    if i>= length:
        break
# cnt = 0
# for ans in switch_arr:
#     if cnt % 20 == 0 and cnt != 0:
#         print('\n')
#     print(ans, end=' ')
#     cnt+=1
