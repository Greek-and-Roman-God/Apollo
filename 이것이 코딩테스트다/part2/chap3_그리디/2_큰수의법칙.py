# 큰 수의 법칙

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort(reverse=True)

num1 = nums[0]
num2 = nums[1]

result = 0
m2 = m
while m:
    for _ in range(k):
        m -= 1
        result += num1
        if m == 0:
            break
    m -= 1
    result += num2
    if m == 0:
        break
print(result)

# 2
count = int(m2/(k+1)) * k + m2 % (k+1)

result = count * num1 + (m2-count) * num2
print(result)
