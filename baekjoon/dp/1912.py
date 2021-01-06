# 1912 연속합
# https://www.acmicpc.net/problem/1912

n = int(input())
num_list = [0] + list(map(int, input().split()))

dp = [-1000] * (n+1)

for i in range(1, n+1):
    dp[i] = max(dp[i-1] + num_list[i], num_list[i])
print(max(dp))
