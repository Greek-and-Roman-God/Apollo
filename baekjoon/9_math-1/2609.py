# 2609 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


x, y = map(int, input().split())
gcd = gcd(x, y)
lcm = (x*y) // gcd
print(gcd)
print(lcm)
