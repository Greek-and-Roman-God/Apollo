# 문자열 재정렬
string = list(input())
string.sort()
number = 0
result = ""
while string:
    s = string.pop(0)
    if(ord('0') <= ord(s) <= ord('9')):
        number += int(s)
    else:
        result = s + ''.join(string) + str(number)
        break
print(result)
