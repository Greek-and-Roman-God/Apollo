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

word = input().upper()

word_set = list(set(word))
cnt_list = []
for char in word_set:
    cnt_list.append([word.count(char),char])
cnt_list.sort()
# print(cnt_list)
if len(cnt_list)>1 and cnt_list[-1][0] == cnt_list[-2][0]:
    print('?')
else:
    print(cnt_list[-1][1])