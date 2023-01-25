#page 259
N, M = map(int, input().split())

routes = [[int(1e9)] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    com_1, com_2 = map(int, input().split())
    routes[com_1][com_2], routes[com_2][com_1] = 1, 1 #직접 연결된 노드 끼리의 거리는 1 

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            routes[i][j] = 0 #자기 자신에게 가는 거리는 0 

X, K = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            routes[j][k] = min(routes[j][k], routes[j][i] + routes[i][k]) #중간 노드를 거치는것과 그렇지 않은 것을 비교

res = routes[1][K] + routes[K][X]

if res < int(1e9):
    print(res)
else:
    print(-1)