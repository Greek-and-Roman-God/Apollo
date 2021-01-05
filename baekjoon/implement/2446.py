# 2446 별찍기 - 9
# https://www.acmicpc.net/problem/2446
n = int(input())

blank = 0
star = n * 2 - 1
for i in range(2*n-1):
    print(' '*blank+'*'*star)
    if i < n-1:
        blank += 1
        star -= 2
    else:
        blank -= 1
        star += 2
