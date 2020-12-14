# 1712 손익분기점
# https://www.acmicpc.net/problem/1712

A, B, C = list(map(int, input().split()))
cnt = 0

if B >= C:
    cnt = -1
else:
    # print(f'{A // (C - B)} {A / (C - B)} {A / (C - B) == A // (C - B)}')
    cnt = A // (C - B) + 1

print(cnt)
