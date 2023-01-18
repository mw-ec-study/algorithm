n = 20
answer = 0
tiles = [1, 2, 3] # 1 - 2*1, 2 - 1*2, 3 - 2*2

def solution(pre, index):
    global answer
    if index == n:
        answer += 1
        return
    
    if pre > 1: #전에 있는 타일의 사이즈가 2일 때 현재 타일 건너뜀
        solution(0, index+1)
        
    elif pre <= 1: #전에 있는 타일의 사이즈가 1일 때 1, 길이를 초과하지 않으면 2, 3도 가능
        solution(1, index+1)
        if index+1 == n:
            return
        solution(2, index+1)
        solution(3, index+1)

for t in tiles:
    solution(t, 1)

print(answer%796796)

# n = 7
# answer = 0
# tiles = [1, 2, 3] # 1 - 2*1, 2 - 1*2, 3 - 2*2

# def solution(array, index):
#     global answer
#     if index == n:
#         answer += 1
#         return
    
#     if array[index-1] > 1:
#         #전에 있는 타일의 사이즈가 2일 때 현재 타일은 -1로 마킹
#         solution(array, index+1)
        
#     elif array[index-1] <= 1:
#         #전에 있는 타일의 사이즈가 1일 때 1 길이를 초과하지 않으면 2, 3
        
#         array[index] = 1
#         solution(array.copy(), index+1)
#         if index+1 == len(array):
#             return
#         array[index] = 2
#         solution(array.copy(), index+1)
#         array[index] = 3
#         solution(array.copy(), index+1)

# for t in tiles:
#     array = [0]*n
#     array[0] = t
#     solution(array.copy(), 1)

# print(answer%796796)
    
    
