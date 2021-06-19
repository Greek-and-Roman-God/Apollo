# 편집 거리

string1 = input()
string2 = input()

length1, length2 = len(string1)+1, len(string2)+1

dp = [[0]*(length1) for _ in range(length2)]
dp[0][0] = 0

for i in range(1, length1):
    dp[0][i] = dp[0][i-1] + 1


for i in range(1, length2):
    dp[i][0] = dp[i-1][0] + 1

# print(dp)
for i in range(1, length2):
    # for d in dp:
    #     print(d)
    for j in range(1, length1):
        # print("i, j", i, j)
        if string1[j-1] == string2[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

print(dp)
