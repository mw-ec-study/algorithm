'''숫자 카드 게임'''
def solution(cards):
    answer = -1
    for row in cards:
        answer = max(min(row), answer)
    
    print(answer)

cards = [
    [3, 1, 2],
    [4, 1, 4],
    [2, 2, 2]
]

solution(cards)