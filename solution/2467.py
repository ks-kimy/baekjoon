import sys
sys.setrecursionlimit(10000000)
from itertools import combinations 
def pointer(start, end):
    global result ,a,b
    if start == end:
        return
    start_value = solutions[start]
    end_value = solutions[end]
    add = start_value + end_value
    if add == 0:
        a = start_value
        b = end_value
        return
    if abs(result) >= abs(add):
        result = add
        a = start_value
        b = end_value
    if add > 0:
        end -= 1
        pointer(start,end)
    elif add < 0:
        start += 1
        pointer(start,end)
N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
result = 2000000000
a= 0 
b=0
pointer(0,N-1)
print(a,b)