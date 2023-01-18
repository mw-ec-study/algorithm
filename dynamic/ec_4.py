def solution(num, coins:list):
    coins.sort(reverse=True)
    array = []
    last_index = 0
    
    while last_index != len(coins):
        for i in range(last_index, len(coins)):
            #가장 비싼 코인 먼저 채우기
            coin_count = num//coins[i]
            num -= coins[i] * coin_count
            
            if num == 0:
                array += [coins[i]]*coin_count
                return len(array)
            if num > 0:
                array += [coins[i]]*coin_count
                
        if not array:
            #코인이 가격보다 비쌀 경우
            return -1
        
        last_index += 1 #다음 코인
        array.pop(-1) #
        
    return -1
        
print(solution(3534, [5, 4]))

# num = 19
# coins = [5, 4]

# def solution(num, coins:list):
#     coins.sort(reverse=True)
#     array = []
#     last_index = 0
    
#     while last_index != len(coins):
#         for i in range(last_index, len(coins)):
#             #가장 비싼 코인 먼저 채우기
#             while num >= 0:
#                 num -= coins[i]
#                 if num == 0:
#                     array.append(coins[i])
#                     print(array)
#                     return len(array)
#                 elif num > 0:
#                     array.append(coins[i])
#                     print(array)
                    
#             num += coins[i] # 다시 복구(0보다 작아졌기 때문)
                
#         if not array:
#             #코인이 가격보다 비쌀 경우
#             return -1
        
#         last_index += 1 #다음 코인
#         array.pop(-1) #
        
#     return -1
        
# print(solution(3000, [3, 4]))
