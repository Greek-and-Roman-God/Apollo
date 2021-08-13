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


# 2021-08-13
x, y = list(input())
# print(x,y)
x = ord(x) - ord('a')
y = ord(y) - ord('1')

moves = [(1, -2), (-1, -2),(1, 2), (-1, 2),(-2, 1), (-2, 1),(2, 1), (2, -1)]

answer = 0
for move in moves:
  nx, ny = x+move[0], y + move[1]
  if 0 <= nx < 8 and 0 <= ny < 8:
    answer += 1

print(answer)