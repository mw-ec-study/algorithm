## 그래프란?

그래프란 노드와 노드사이에 연결된 간선의 정보를 가지고 있는 자료구조를 의미한다. 
알고리즘 문제를 접했을 때 ‘서로 다른 개체 (혹은 객체)가 연결되어 있다’는 이야기를 들으면 가장 먼저 그래프 알고리즘을 떠올려야 한다. 예를 들어 ‘여러 개의 도시가 연결되어 있다’와 같은 내용이 등장하면 그래프 알고리즘을 의심해보자.

- 인접 행렬: 2차원 배열을 사용하는 방식
- 인접 리스트: 리스트를 사용하는 방식

|  | 공간 | 시간 |
| --- | --- | --- |
| 인접 행렬 | $O(V^2)$ | $O(1)$ |
| 인접 리스트 | $O(E)$ | $O(V)$ |

> 노드의 개수 V, 간선의 개수 E
> 

### 서로소 집합

수학에서 **서로소 집합**이란 공통 원소기 없는 두 집합을 의미한다.
예를 들어 {1, 2}와 {3, 4}는 서로소 관계이다. 반면에 {1, 2}와 {2, 3}은 서로소 관계가 아니다.

서로소 집합 자료구조란 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조라고 할 수 있다. 서로소 집합 자료구조는 `union`과 `find` 이 2개의 연산으로 조작할 수 있다.

`union` 연산은 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 연산이다. `find` 는 특정한 원소가 속한 집합이 어떤 집합인지 알려주는 연산이다.

- union 1, 4
- union 2, 4
- union 2, 3
- union 5, 6

위의 연산을 그래프로 표현하면 아래와 같다. 

![union_graph.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e4f21acd-95af-45b6-b58f-662b5823f726/union_graph.png)

### union, find 연산 코드

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
```

### 서로소 집합을 활용한 사이클 판별

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    2. 루트 노드가 서로 같다면 사이클이 발생한 것이다.
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다.

```python
def find_parent(parent, x):
    if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
            parent[b] = a
    else:
            parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        print("사이클 발생")
        break
    else:
        union_parent(parent, a, b)

```

## 신장 트리

신장트리는 그래프 알고리즘 문제로 자주 출제되는 문제 유형이다. 기본적으로 신장 트리란 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/55befb42-a2d7-4702-b2a5-1411ff34102d/Untitled.png)

## 크루스칼 알고리즘

우리는 다양한 문제 상황에서 가능한 최소한의 비용으로 신장 트리를 찾아야 할 때가 있다.

신장 트리 중에서 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘을 ‘최소 신장 트리 알고리즘’이라고 한다. 대표적인 최소 신장 트리 알고리즘으로는 **크루스칼 알고리즘**이 있다.

먼저 모든 간선에 대하여 정렬을 수행한 뒤에 가장 거리가 짧은 간선부터 집합에 표함시키면 된다. 이때 사이클을 발생시킬 수 있는 간선의 경우, 집합에 포합시키지 않는다.

1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    1. 사이클이 발생하지 않을 경우 최소 신장 트리에 포함시킨다.
    2. 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3. 모든 간선에 대하여 2번의 과정을 반복한다.

### 코드

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print("최소 비용: ", result)
```

## 예제 - 팀 결성

- 첫째 줄은 팀 개수 N과 연산 개수 M이 입력된다.
- M개의 줄에는 ‘팀 합치기’ 연산은 0, a, b 형태로 주어지고 ‘같은 팀 여부 확인’은 1, a, b 형태로 주어진다.
- 같은 팀 여부 확인 연산에 대하여 한 줄에 하나씩 YES, NO로 결과를 출력한다.

```python
[입력 예시]
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
```

### 코드

```python
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[max(a, b)] = min(a, b)

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
for _ in range(m):
    func, a, b = map(int, input().split())
    if func == 0:
        #union
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
```