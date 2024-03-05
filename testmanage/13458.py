import sys
import math
sys.stdin = open("input.txt", "r")
def manager():
    managers = 0
    for students in classes:
        rest_students = students - B
        managers += 1
        if rest_students > 0:
            managers += math.ceil(rest_students / C )        
    return managers


N =int(input())
classes = list(map(int,input().split()))
B, C = map(int, input().split())
result = manager()
print(result)
