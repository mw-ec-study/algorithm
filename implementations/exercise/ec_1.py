def solution(location):
    answer = 0
    x, y = eng_to_num(location[0]), int(location[1])
    nums = [
        (2, 1),
        (1, 2)
    ]

    for num in nums:
        if 0 < x + num[0] < 9 and 0 < y + num[1] < 9:
            answer += 1
        if 0 < x + num[0] < 9 and 0 < y - num[1] < 9:
            answer += 1
        if 0 < x - num[0] < 9 and 0 < y + num[1] < 9:
            answer += 1
        if 0 < x - num[0] < 9 and 0 < y - num[1] < 9:
            answer += 1
                
    print(answer)
    
def eng_to_num(e):
    table = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8} 
    return table[e]

solution("e5")