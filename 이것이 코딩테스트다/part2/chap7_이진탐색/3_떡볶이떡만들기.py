# 떡볶이 떡 만들기
def cut(tteok):

    start = 0
    end = max(tteok) - 1
    cutt = 0
    while start <= end:
        mid = (start + end) // 2

        temp = sum([t-mid if t > mid else 0 for t in tteok])

        if temp >= h:
            start = mid + 1
            cutt = mid
        else:
            end = mid - 1
    return cutt


n, h = map(int, input().split())
tteok = list(map(int, input().split()))
print(cut(tteok))
