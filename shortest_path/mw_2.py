import heapq

N, M, C = map(int, input().split())

routes = [[] for _ in range(N + 1)]

distance = [int(1e9)] * (N + 1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    routes[X].append([Y, Z])

queue = []
heapq.heappush(queue, (0, C)) #시작 지점
distance[C] = 0

while queue:
    dist, node = heapq.heappop(queue)

    if distance[node] < dist:
        continue

    for route in routes[node]:
        cost = route[1] + dist #현재 노드를 거쳐 다른 노드로 이동 하는 거리
        if cost < distance[route[0]]:
            distance[route[0]] = cost
            heapq.heappush(queue, (cost, route[0]))

count = 0
far_from_node = 0
for dist in distance:
    if dist != int(1e9):
        count += 1
        far_from_node = max(dist, far_from_node)

print(count - 1, far_from_node)