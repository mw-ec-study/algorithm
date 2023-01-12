'''p152'''
from collections import deque

movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(start, n, m):
    answer = 0
    
    q = deque([start])
    map[start[0]][start[1]] = 0
    last_node = list(q[-1])
    
    while q:
        path = q.popleft()
        
        if path[0] == n and path[1] == m:
            return answer + 1
        
        for move in movements:
            next_path = (path[0]+move[0], path[1]+move[1])
            if not 0 < next_path[0] <= n or not 0 < next_path[1] <= m:
                continue
            
            if map[next_path[0]][next_path[1]] == 1:
                q.append(next_path)
                map[next_path[0]][next_path[1]] = 0
    
        if not last_node in list(q):
            last_node = list(q)[-1]
            answer += 1
            
map = [
    [-1, -1, -1, -1, -1, -1],
    [-1, 1, 1, 0, 0, 1, 0],
    [-1, 0, 1, 0, 1, 1, 1],
    [-1, 1, 1, 0, 0, 1, 0],
    [-1, 1, 0, 0, 1, 1, 1],
    [-1, 1, 1, 1, 1, 0, 1],
]


# map = [
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 1, 0, 1, 0, 1, 0],
#     [-1, 1, 1, 1, 1, 1, 1],
#     [-1, 0, 0, 0, 0, 0, 1],
#     [-1, 1, 1, 1, 1, 1, 1],
#     [-1, 1, 1, 1, 1, 1, 1],
# ]

# map = [
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 1, 1, 0, 1, 1, 1],
#     [-1, 0, 1, 0, 1, 0, 1],
#     [-1, 1, 1, 0, 1, 0, 1],
#     [-1, 1, 0, 0, 1, 0, 1],
#     [-1, 1, 1, 1, 1, 0, 1],
# ]

print(solution((1, 1), 5, 6))