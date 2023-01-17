N = int(input())

dp_table = [0] * (N + 1)

dp_table[1] = 1
dp_table[2] = 3

'''
2 x 1
2
2

2 x 2
1 1  2 2  3 3
1 1  2 2  3 3

2 x 3
1 1 2  2 2 2  3 3 2  2 1 1  2 3 3   
1 1 2  2 2 2  3 3 2  2 1 1  2 3 3
'''


for i in range(3, N + 1):
    dp_table[i] = (dp_table[i - 2] * 2 + dp_table[i - 1]) % 796796 #(i - 2 를 채운 방식으로 한번 더 채우는 방법) + (i - 1 만큼 채우고 2x1 만큼 더 채워주는 방법)

print(dp_table[N])