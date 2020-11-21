# 한수

rang = int(input())
result = rang if rang < 100 else 99
temp = []

for num in range(100, rang+1):
    diff = int(str(num)[0]) - int(str(num)[1])
    flag = True
    for i in range(1,len(str(num))-1):
        if diff != int(str(num)[i]) - int(str(num)[i+1]):
            flag = False
    if flag:
        result += 1

print(result)

# 다른 사람 풀이
N = int(input())
hansu = 0

for k in range(N):
    if k+1 <= 99:
        hansu += 1
    else:
        num = list(map(int, str(k+1)))
        if num[0] - num[1] == num[1] - num[2]:
            hansu += 1

print(hansu)