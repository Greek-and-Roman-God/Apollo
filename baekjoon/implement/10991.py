# 10991 별찍기 - 16
# https://www.acmicpc.net/problem/10991
n = int(input())

front = n-1
repeat = 0
for i in range(n):

    print(' '*front+'*' + ' *'*repeat)
    repeat += 1
    front -= 1
