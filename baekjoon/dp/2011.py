# 2011 암호코드
# https://www.acmicpc.net/problem/2011
code = list(map(int, input()))
l = len(code)
print(code)
dp = [0] * (l+1)
if code[0] == '0':
    print(0)
else:
    code = [0] + code
    dp[0] = 1
    dp[1] = 1
    for n in range(2, l+1):
        temp1 = code[n]
        temp2 = code[n-1]*10 + code[n]
        if 1 <= temp1 and temp1 <= 10:
            dp[n] += dp[n-1]
        if 10 <= temp2 and temp2 <= 26:
            dp[n] += dp[n-2]
        dp[n] %= 1000000

# print(code)
    print(dp[l])


# 나누는 숫자 자릿수 잘못써서 몇시간을 헤맴...
code = ['0'] + list(input())
dp = [0] * (len(code))
if code[1] == '0':
    dp = [0]
else:
    dp[0] = 1
    dp[1] = 1
    for n in range(2, len(code)):
        temp1 = int(code[n])
        temp2 = int(''.join(code[n-1:n+1]))
        # print(temp1, temp2)
        if 1 <= temp1 <= 10:
            dp[n] += dp[n-1]
        if 9 < temp2 <= 26:
            dp[n] += dp[n-2]
        dp[n] %= 1000000


print(dp[-1])
