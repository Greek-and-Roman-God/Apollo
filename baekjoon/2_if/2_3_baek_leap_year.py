# 윤년
year=int(input())
result = 0
if (not(year%4) and year%100) or not(year%400):
    result=1
print(result)