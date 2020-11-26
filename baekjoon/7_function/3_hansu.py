# 한수

#1 flag사용

rang = int(input())
result = rang if rang < 100 else 99
temp = []

for num in range(100, rang+1):
    num = str(num)
    diff = int(num[0]) - int(num[1])
    flag = True
    for i in range(1,len(num)-1):
        if diff != int(num[i]) - int(num[i+1]):
            flag = False
    if flag:
        result += 1
print(result)

#2 for else 사용
rang = int(input())
result = rang if rang < 100 else 99
temp = []

for num in range(100, rang+1):
    num = str(num)
    diff = int(num[0]) - int(num[1])
    for i in range(1,len(num)-1):
        if diff != int(num[i]) - int(num[i+1]):
            break
    else:
        result += 1

print(result)

# 다른 사람 풀이
N = int(input())
hansu = 0

# 값 전체를 돌면서
for k in range(N):
    # 99까지는 그냥 +1
    if k+1 <= 99:
        hansu += 1
    else: # 나머지는 각 자리 수의 차가 값이 같으면 + 1
        num = list(map(int, str(k+1)))
        # 최대수가 1000이므로 3자리만 확인하면 됨
        if num[0] - num[1] == num[1] - num[2]:
            hansu += 1

print(hansu)