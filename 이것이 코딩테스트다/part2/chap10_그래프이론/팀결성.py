# 팀 결성
n, m = map(int, input().split())
check = [0] * (n+1)
for i in range(n+1):
    check[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        if check[a] < check[b]:
            check[b] = a
            for num in range(n+1):
                if check[num] == b:
                    check[num] = a
        else:
            check[a] = b
            for num in range(n+1):
                if check[num] == a:
                    check[num] = b
    elif oper == 1:
        if check[a] == check[b]:
            print("YES")
        else:
            print("NO")
