# 문자열 뒤집기
string = list(input())
cnt = [0, 0]
cnt[int(string[0])] += 1
idx = 0
# 0001100
while idx < len(string)-1:
    if string[idx] != string[idx+1]:
        cnt[int(string[idx+1])] += 1
    idx += 1
# print(cnt)
# cnt = [2, 1]

print(min(cnt))

# 2021-07-18
s = list(input())
cnt0, cnt1 = 0, 0
pre = ""
for ss in s:
    if ss != pre:
        if ss == "0":
            cnt0 += 1
        else:
            cnt1 += 1
        pre = ss

print(min(cnt0, cnt1))
