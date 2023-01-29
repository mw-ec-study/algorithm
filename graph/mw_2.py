n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

datas = []
res = 0
last = 0

for i in range(m):
    a, b, c = map(int, input().split())
    datas.append([a, b, c])

datas.sort(key = lambda x:x[2]) #비용 기준으로 오름차순 정렬

for data in datas:
    a, b, c = data
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += c
        last = c 

print(res - last)