## 다익스트라 알고리즘

다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가능 각각의 최단 경로를 구해주는 알고리즘이다. 다익스트라 알고리즘은 ‘음의 간선’이 없을 때 정상적으로 동작한다.(음의 간선이란 0보다 작은 값을 가지는 간선을 의미)

현실 세계의 길은 음의 간선이 표현되지 않으므로 다익스트라 알고리즘은 실제로 GPS 의 기본 알고리즘으로 채택되곤 한다.

1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화 한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정 3, 4번을 반복한다.

다익스트라 알고리즘에서는 **우선순위 큐**를 사용한다. 파이썬에서 우선순위 큐가 필요할 때 `heapq` 를 사용한다. 일반적인 프로그래밍 언어에서는 우선순위 큐 라이브러리에 데이터 묶음을 넣으면 첫 번째 원소를 기준으로 우선순위를 설정한다. (가치, 물건)

또한 우선순위 큐를 구현할 때는 내부적으로 최소 힙 혹은 최대 힙을 이용한다. 최소 힙은 값이 낮은 데이터가 먼저 삭제되며, 최대 힙을 이용하는 경우 값이 큰 데이터가 먼저 삭제된다. 파이썬은 기본적으로 최소 힙으로 구현되어 있고 최대 힙을 이용하기 위해 가치에 `-` 부호를 붙여 사용하기도 한다.

```python
import heapq
import sys

INF = int(1e9)

#노드 개수
n = 6
#시작 노드
start = 0
#각 노드의 정보
graph = [[] for i in range(n+1)]
graph[0].append((1, 2))#(노드, 비용)
graph[0].append((2, 4))
graph[0].append((3, 1))

graph[1].append((2, 3))
graph[1].append((3, 2))

graph[2].append((1, 3))
graph[2].append((5, 5))

graph[3].append((2, 3))
graph[3].append((4, 1))

graph[4].append((2, 1))
graph[4].append((5, 2))

# #최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n)

def dijkstra(start):
    q = []
    #시작 노드 큐에 삽입
    heapq.heappush(q, (0, start))#(비용, 노드)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리되었다면 무시
        if distance[now] < dist:
            continue
        
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
print(distance)
```

## 전보

도시 c에서 보낸 메시지를 받은 도시 개수, 모두 메시지를 받는 데까지 걸리는 시간이 얼마?

```python
[입력 예시]
#도시 개수, 통로 개수, 도시 c
3 2 1 
#x y z: 도시 x -> 도시 y, 비용 z
1 2 4 
1 3 2
```

```python
[출력 예시]
2 4
```

### 소스 코드

```python
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
```

## 플로이드 워셜 알고리즘

---

**플로이드 워셜 알고리즘**은 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우에 사용할 수 있는 알고리즘이다.

각 단계에서는 해당 노드를 거쳐가는 경우를 고려한다. 
예를 들어 1번 노드에 대해서 확인할 때는 1번 노드를 중간에 거쳐가는 모든 경우를 고려하면 된다. 
a → b로 가는 경우와 a → 1 → b로 가는 경우 중 더 비용이 적은 길을 기록해 둔다. 다음으로 2번, 3번 .. n번까지 반복하면 된다.

$D_{ab} = min(D_{ab}, D_{ak} + D_{kb})$

### 소스코드

```python
INF = int(1e9)
n = 4

graph = [[INF]*n for _ in range(n)]

#자기 자신으로 가는 비용은 0
for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

graph[0][1] = 3
graph[0][3] = 5
graph[1][0] = 2
graph[1][2] = 6
graph[2][0] = 4
graph[2][3] = 3
graph[3][2] = 1

    
#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#출력
for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
```

### 미래 도시

1번 도시에서 k를 거쳐 x로 가는 최단 거리를 구하라

(연결되어 있는 도시는 모두 양방향이고 비용은 모두 1)

```python
[입력 예시]
(1 <= n, m <= 100)
#n, m
5 7
#연결되어 있는 도시 
1 2
1 3
1 4
2 4
3 4
3 5
4 5
#x, k
4 5
```

```python
[출력 예시]
3
```

### 소스코드

```python
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
```