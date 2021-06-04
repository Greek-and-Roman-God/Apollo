# 고정점 찾기
n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n

while start < end:
    mid = (start + end) // 2

    if nums[mid] <= mid:
        start = mid + 1
    else:
        end = mid - 1

    print(start, end)

if nums[start] == start:
    print(start)
else:
    print(-1)
