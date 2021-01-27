# 1934 최소공배수
# https://www.acmicpc.net/problem/1934
import sys
import math


def input():
    return sys.stdin.readline().strip()


t = int(input())

# 1 시간 초과
# for _ in range(t):
#     a, b = map(int, input().split())
#     if a > b:
#         a, b = b, a

#     for num in range(b, a*b+1, b):
#         if num % a == 0:
#             print(num)
#             break

# 2
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    print(a*b//math.gcd(a, b))
