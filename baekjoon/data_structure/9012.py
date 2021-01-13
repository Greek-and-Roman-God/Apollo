# 9012 괄호
# https://www.acmicpc.net/problem/9012
import sys


def input():
    return sys.stdin.readline()


n = int(input())

for _ in range(n):
    ps = input()

    flag = 0
    for p in ps:
        if p == '(':
            flag += 1
        elif p == ')':
            flag -= 1

        if flag < 0:
            print('NO')
            break
    else:
        if flag == 0:
            print('YES')
        else:
            print('NO')
