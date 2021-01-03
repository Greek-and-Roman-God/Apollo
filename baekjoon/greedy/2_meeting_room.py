# 1931 회의실 배정
# https://www.acmicpc.net/problem/1931
import sys
n = int(input())
times = []
for _ in range(n):
    times.append(tuple(map(int, sys.stdin.readline().split())))
# n = 11
# times = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9),
#          (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
times.sort(key=lambda x: (x[1], x[0]))
print(times)
i = 0
cnt = 1
for j in range(1, n):
    if times[j][0] >= times[i][1]:
        i = j
        cnt += 1
print(cnt)
