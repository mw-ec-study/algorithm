#page 313 (문자열 뒤집기)

input = input()
count_0 = 0
count_1 = 0

for i in range(len(input)-1):
    if input[i] != input[i+1]:
        if input[i] == '0':
            count_0 += 1
        else:
            count_1 += 1

print(min(count_0, count_1))
