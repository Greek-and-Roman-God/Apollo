# 11651 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651
import sys
n = int(sys.stdin.readline())
coo = []
for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    coo.append(xy)
coo.sort(key=lambda x: (x[1], x[0]))

for x, y in coo:
    print(x, y)
