def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    parent[max(a, b)] = min(a, b)

n, m = map(int, input().split())
result = 0
edges = []

for _ in range(m):
    a, b, c = map(int, input().split()) #a -> b 유지비용: c
    edges.append((c, a, b))

parent = [i for i in range(n+1)]

edges.sort()
max_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost) #가장 비싼 도로를 제거

