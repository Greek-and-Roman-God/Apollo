# 2839 설탕배달
N = int(input())

cnt = 0
temp = 0

if N % 5 == 0:
    cnt = N // 5

elif N % 5 == 1:
    cnt = N // 5 + 1

elif (N % 5 == 4 or N % 5 == 2) and N > 10:
    cnt = N // 5 + 2

elif N % 3 == 0 and (N % 5) % 3 != 0:
    cnt = N // 3

else:
    cnt = N // 5
    N = N % 5
    cnt += N // 3

    if N % 3:
        cnt = -1


print(cnt)
