# 음계
# https://www.acmicpc.net/problem/2920

mel = list(map(int, input().split()))
scale = [1, 2, 3, 4, 5, 6, 7, 8]
# print(list(reversed(scale)))
if mel == scale:
    print('ascending')
elif mel == list(reversed(scale)):
    print('descending')
else:
    print('mixed')
