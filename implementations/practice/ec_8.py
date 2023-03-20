''''
알파벳 대문자와 숫자로만 구성된 문자열
알파벳 오름차순 숫자 더한 값 출력
'''

string = input()

string_list = list(string)
answer_s = []
answer_n = 0

for s in string_list:
    if s.isalpha():
        answer_s.append(s)
    else:
        answer_n += int(s)
        
print(''.join(sorted(answer_s)) + str(answer_n))