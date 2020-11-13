# 싱히좌우
space = int(input())
plans = input().split(' ')
x,y = [1,1]

# 1
for plan in plans:
    if plan == 'U' and y > 1: 
        y = y - 1
        continue
    if plan == 'D' and y < space: 
        y = y + 1
        continue
    if plan == 'R' and x < space: 
        x = x + 1
        continue
    if plan == 'L' and x > 1: 
        x = x - 1
        continue

# 2
for plan in plans:
    if plan == 'U' and y > 1: 
        y = y - 1
    elif plan == 'D' and y < space: 
        y = y + 1
    elif plan == 'R' and x < space: 
        x = x + 1
    elif plan == 'L' and x > 1: 
        x = x - 1
print([y,x])

