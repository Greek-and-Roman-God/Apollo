# 11054 가장 긴 바이토닉 부분 수열
# https://www.acmicpc.net/board/view/41941

import sys
def input(): return sys.stdin.readline().strip()


n = int(input())
num_list = [0] + list(map(int, input().split()))

dp_up = [0] * (n+1)
dp_down = [0] * (n+1)
dp_up[1] = 1
dp_down[-1] = 1
# 증가수열
for i in range(2, n+1):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_up[i] = max(dp_up[i], dp_up[j])
    dp_up[i] += 1

# 감소수열
for i in range(n-1, 0, -1):
    for j in range(n, i, -1):
        if num_list[i] > num_list[j]:
            dp_down[i] = max(dp_down[i], dp_down[j])
    dp_down[i] += 1

print(max([up+down for up, down in zip(dp_up, dp_down)])-1)
