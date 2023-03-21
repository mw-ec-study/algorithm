def print_arr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i][j], end=" ")
        print()
    print()

def rotate_key(key):
    n = len(key)
    new_key = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_key[j][n - 1 - i] = key[i][j]
    return new_key

def get_new_lock(key, lock):
    new_lock = [[0] * (len(lock) + 2 * (len(key) - 1)) for _ in range(len(lock) + 2 * (len(key) - 1))]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i + len(key) - 1][j + (len(key) - 1)] = lock[i][j]
    return new_lock

def check(lock, key, new_lock):
    for k in range(len(lock)):
        for l in range(len(lock)):
            if new_lock[len(key) - 1 + k][len(key) - 1 + l] != 1:
                return False
    return True

def solution(key, lock):
    new_lock = get_new_lock(key, lock)
    for _ in range(4):
        key = rotate_key(key)
        for i in range(len(new_lock) - (len(key) - 1)):
            for j in range(len(new_lock) - (len(key) - 1)):

                # 열쇠 넣기
                for k in range(len(key)):
                    for l in range(len(key)):
                        new_lock[i + k][j + l] += key[k][l]

                if check(lock, key, new_lock):
                    return True

                # 열쇠 빼기
                for k in range(len(key)):
                    for l in range(len(key)):
                        new_lock[i + k][j + l] -= key[k][l]
    return False

print(solution([[0, 1], [1, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

