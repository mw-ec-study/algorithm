#page 113
n, m = map(int, input().split()) #map size
character = list(map(int, input().split()))

# _map = [          #테스트 입력 귀찮아서 만듬
#     [1,1,1,1],
#     [1,0,0,1],
#     [1,1,0,1],
#     [1,1,1,1]
# ] 

_map = []

for i in range(n):
    _map.append(list(map(int, input().split())))

visit_count = 1
check_count = 0

character_x = character[0]
character_y = character[1]
current_look = character[2]

_map[character_x][character_y] = 1004

def look():
    global current_look
    if current_look == -1 : current_look = 3
    if current_look == 0 : return [0, -1]
    if current_look == 1 : return [1, 0]
    if current_look == 2 : return [0, 1]
    else: return [-1, 0]

while True:
    moving = look()
    if check_count == 4:
        if _map[character_x - moving[0]][character_y - moving[1]] == 1: #바다
            break
        elif character_x - moving[0] < 0 or character_x - moving[0] > m or character_y - moving[1] < 0 or character_y - moving[1] > n:
            #맵을 벗어나면
            break
        else:
            #뒤로 이동
            character_x -= moving[0]
            character_y -= moving[1]
            _map[character_x][character_y] = 1004 #방문처리

        check_count = 0

    else:
        if character_x + moving[0] < 0 or character_x + moving[0] > m or character_y + moving[1] < 0 or character_y + moving[1] > n:
            #맵을 벗어나면
            current_look -= 1
            check_count += 1
        elif _map[character_x + moving[0]][character_y + moving[1]] != 0:
            #이미 갔던곳이나 바다면
            current_look -= 1
            check_count += 1 
        else:
            character_x += moving[0]
            character_y += moving[1]
            _map[character_x][character_y] = 1004
            visit_count += 1
            check_count = 0

print(visit_count)