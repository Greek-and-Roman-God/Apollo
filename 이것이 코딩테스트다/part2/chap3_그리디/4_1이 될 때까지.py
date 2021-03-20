import math
# 1이 될 때까지
n, k = map(int, input().split())

temp = n
cnt = 0
while True:
    temp //= k

    if temp == 0:
        break
    cnt += 1

result = cnt + n % k
print(result)
