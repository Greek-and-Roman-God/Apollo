# 10814 나이순 정렬
# https://www.acmicpc.net/problem/10814
import sys
n = int(sys.stdin.readline())
members = []
for _ in range(n):
    info = sys.stdin.readline().split()
    members.append(info)
members.sort(key=lambda x: int(x[0]))

for age, name in members:
    print(age, name)
