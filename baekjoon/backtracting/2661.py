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

    for num in range(1, 4):
        result.append(num)
        # print(i, result)
        if check(result):
            result.pop()
            if num == 3:
                return

        else:
            dfs(i+1)
            if len(result) == n:
                return
            result.pop()


dfs(0)
print(int(''.join(list(map(str, result)))))
