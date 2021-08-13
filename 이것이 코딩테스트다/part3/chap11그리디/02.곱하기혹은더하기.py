# 곱하기 혹은 더하기
numbers = list(map(int, list(input())))
print(numbers)

result = numbers.pop(0)

while numbers:
    number = numbers.pop(0)
    print(result, number)
    if result and number:
        result *= number
    else:
        result += number
print(result)

# 2021-07-18
numbers = list(map(int, list(input())))
print(numbers)

result = numbers[0]
for i in range(1, len(numbers)):
    num = numbers[i]
    result = result + num if num <= 1 or result <= 0 else result * num

print(result)
