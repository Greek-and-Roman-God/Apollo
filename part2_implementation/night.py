# 왕실의 나이트
data = input()
# 나이트의 위치
row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-2,1),(-1,+2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

result = 0
for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]
    if next_row  >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)

print([[0]*3 for _ in range(3)])
