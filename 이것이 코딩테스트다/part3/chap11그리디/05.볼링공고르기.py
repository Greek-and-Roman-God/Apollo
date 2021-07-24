# 볼링공 고르기
# m, n = map(int, input().split())
# balls = list(map(int, input().split()))
# dupl = m - len(list(set(balls)))
# print(dupl)
# print(int(m*(m-1)/2 - int(dupl*(dupl-1))))

# 5 3
# 1 2 3 2 3
# 5 * 4/2 - (5-3)

# 2021-07-25
n, m = map(int, input().split())
balls = list(map(int, input().split()))
result = n * (n-1) // 2

for ball in set(balls):
    count = balls.count(ball)
    result -= count * (count - 1) // 2

print(result)
