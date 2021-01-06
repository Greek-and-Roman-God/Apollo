# 11722 가장 긴 감소하는 부분수열
# https://www.acmicpc.net/problem/11722

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
num_list = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    for num, d in zip(num_list[:i], dp):
        if num > num_list[i]:
            dp[i] = max(dp[i], d)
    dp[i] += 1
print(max(dp))
