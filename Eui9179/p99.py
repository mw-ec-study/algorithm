'''1이 될 때까지'''

def solution(num, k):
    answer = 0
    while num != 1:
        if num % k != 0:
            num -= 1
        else:
            num //= k
        answer += 1
    return answer
    
print(solution(100, 4))