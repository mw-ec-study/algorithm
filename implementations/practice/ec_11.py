def solution(n, apples, move):
    board = [[0] * n for _ in range(n)]
    for apple in apples:
        board[apple[0]][apple[1]] = 5

    t = 0
    move_t = 0
    move_len = len(move)
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cur_direction = 0
    snake = [(0, 0)]

    while True:
        t += 1

        next_a = snake[-1][0] + directions[cur_direction][0]
        next_b = snake[-1][1] + directions[cur_direction][1]

        if (next_a, next_b) in snake:
            return t

        snake.append((next_a, next_b))

        if n <= snake[-1][0] or 0 > snake[-1][0] or n <= snake[-1][1] or 0 > snake[-1][1]:
            return t

        if board[snake[-1][0]][snake[-1][1]] != 5:
            snake.pop(0)
        else:
            board[snake[-1][0]][snake[-1][1]] = 0

        if move_t < move_len and t == move[move_t][0]:
            if move[move_t][1] == 'L':
                cur_direction -= 1
                if cur_direction < 0:
                    cur_direction = len(directions) - 1
            else:
                cur_direction += 1
                if cur_direction == len(directions):
                    cur_direction = 0
            move_t += 1


n = int(input())
k = int(input())
apples = []
move = []
for _ in range(k):
    a_a, a_b = map(int, input().split())
    apples.append((a_a - 1, a_b - 1))

l = int(input())
for _ in range(l):
    t, d = map(str, input().split())
    move.append((int(t), d))

print(solution(n, apples, move))