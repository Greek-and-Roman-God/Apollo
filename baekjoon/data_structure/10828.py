# 10828 스택
# https://www.acmicpc.net/problem/10828
import sys


def input():
    return sys.stdin.readline()


def push(lst, command):
    lst.append(command[1])


def pop(lst):
    if len(lst) != 0:
        result = lst[-1]
        del lst[-1]
        # print(lst)
        return result
    else:
        return -1


def size(lst):
    return len(lst)


def empty(lst):
    if len(lst) == 0:
        return 1
    else:
        return 0


def top(lst):
    if len(lst) > 0:
        return lst[-1]
    else:
        return -1


n = int(input())
lst = []
for _ in range(n):
    command = input().split()

    if command[0] == 'push':
        push(lst, command)
    elif command[0] == 'pop':
        print(pop(lst))
    elif command[0] == 'size':
        print(size(lst))
    elif command[0] == 'empty':
        print(empty(lst))
    elif command[0] == 'top':
        print(top(lst))
