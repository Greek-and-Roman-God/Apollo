# 두 배열의 원소 교체
n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i, (num1, num2) in enumerate(zip(a, b)):
    if num1 <= num2 and k:
        a[i], b[i] = b[i], a[i]
        k -= 1
    else:
        break
print(sum(a))
