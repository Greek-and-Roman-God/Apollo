# 10870 피보나치 수 5
# https://www.acmicpc.net/problem/10870

def fibo(n):
    if n > 1:
        return fibo(n-2) + fibo(n-1)
    elif n == 1:
        return 1
    else:
        return 0


n = int(input())
print(fibo(n))
