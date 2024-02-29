# def recursion_combination(level):
#     if level == M:
#         arr.sort()
#         print(arr)
#         return
#     for i in range(N):
#         if visited[i] == 1: continue
#         if 
#         # visited[i] = 1
#         arr.append(numbers[i])
#         recursion_combination(level+1)
#         arr.pop()
#         visited[i] = 0

# N , M = map(int,input().split())
# numbers = [i for i in range(1,N+1)]
# visited = [0] * N
# arr = []

# recursion_combination(0)
nums = [1, 2, 3, 4, 5]

answer_list = []

def combi(n, ans):
    if n == len(nums):
        temp = [i for i in ans]
        answer_list.append(temp)
        return
    ans.append(nums[n])
    combi(n + 1, ans)
    ans.pop()
    combi(n + 1, ans)

combi(0, [])
print(answer_list)