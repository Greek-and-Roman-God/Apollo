# 4153 직각삼각형
# https://www.acmicpc.net/problem/4153

while 1:
    sides = list(map(int, input().split()))
    a, b, c = sorted(sides)

    if not (a and b and c):
        break
    elif a**2 + b**2 == c**2:
        print("right")
    else:
        print("wrong")
