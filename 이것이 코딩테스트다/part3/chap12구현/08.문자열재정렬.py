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


# 2021-08-13
string = list(map(ord, input()))
string.sort()
answer = ""
number = 0
for s in string:
  temp = chr(s)
  if not (48 <= s <= 57):
    answer += temp
  else:
    number += int(temp)
print(answer+str(number))