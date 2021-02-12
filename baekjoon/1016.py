# 1016 제곱 ㄴㄴ 수
# https://www.acmicpc.net/problem/1016

from math import sqrt
min, max = map(int, input().split())
# print(sqrt(min), sqrt(max))
temp_min = int(sqrt(min))
temp_max = int(sqrt(max))

temp = 0

for i in range(temp_min, temp_max+1):
    if i**2 <= max:
        temp += 1
# print(temp)
# print(max-min+1)
print(max-min+1-temp)
# n = 1000
# mat = [0] * (n+1)
# mat[1] = 1

# for i in range(2, n):
#     if i ** 2 <= n and mat[i**2] == 0:
#         mat[i**2] = 1

# nums = []

# for num, m in enumerate(mat):
#     if m == 1:
#         nums.append(num)
# print(nums)

# # for num in range(min, max+1):
# #     for nono in nums:
