# 1850 최대공약수
# https://www.acmicpc.net/problem/1850

def gcd(a, b):
    result = 0
    while b > 0:
        result = b
        a, b = b, a % b
    return result


a, b = map(int, input().split())
print('1' * gcd(a, b))
