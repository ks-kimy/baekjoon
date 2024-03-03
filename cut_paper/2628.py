import sys
sys.stdin = open("input.txt", "r")

width , height = map(int, input().split())
numbers = int(input())
cut_arr = [] # 자르는 방법. sort 하기 위해 선언
cut_width = []
cut_height = []
widths = [] # 가로 길이들의 집합
heights = [] # 세로 길이들의 집합
for _ in range(numbers):
    kind, spot = map(int,input().split())
    cut_arr.append([kind,spot])

for method in cut_arr:
    if method[0] == 0:
        cut_height.append(method)
    if method[0] == 1:
        cut_width.append(method)
cut_height.sort(key= lambda x: x[1]) # cut_height은 --- 이렇게 자른다. 
cut_height.append([0,height])
cut_width.append([1,width])
cut_width.sort(key= lambda x: x[1]) # cut_width 는 ㅣ 이렇게 자른다.
start = 0
end = height
for hgt in cut_height:
    heights.append(hgt[1]-start)
    start = hgt[1]

start = 0
end = width
for wid in cut_width:
    widths.append(wid[1]-start)
    start = wid[1]
result = 0
for w in widths:
    for h in heights:
        area = w*h

        if result < area:
            result = area
print(result)


# print(heights)
# print(widths)
# print(cut_width)   
# print(cut_height)
