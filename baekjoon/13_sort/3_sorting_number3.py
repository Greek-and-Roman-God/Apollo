# 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys
n = int(sys.stdin.readline())
count = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1


for num, cnt in enumerate(count):
    if num:
        for _ in range(cnt):
            print(num)
