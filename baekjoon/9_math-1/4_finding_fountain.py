# 1193 분수찾기

X = int(input())

cnt = 1
temp = 0
multi = 1
while 1:
    temp += cnt
    print(f'temp {temp} cnt {cnt} X {X}')

    if temp >= X:
        break

    cnt += 1


print(cnt, temp)
# temp번째 수 1/(cnt+1)-1
fou_sum = cnt + 1
print(fou_sum)
if cnt % 2 == 0:
    cha = temp - X + 1
else:
    cha = X - temp + cnt
print(str(fou_sum-cha)+'/'+str(cha))

# print(str(cha)+'/'+str(fou_sum-cha))
