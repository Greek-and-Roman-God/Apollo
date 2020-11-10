# A+B-7
count = int(input())

for num in range(1,count+1):
    a,b = list(map(int,input().split(' ')))
    print(f'Case #{num}: {a+b}')