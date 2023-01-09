'''p115'''
def solution(location):
    answer = 0
    x, y = eng_to_num(location[0]), int(location[1])
    steps = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, -2), (-2, 1)
    ]
    
    for step in steps:
        next_row = x + step[0]
        next_col = y + step[1]
        if 0 < next_row < 9 and 0 < next_col < 9:
            answer += 1

    print(answer)
    
def eng_to_num(e):
    table = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8} 
    return table[e]

solution("a1")