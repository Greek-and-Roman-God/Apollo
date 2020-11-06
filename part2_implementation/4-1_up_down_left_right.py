space = int(input())
plans = input().split(' ')
x,y = [1,1]

# direction = [{'U':+1},{'D':-1},{'L':-1},{'R':+1}]
# print(direction)
for plan in plans:
    if plan == 'U' and y > 1: 
        y = y - 1
    if plan == 'D' and y < space: 
        y = y + 1
    if plan == 'R' and x < space: 
        x = x + 1
    if plan == 'L' and x > 1: 
        x = x - 1
print([y,x])

