N, M = map(int, input().split())

moneys = []
# 10000, [13, 11, 7, 6, 3, 2]
for i in range(N):
    moneys.append(int(input()))

dp_table = [99999999] * (M + 1)
dp_table[0] = 0

for money in moneys: #화폐 단위별로 금액별 만드는데 드는 횟수 체크
    for j in range(money, M + 1):
        dp_table[j] = min(dp_table[j], dp_table[j - money] + 1)

if dp_table[M] == 99999999:
    print(-1)
else:
    print(dp_table[M])