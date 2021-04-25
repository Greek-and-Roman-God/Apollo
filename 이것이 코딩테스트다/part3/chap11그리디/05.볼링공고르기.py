# 볼링공 고르기
m, n = map(int, input().split())
balls = list(map(int, input().split()))
dupl = m - len(list(set(balls)))
print(dupl)
print(int(m*(m-1)/2 - int(dupl*(dupl-1))))

# 5 3
# 1 2 3 2 3
# 5 * 4/2 - (5-3)
