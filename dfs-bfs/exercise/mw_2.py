'''
list와 달리 deque는 맨앞, 맨뒤 pop 연산시 시간복잡도 O(1)로 효율적임
'''
from collections import deque
# N, M = map(int, input().split())

# array = []

# for i in range(N):
#     array.append(list(map(int, input())))

N, M = 5, 6
array = [
    [ 1, 0, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 0, 1],
    [ 0, 0, 0, 0, 1, 1],
    [ 1, 1, 1, 1, 1, 1],
    [ 1, 1, 1, 1, 1, 1],
]

direction = [[-1,0], [1,0], [0,-1], [0,1]]
def solution(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for direct in direction: #상 하 좌 우 체크
            check_x = x + direct[0]
            check_y = y + direct[1]

            if check_x < N and check_x >= 0 and check_y < M and check_y >= 0 and array[check_x][check_y] == 1:
                queue.append([check_x, check_y])
                array[check_x][check_y] = array[x][y] + 1
    print(array)
    print(array[N-1][M-1])

solution(0, 0)