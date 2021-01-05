# 2442 별찍기 - 5
# https://www.acmicpc.net/problem/2442

n = int(input())

blank = n - 1
star = 1

for i in range(n):
    print(' '*blank + '*'*star)
    blank -= 1
    star += 2
