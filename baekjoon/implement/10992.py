# 10992 별찍기 - 13
# https://www.acmicpc.net/problem/10992
n = int(input())
#   *       -> 2, *
#  * *      -> 1. *, 1, *
# *****     -> 5

#    *      -> 3, *
#   * *     -> 2, *, 1, *
#  *   *    -> 1, *, 3, *
# *******   -> 7

front = n - 1
between = 1
for i in range(n):
    if i == n-1:
        print('*'*(2*n-1))
    else:
        if i == 0:
            print(' '*front + '*')
        else:
            print(' '*front + '*' + ' '*between+'*')
            between += 2
        front -= 1
