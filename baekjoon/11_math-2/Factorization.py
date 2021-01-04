# 11653 소인수분해
# https://www.acmicpc.net/problem/11653

# 1
n = int(input())

i = 2

while 1:
    if n == 1:
        break

    if n % i:
        i += 1
    else:
        print(i)
        n = n // i

# 2
n = int(input())
for i in range(2, n//2+1):
    while n % i == 0:
        print(i)
        n //= i
if n != 1:
    print(n)
