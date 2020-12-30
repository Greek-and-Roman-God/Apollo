# 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

n = int(input())
coo = []
for _ in range(n):
    xy = list(map(int, input().split()))
    coo.append(xy)
coo.sort()
for x, y in coo:
    print(x, y)
