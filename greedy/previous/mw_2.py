#page 312 (곱하기 혹은 더하기)
input = input()
result = 0

#이전 숫자가 0이나 1이면 곱셈보다 덧셈을 해주는게 더 커진다.
for i in range(len(input)):
    if int(input[i]) <= 1 or result <= 1:
        result += int(input[i])
    else:
        result *= int(input[i])

print(result)
