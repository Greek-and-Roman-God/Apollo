# 부품찾기
def check(m_item):

    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if n_list[mid] == m_item:
            return mid
        elif n_list[mid] < m_item:
            start = mid + 1
        else:
            end = mid - 1
    return


n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for item in m_list:
    result = check(item)

    if result:
        print("yes", end=" ")
    else:
        print("no", end=" ")
