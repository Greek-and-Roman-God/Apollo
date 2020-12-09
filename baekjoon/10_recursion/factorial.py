# 10872 팩토리얼
# https://www.acmicpc.net/problem/10872

N = int(input())


def fac(n):
    result = 1
    if n > 1:
        result *= n * fac(n-1)
        return result
    else:
        return 1


print(fac(N))
