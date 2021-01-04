# 18238 ZOAC 2
# https://www.acmicpc.net/problem/18238
string = input()
# string = 'ZOAC'
move = 0
# 65 ~ 90
# A - > Z
# 65 + 25 -> 90
# 65 - 1  -> 90
cursor = 0  # 0 ~ 25
for s in string:
    up = cursor - (ord(s)-65)
    down = ord(s)-65 - cursor
    # print(up, down)

    if up < down:
        up += 26
    else:
        down += 26
    move += min(up, down)

    cursor = abs(ord(s)-65)
print(move)
