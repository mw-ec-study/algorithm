import heapq, sys

answer = ''
INF = 1e9

input = sys.stdin.readline

#도시의 개수 n, 통로의 개수 m, 메시지를 보내고자 하는 도시 c
n, m, c = map(int, input().split())

#m+1번째 줄에 걸쳐서 통로에 대한 정보 x,y,z가 주어진다.
#이는 특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 z라는 의미이다.
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (n+1)
distance[1] = 0

q = []
heapq.heappush(q, (0, c))

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for g in graph[now]:
        cost = g[1] + dist
        if cost < distance[g[0]]:
            distance[g[0]] = cost
            heapq.heappush(q, (cost, g[0]))

count = 0
time = 0
for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        time = max(distance[i], time)

print(str(count-1) + " " + str(time))