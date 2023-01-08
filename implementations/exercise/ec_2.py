def solution(current, map, n, m):
    answer = 0
    
    direc = current[2]
    a = current[0]
    b = current[1]
    rotation_count = 0
    
    while True:
        if direc == 4: direc = 0
        directions = get_direction(direc)
        
        if rotation_count == 4:
            # 이미 전부 4 방향을 본 상황
            rotation_count = 0
            
            next_a = a + directions[0] * -1
            next_b = b + directions[1] * -1
            
            # 4 뱡향을 모두 보고 뒤로 갔을 때
            if next_a < 0 or next_a > n or next_b < 0 or next_b > m:
                # 벽일 경우
                break
            elif map[next_a][next_b] == 1:
                # 바다일 경우
                break
            else:
                # 뒤로 가기
                map[a][b] = 2
                a = next_a
                b = next_b
                answer += 1
        
        elif 0 > (a + directions[0]) or (a + directions[0]) >= n \
            or 0 > (b + directions[1]) or (b + directions[1]) >= m:
                # 벽인 경우 회전 횟수 + 1, 다음 방향
                rotation_count += 1
                direc += 1
                
        elif map[a + directions[0]][ b + directions[1]] != 0:
            # 바다나 이미 지나왔던 경로라면 회전 횟수 + 1, 다음 방향
            rotation_count += 1
            direc += 1
            
        elif map[a + directions[0]][b + directions[1]] == 0:
            # 지나갈 수 있는 방향
            rotation_count = 0
            map[a][b] = 2 # 마킹
            a += directions[0]
            b += directions[1]
            answer += 1
            
    print(answer)
        
def get_direction(direction):
    table = {
        0: (-1, 0), #북
        1: (0, -1), #서
        2: (1, 0), # 남
        3: (0, 1), # 동
    }
    return table[direction]
        

map = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]

solution((1,1,0), map, n=4, m=4)