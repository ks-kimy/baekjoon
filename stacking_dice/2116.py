import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
# 우선 밑면을 결정할 수 있는 것을 짜볼까?
# 무조건 1,2,3,4,5,6  으로 이루어져 있다
# Index기준으로 0-5 , 1-3, 2-4 로 연결
def index_check(arr,number): # 해당되는 arr, number 을 입력받는다. 
    return arr.index(number)

def side_max(under, up): #under 와 Up 에 대한 정보.
    temp = 0
    for i in range(1,7):
        if i == under or i == up:
            continue
        if temp < i:
            temp = i 
    return temp 

def find_bases(arr, id): # 해당하는 index의 숫자를 반환
    if id == 0:
        return arr[5]
    if id ==1:
        return arr[3]
    if id == 2:
        return arr[4]
    if id == 3:
        return arr[1]
    if id == 4:
        return arr[2]
    if id == 5:
        return arr[0]


N = int(input())

 # a-f (0-5), b-d (1-3), c-e(2-4) 끼리 짝 
dice_lists = [list(map(int, input().split())) for _ in range(N)]
result = 0
for i in range(6): # 맨 아래 주사위의 밑면만 정해지면 자동으로 위의 것들이 정해진다. 
    dice_underside = dice_lists[0][i] # 첫번째 주사의의 아랫밑면의 숫자.
    dice_upside = find_bases(dice_lists[0], i)
    temp  = side_max(dice_underside, dice_upside)
    # print(dice_underside,dice_upside)
    for j in range(1,N):
        next_dice_underside_index = index_check(dice_lists[j],dice_upside) # 두 번째 주사위로 다음 주사위의 밑면의 숫자의 인덱스를 할당해둠.
        next_under_num = dice_lists[j][next_dice_underside_index]
        next_upside_num = find_bases(dice_lists[j], next_dice_underside_index)
        temp += side_max(next_under_num,next_upside_num)
        dice_upside = next_upside_num
        # print(next_under_num,next_upside_num)
    if result < temp:
        result = temp
    # print()
    # print(temp)

print(result)


