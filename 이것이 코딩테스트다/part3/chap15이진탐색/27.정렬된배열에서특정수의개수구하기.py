# 정렬된 배열에서 특정 수의 개수 구하기
#
n, x = map(int, input().split())
nums = list(map(int, input().split()))


# 시작 인덱스 찾기
start = 0
end = n
x_start = 0
while start < end:
    mid = (start + end) // 2

    if nums[mid] < x:
        start = mid
    else:
        end = mid

    if end == 0 or x > nums[end-1]:
        x_start = end
        break
# print(start, end)


# 끝 인덱스 찾기
start = 0
end = n
x_end = n
while start < end:
    mid = (start + end) // 2

    if nums[mid] <= x:
        start = mid
    else:
        end = mid

    if start == n-1 or nums[start+1] > x:
        x_end = start
        break
# print(start, end)
# print(x_start, x_end)
result = x_end-x_start + 1 if x_end-x_start > 0 else -1
print(result)
