# 나머지
numbers = []
for _ in range(0,10):
    numbers.append(int(input())%42)

print(len(set(numbers)))