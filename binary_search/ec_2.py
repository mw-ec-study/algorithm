def solution(req, rcs):
    answer = 0
    end = max(rcs)
    start = 0
    
    while(start <= end):
        rc_sum = 0
        mid = (end + start)//2
        
        for rc in rcs:
            if rc > mid:
                rc_sum += rc - mid
                
        if rc_sum < req:
            end = mid - 1
        
        elif rc_sum > req:
            answer = mid
            start = mid + 1
        else:
            return mid
        
    return answer
        
print(solution(6, [19, 15, 10, 17]))