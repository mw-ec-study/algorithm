'''p149'''
map = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
]

def solution(map):
    answer = 0
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                dfs(i, j)
                print_map()
                answer += 1
                
    print(answer)

def dfs(i, j):
    if 0 <= i < len(map) and 0 <= j < len(map[0]) and map[i][j] == 0:
        map[i][j] = 1
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i-1, j)
        dfs(i+1, j)
        
def print_map():
    print(map[0])
    print(map[1])
    print(map[2])
    print(map[3])
    print()

solution(map)