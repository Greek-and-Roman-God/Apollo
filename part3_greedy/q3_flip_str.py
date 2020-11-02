# Q3 문자열 뒤집기
str = input()
pre=""
count0=0
count1=0
for c in str:
    if pre == c:
        pass
    elif c == "0": count0+=1
    else: count1+=1
    pre = c

if count0 < count1: print(count0)
else: print(count1)
    

