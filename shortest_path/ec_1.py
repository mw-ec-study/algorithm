'''p259'''
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#간선 입력        
for _ in range(m):
    #a와 b가 서로 가는 비용 1
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][k] + graph[k][x]
if answer >= INF:
    answer = -1
    
print(answer)