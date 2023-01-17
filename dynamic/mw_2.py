N = int(input())
food = list(map(int, input().split()))

dp_table = [0] * (N + 1)

dp_table[1] = food[0]
dp_table[2] = max(food[0], food[1])

for i in range(3, N + 1):
    #i = 3 이면 1,3번째 식량창고선택과 2번째 식량창고 선택지가 있음. 이중 더 큰것을 선택
    dp_table[i] = max(dp_table[i - 1], dp_table[i - 2] + food[i - 1]) 

print(dp_table[N])



