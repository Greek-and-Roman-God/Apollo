# 10866 덱
# https://www.acmicpc.net/problem/10866
import sys


def input():
    return sys.stdin.readline()


n = int(input())
deque = []
for _ in range(n):
    command = input().split()

    if command[0] == 'push_front':
        deque = [command[1]] + deque

    if command[0] == 'push_back':
        deque = deque + [command[1]]

    if command[0] == 'pop_front':
        if len(deque) > 0:
            print(deque[0])
            deque = deque[1:]
        else:
            print(-1)
    if command[0] == 'pop_back':
        if len(deque) > 0:
            print(deque[-1])
            deque = deque[:-1]
        else:
            print(-1)
    if command[0] == 'size':
        print(len(deque))
    if command[0] == 'empty':
        if len(deque) > 0:
            print(0)
        else:
            print(1)
    if command[0] == 'front':
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    if command[0] == 'back':
        if len(deque):
            print(deque[-1])
        else:
            print(-1)
