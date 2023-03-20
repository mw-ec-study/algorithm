def solution(s):
    answer = 10001
    split = 1
    
    while split <= len(s) / 2:
        cur_s_len = 0 # 현재 문자 길이
        cur = s[:split] # 현재 문자
        count = 1 # 중복된 문자 개수
        next_s = 0 # 다음 문자
        
        for i in range(split, len(s), split):
            next_s = s[i:i+split] # 다음 문자
            if cur == next_s: # 다음 문자와 현재 문자가 같으면
                count += 1 # 중복 + 1
            else: # 다르면 
                if count > 1: # 이전 중복 처리
                    cur_s_len += len(str(count)) + split
                else:
                    cur_s_len += split
                count = 1
            cur = next_s
            
        if count > 1:
            cur_s_len += len(str(count)) + split
        else:
            cur_s_len += len(next_s) # 남은 문자 처리
            
        answer = min(answer, cur_s_len)
        split += 1
    
    return answer if answer != 10001 else len(s)

print(solution("aaaaaaaaaaaabcd"))