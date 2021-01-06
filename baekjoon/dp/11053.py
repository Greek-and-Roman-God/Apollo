# 11053 가장 긴 증가하는 부분수열
# https://www.acmicpc.net/problem/11053

# 처음으로 혼자 풀었다...ㅜㅜㅠㅠ
import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
num_list = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    temp = 0
    for num, j in zip(num_list[0:i], dp):

        if num < num_list[i]:
            dp[i] = max(dp[i], j)
    dp[i] += 1
print(max(dp))
