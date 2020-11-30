# 1157 단어 공부
# https://www.acmicpc.net/problem/1157

# 1 런타임에러
'''
word = input().upper()

count = 0
up_word = list(set(word))
char_dict = {}
print(up_word)
for char in up_word:
    char_dict[char] = word.count(char)
    # print(f'char {char} count {count} num {num}')
print(char_dict)
sorted_list = sorted(char_dict.items(), key = lambda x: x[1], reverse=True)
if sorted_list[0][1] == sorted_list[1][1]:
    print('?')
else:
    print(sorted_list[0][0])'''

# 입력받은 문자열을 모두 대문자로 바꿔줌
# 결과값이 대문자이고, count함수를 사용할 수 있도록
word = input().upper()

# word에 중복제거
# 여러번 등장하는 문자를 제거하여 count할 문자를 정리함
word_set = list(set(word))

# 반복문으로 [문자의 개수, 찾은 문자]형태의 리스트가 요소인 리스트를 만들어줌
# 문자의 개수를 기준으로 리스트를 정렬하여 가장 많이 등장한 문자를 출력할 것이므로 개수와 문자가 묶여있는 형태의 리스트를 만들었다.
cnt_list = []
for char in word_set:
    cnt_list.append([word.count(char),char])

# list[x][0]을 기준으로 오름차순 정렬
# 마지막 값들을 비교하여 결과를 출력할 것이므로 reverse를 사용하지 않았다.
# list[x][0]이 동일한 경우가 있다고 해도 가장 큰 수가 중복되는 경우는 '?'를 출력해줄 것이므로 상관없다.
cnt_list.sort()

# - 오름차순으로 정렬되어있어 마지막 값과 마지막에서 두번째 값을 비교하였다.
#   1. 문자의 개수가 중복되는 경우는 문자열의 길이가 2 이상일 경우에만 존재하므로 len을 사용하여 문자열의 길이가 1일 경우엔 if 조건문을 통과하지 못하도록 했다.
#   2. 문자의 개수의 최댓값이 중복되지 않는 경우와 문자열이 1인 경우엔 cnt_list의 마지막 요소의 문자부분을 출력하게 만듦
if len(cnt_list) > 1 and cnt_list[-1][0] == cnt_list[-2][0]:
    print('?')
else:
    print(cnt_list[-1][1])