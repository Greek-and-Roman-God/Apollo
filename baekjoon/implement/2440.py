# 2440 별찍기 - 3
# https://www.acmicpc.net/problem/2440
n = int(input())

blank = 0
star = n

for i in range(n):
    print('*'*star+' '*blank)
    blank += 1
    star -= 1
