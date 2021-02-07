# 검증수
# https://www.acmicpc.net/problem/2475
nums = list(map(int, input().split()))

result = 0
for num in nums:
    result += num**2
print(result % 10)
