# 2445 별찍기 - 8
# https://www.acmicpc.net/problem/2445
n = int(input())


star = 1
blank = (n-1) * 2
for i in range(2*n-1):
    print('*'*star+' '*blank+'*'*star)
    if i < n-1:
        star += 1
        blank -= 2
    else:
        star -= 1
        blank += 2
