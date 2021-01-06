# 11055 가장 큰 증가 부분수열
# https://www.acmicpc.net/problem/11055
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
num_list = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = num_list[1]

for i in range(2, n+1):

    for num, d in zip(num_list[:i], dp):

        if num < num_list[i]:
            dp[i] = max(dp[i], d)

    dp[i] += num_list[i]
print(max(dp))
