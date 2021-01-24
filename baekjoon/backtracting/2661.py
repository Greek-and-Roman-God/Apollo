# 2661 좋은 수열
# https://www.acmicpc.net/problem/2661
n = int(input())
result = []


def check(result):
    result = ''.join(list(map(str, result)))
    for n in range(len(result)//2):
        # if result[-1:0] == result[-2:-1]:
        # if result[-2:0] == result[-4:-2]
        # print(result[-n-1:], result[(-n-1)*2:-n-1])
        if result[-n-1:] == result[(-n-1)*2:-n-1]:
            return True
    return False


def dfs(i):
    global result
    if i == n:
        return

    for num in range(1, 4):  # 제일 작은 수를 구해야하므로 1, 2, 3을 순서대로 넣어주면서 체크
        result.append(num)
        # print(i, result)
        if check(result):   # 반복되는 부분이 있으면 마지막 값 pop
            result.pop()
            if num == 3:
                return

        else:
            dfs(i+1)
            if len(result) == n:    # 길이가 충족됐으면 리턴
                return
            result.pop()    # 아니면 다음 값을 찾아야하기 떄문에 마지막 값 pop


dfs(0)
print(int(''.join(list(map(str, result)))))
