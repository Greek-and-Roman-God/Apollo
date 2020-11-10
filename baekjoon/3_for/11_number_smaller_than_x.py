# X보다 작은 수
n, x = list(map(int,input().split(' ')))
data=list(map(int,input().split(' ')))

for num in data:
    if num < x: 
        print(num,end=" ")
        # if num != data[len(data)-1]: print(' ',end='')