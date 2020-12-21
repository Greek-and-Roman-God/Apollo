# 1002 터렛
# https://www.acmicpc.net/problem/1002
t = int(input())


for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x2-x1)**2 + (y2-y1)**2

    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == (r1 + r2)**2 or dist == (r2 - r1)**2:
        print(1)
    elif dist > (r1 + r2)**2 or dist < (r2 - r1)**2:
        print(0)
    else:
        print(2)
