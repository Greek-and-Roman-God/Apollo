# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
n = int(input())

numbers = list(map(int, input().split()))

dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for number, j in zip(numbers[:i], dp[:i]):
        if numbers[i] > number:
            dp[i] = max(dp[i], j)

    dp[i] += 1

print(dp)
