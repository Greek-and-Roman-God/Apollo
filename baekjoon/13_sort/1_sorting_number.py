# 2750 수 정렬하기
# https://www.acmicpc.net/problem/2750
n = int(input())
nums = []
for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort()
for num in nums:
    print(num)
