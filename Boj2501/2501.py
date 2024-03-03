import math

N, K = map(int, input().split())
divisor = []
for i in range(1,int(math.sqrt(N)+1)):
    if N % i == 0 :
        divisor.append(i)
        if i != N/i:
            divisor.append(N//i)
divisor.sort()
# print(divisor)
print(divisor[K-1]) if len(divisor) >= K else print(0)


