#못 품
dp = [0] * 100

storeges = [1, 3, 1, 5, 99]

dp[0] = storeges[0]
dp[1] = storeges[1]

for i in range(2, len(storeges)):
    dp[i] = max(storeges[i-1], storeges[i] + storeges[i-2])

print(dp[len(storeges)-1])