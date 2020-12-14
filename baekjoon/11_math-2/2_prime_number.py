# 2581 소수
# https://www.acmicpc.net/problem/2581

# 가장 큰 수의 1/2까지만 돌면 소수를 찾을듯 -> 그 다음은 나눠질 수 있는 수가 없을 테니까
m = int(input())
n = int(input())
prime = []


if m <= 2 <= n:
    prime.append(2)

# 1은 소수가 아니므로 고려하지 않음
# if n-m > 0 and m == 1:
#     m += 1
# 2를 제외한 짝수는 소수가 될 수 없으므로 고려하지 않음
if m % 2 == 0:
    m += 1

for num in range(m, n+1, 2):
    if num == 1:
        continue
    for i in range(3, num//3+1):
        if num % i == 0:
            break
    else:
        # print(num, prime)
        prime.append(num)
# print(prime)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)


print('------방법2-------')
m = int(input())
n = int(input())
prime = []
for num in range(m, n+1):
    if num == 1:
        continue
    for i in range(2, num//2+1):
        if num % i == 0:
            break
    else:
        # print(num, prime)
        prime.append(num)
# print(prime)
if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)
