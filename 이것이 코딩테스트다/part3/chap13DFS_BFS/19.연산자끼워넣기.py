# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

max_val = int(-1e10)
min_val = int(1e10)

# 나올 수 있는 모든 경우의 수를 구해서 비교해야함으로 dfs를 사용
# num_idx - 지금 계산할 숫자
# opers - 남은 연산자 개수 리스트
# result - 직전에 계산된 결과


def dfs(num_idx, opers, result):
    global max_val, min_val

    # opers가 모두 0일 경우 (= 남은 연산자가 없을 경우)
    if not any(opers):
        max_val = max(max_val, int(result))
        min_val = min(min_val, int(result))
        return

    # 남은 연산자를 사용해서 하나씩 계산
    for i, (oper, o_cnt) in enumerate(zip(["+", "-", "*", "//"], opers)):
        # 연산자가 있을 경우
        if o_cnt != 0:
            # result와 num[num_idx]를 사용해서 연산하고 사용한 연산은 -1

            # result가 음수이고 연산자가 //일 때 원하는 값이 나오지 않으므로(올림값에 -가 붙여서 나옴)
            # 원하는 값을 얻기 위해 조건문을 사용하여 따로 연산
            if oper == "//" and result < 0:
                temp = -eval(str(result)[1:] + oper + str(nums[num_idx]))
            else:
                temp = eval(str(result) + oper + str(nums[num_idx]))
            opers[i] -= 1
            # 다음 연산을 위해 num_idx+1, 남은 연산자 개수 리스트 opers, 지금 연산의 결과 temp를 사용해서 재귀
            dfs(num_idx+1, opers, temp)

            opers[i] += 1


dfs(1, opers, nums[0])

print(max_val, min_val)
