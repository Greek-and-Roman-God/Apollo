# 1259 팰린드롬수
# https://www.acmicpc.net/problem/1259

while 1:
    num = input()
    if num == '0':
        break

    if list(num) == list(reversed(num)):
        print('yes')
    else:
        print('no')
