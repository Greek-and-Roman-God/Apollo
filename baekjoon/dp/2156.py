# 2156 포도주 시식
# https://www.acmicpc.net/problem/2156
import sys
n = int(input())

wine = [0]
for _ in range(n):
    score = int(input())
    wine.append(score)
dp = [0]*(n+1)
dp[1] = wine[1]

if n > 1:
    dp[2] = wine[1] + wine[2]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])

print(dp[n])

# 다른 사람 풀이


def input(): return sys.stdin.readline().strip()


num = int(input())
glasses = list(int(input()) for _ in range(num))
dp = list()


if num < 3:
    print(sum(glasses))
else:
    dp.append(glasses[0])
    dp.append(dp[0] + glasses[1])
    dp.append(max(dp[1], dp[0]+glasses[2], glasses[1] + glasses[2]))

    for i in range(3, num):
        dp.append(max(dp[i-1], dp[i-3] + glasses[i-1] +
                      glasses[i], dp[i-2] + glasses[i]))

    print(dp[-1])
