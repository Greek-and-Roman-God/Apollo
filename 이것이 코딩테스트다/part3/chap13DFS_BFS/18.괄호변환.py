# 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058
from collections import Counter


def solution(p):
    answer = ''

    # ()의 개수가 같다면 '균형잡힌 괄호 문자열'
    # ()의 짝이 맞을 경우 '올바른 괄호 문자열'
    def balance(string):
        cnt = Counter(string)
        if cnt['('] == cnt[')']:
            return True
        return False

    def correct(string):
        cnt = 0
        for s in string:
            if s == '(':
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:
                return False

        return True

    def recur(p):
        if p == "":
            return ""
        u, v = "", ""
        flag = False
        for s in p:
            if not flag:
                u += s
                if balance(u):
                    flag = True
            else:
                v += s

        # print(u, v)

        if correct(u):
            return u + recur(v)
        else:
            u = u[1:-1]
            new_u = ""
            for c in u:
                if c == "(":
                    new_u += ")"
                else:
                    new_u += "("
            return "(" + recur(v) + ")" + new_u

    return recur(p)


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

# 괄호의 개수가 맞는지 확인하는 함수는 Counter 모듈을 사용
# 괄호 짝이 맞는지 확인하는 함수는 반복문 중간에 계속 cnt가 음수가 되는지 확인해서 짝에 맞지 않는 괄호가 존재하는직 확인
# 나머지는 문제에 적힌 순서 그대로 구현함
