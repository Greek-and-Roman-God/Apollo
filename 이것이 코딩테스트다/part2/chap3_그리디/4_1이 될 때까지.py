import math
# 1이 될 때까지
# n, k = map(int, input().split())

# temp = n
# cnt = 0
# while True:
#     temp //= k

#     if temp == 0:
#         break
#     cnt += 1

# result = cnt + n % k
# print(result)


# 2021-07-25
n, k = map(int, input().split())
result = 0
while n != 1 and n > k:
    result += n % k + 1  # 1씩 뺄 횟수(나머지) + k로 나눈 횟수(1)
    n = n // k

result += n - 1  # 마지막 남은 k보다 작은 값은 따로 횟수를 더해준다.
print(result)
