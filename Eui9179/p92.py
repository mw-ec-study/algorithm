# 큰 수의 법칙

def solution(nums:list, k:int, m:int):
    nums.sort()
    max1 = nums[-1]
    max2 = nums[-2]
    max2_count = m // (k + 1)
    
    result = (max1 * (m - max2_count)) + (max2 * max2_count)
    
    print(result)

nums = [2, 4, 5, 4, 6]
k = 2 #연속해서 더할 수 있는 횟수
m = 9 #더할 횟수

solution(nums, k, m)