# 왕실의 나이트

moves = [[-2, 1], [-2, -1], [2, 1], [2, -1],
         [1, -2], [-1, -2], [1, 2], [-1, 2]]
position = list(input())
x = int(position[1])
y = ord(position[0]) - ord('a') + 1

result = 0
for move in moves:
    next_x = move[0] + x
    next_y = move[1] + y
    if 0 < next_x < 9 and 0 < next_y < 9:
        result += 1
print(result)
