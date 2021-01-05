# 2522 별찍기 - 12
# https://www.acmicpc.net/problem/2522

n = int(input())

blank = n-1
star = 1
for i in range(2*n-1):
    print(' '*blank+'*'*star)
    if i < n-1:
        blank -= 1
        star += 1
    else:
        blank += 1
        star -= 1
