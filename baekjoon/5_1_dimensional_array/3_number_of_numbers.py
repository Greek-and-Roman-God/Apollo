# 숫자의 개수

a,b,c = int(input()),int(input()),int(input())

multi = a*b*c
for i in range(0,10):
    print(str(multi).count(str(i)))