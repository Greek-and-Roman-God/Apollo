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
