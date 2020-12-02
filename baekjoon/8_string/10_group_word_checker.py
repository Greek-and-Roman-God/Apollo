# 1316 그룹 단어 체커
# https://www.acmicpc.net/step/7

word_cnt = int(input()) # 입력받을 단어의 개수
group_word_cnt = 0 # 그룹단어의 개수
for _ in range(word_cnt):
    word = input()

    # 직전 문자 temp와 현재 문자 char를 비교하여 직전과 달라지면 char_arr에 append
    char_arr = []
    temp = ''
    for char in word:
        if temp != char:
            char_arr.append(char)
        temp = char
    # print(char_arr, list(set(word)))

    # 위에서 구한 char_arr(문자가 여러번 나오는 경우만 줄임)와 중복제거한 list를 길이 비교 -> 같으면 그룹단어
    # set은 순서가 없기 떄문에 길이로 비교
    if len(char_arr) == len(list(set(word))):
        group_word_cnt += 1
    
print(group_word_cnt)



# 정리
word_cnt = int(input()) # 입력받을 단어의 개수
group_word_cnt = 0 # 그룹단어의 개수
for _ in range(word_cnt):
    word = input()

    char_arr = []
    temp = ''

    for char in word:
        if temp != char:
            char_arr.append(char)
        temp = char

    if len(char_arr) == len(list(set(word))):
        group_word_cnt += 1


    
print(group_word_cnt)