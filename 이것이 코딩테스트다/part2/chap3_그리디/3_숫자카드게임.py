# 숫자 카드 게임

n, m = map(int, input().split())

cards = [min(list(map(int, input().split()))) for _ in range(n)]
print(max(cards))

# 2
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001

    for d in data:
        min_value = min(min_value, d)

    result = max(result, min_value)

print(result)


# 2021-07-18

n, m = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(min(list(map(int, input().split()))))

print(max(nums))
