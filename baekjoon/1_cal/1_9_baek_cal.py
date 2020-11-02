# 사칙연산
a=int(input())
b=input()
for num in range(len(b)-1,-1,-1):
    print(a*int(b[num]))
print(a*int(b))