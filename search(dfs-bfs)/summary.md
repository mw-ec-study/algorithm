# BFS/DFS

---

## 탐색

---

**탐색**이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다.

대표적인 탐색 알고리즘으로 DFS/BFS를 꼽을 수 있는데 이 두 알고리즘은 기본 자료구조인 **스택**과 **큐**에 대한 이해가 전제 되어야 하므로 사전 학습으로 스택과 큐, 재귀 함수를 간단히 알아보자.

## 스택

---

스택은 **선입후출** 구조 또는 **후입선출** 구조라고 한다.

python에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요가 없다.

기본 리스트에서 `append()` 와 `pop()` 메서드를 이용하면 스택 자료구조와 동일하게 동작한다.

```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack) #1, 2, 3

stack.pop() #가장 뒤쪽에 있는 데이터를 꺼냄

print(stack) #1, 2
```

## 큐

---

큐는 **선입선출** 구조라고 한다.

python에서는 `collections` 의 `deque` 를 이용한다.

```python
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(list(queue)) #1, 2, 3

queue.popleft() #가장 앞에 있는 데이터를 꺼냄

print(list(queue)) #2, 3
```

## DFS

**DFS**는 Depth-First-Search, “깊이 우선 탐색”이라고도 부르며, *그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

> 그래프는 **노드(Node)**와 **간선(Edge)**으로 표현되며 이때 노드를 **정점(Vertex)**이라고도 말한다.
- 인접 행렬: 2차원 배열로 그래프의 연결 관계를 표현하는 방식
- 인접 리스트: 리스트로 그래프의 연결 관계를 표현하는 방식
> 
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를  스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2 번 과정을 더 이상 수행할 수 없을 때까지 반복한다.

### DFS 예제

```python
def dfs(graph, v, visited):
		# 현재 노드 방문 처리
		visited[v] = True
		print(v, end=' ')
		# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
		for i in graph[v]:
            if not visited[i]:
                    dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문한 정보 리스트
visited = [False] * 9

dfs(graph, 1, visited)
```

## BFS

**BFS** 알고리즘은 “너비 우선 탐색” 이라는 의미를 가지며 쉽게 말해 가까운 노드부터 탐색하는 알고리즘이다. DFS는 최대한 멀리 있는 노드를 우선 탐색하는 방식이고 그 반대로 BFS는 큐 자료구조를 이용하여 가장 가까운 노드부터 방문한다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.

BFS는 큐 자료구조에 기초한다는 점에서 구현이 간단하다. `deqeq` 라이브러리를 사용하는 것이 좋으며 탐색을 수행할 경우 O(N)의 시간이 소요된다. 일반적인 경우 실제 수행 시간은 DFS보다 좋은 편이다.

```python
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")
        for node in graph[current_node]:
            if not visited[node]:            
                queue.append(node)
                visited[node] = True
```

## 정리

---

|  | DFS | BFS |
| --- | --- | --- |
| 동작 원리  | 스택 | 큐 |
| 구현 방법 | 재귀 함수 이용 | 큐 자료구조 이용 |s