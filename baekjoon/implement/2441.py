# 2441 별찍기 - 4
# https://www.acmicpc.net/problem/2441

n = int(input())

blank = 0
star = n

for i in range(n):
    print(' '*blank+'*'*star)
    blank += 1
    star -= 1
