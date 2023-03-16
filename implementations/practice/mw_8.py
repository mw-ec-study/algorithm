#page 322 (문자열 재정렬)
#is_alpha 라는 내장 함수가 있다..
input_str = input()
string, number = [], ['0','1','2','3','4','5','6','7','8','9']
sum_num = 0
result = []

for i in range(len(input_str)):
    if input_str[i] in number:
        sum_num += int(input_str[i]) #숫자만 따로
    else:
        result.append(input_str[i]) #알파벳만 따로 

result.sort()

if sum_num != 0:
    result.append(str(sum_num))

print(''.join(result))


