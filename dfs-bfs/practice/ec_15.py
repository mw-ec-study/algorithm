n, m, k, x = map(int, input().split())

graph = {
    i: [] for i in range(n + 1)
}

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = []
visited = [False] * (n + 1)
node_in_cycle = {i: [] for i in range(k + 1)}
cycle = 0
cycle_count = 1

q.append(x)

while q:
    node = q.pop(0)
    cycle_count -= 1
    
    if not visited[node]:
        visited[node] = True
        q += graph[node]
        node_in_cycle[cycle].append(node)
    
    if cycle_count == 0:
        cycle += 1
        cycle_count = len(q)
    
    if cycle > k:
        break

if len(node_in_cycle[k]) == 0:
    print(-1)
else: 
    node_in_cycle[k].sort()
    for n in node_in_cycle[k]:
        print(n)