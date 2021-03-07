# 부등호
# https://www.acmicpc.net/problem/2529
n = int(input())
ch_list = input().split()

check = [False] * 10
mx, mn = "", ""


def ch(i, j, k):
    if k == '>':
        return i > j
    else:
        return i < j


def recu(cnt, s):
    global mx, mn
    if cnt > n:
        if len(mn) == 0:
            mn = s
        else:
            mx = s
        return

    for i in range(10):
        if check[i] == False:
            if cnt == 0 or ch(s[-1], str(i), ch_list[cnt-1]):
                check[i] = True
                recu(cnt + 1, s+str(i))
                check[i] = False


recu(0, "")
print(mx)
print(mn)
