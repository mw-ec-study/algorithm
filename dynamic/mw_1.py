number = int(input())

dp_table = [0] * (number + 1)

for i in range(2, number + 1):
    dp_table[i] = dp_table[i - 1] + 1 # i를 달성하는 최소 횟수를 이전 i를 달성하는 횟수+1이 최솟값이라고 가정

    if i % 5 == 0: #ex) i = 10이면, (i = 2를 달성하는 횟수 + 1) 과 (이전 i + 1) 비교하여 더 작은것 선택 why? 2 * 5 = 10이므로  
        if (dp_table[i//5] + 1) < dp_table[i]: dp_table[i] = dp_table[i//5] + 1

    if i % 3 == 0:
        if (dp_table[i//3] + 1) < dp_table[i]: dp_table[i] = dp_table[i//3] + 1

    if i % 2 == 0:
        if (dp_table[i//2] + 1) < dp_table[i]: dp_table[i] = dp_table[i//2] + 1

print(dp_table[number])