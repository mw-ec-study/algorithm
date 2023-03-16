#page 323 문자열 압축
'''
풀이 방법 요약

입력 문자마다 몇 자릿수를 기준으로 압축하는것이 가장 짧은지 구해야함.
자릿수를 (1~문자열 길이의 절반) 순서대로 늘려가며 최솟값을 비교

pattern의 디폴트 값 = 문자열의 첫글자부터 자릿수 만큼 지정

만약 'aabbaccc'를 두자릿수 패턴으로 압축하는것을 체크중이면 
pattern = 'aa' 이고 이와 동일한지 체크 하는 부분은 'bb'가 된다 <- 두번째 루프에서 체크하는 방식.
동일할경우 count + 1 다를 경우 pattern을 'bb'로 재설정하게된다.
'''

def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1): #패턴을 자릿수를 늘려가며 체크 단, 문자열의 중간지점까지 
        count = 1
        pattern = s[0:i] #i 자릿수 만큼의 패턴 
        compressed = '' 

        for j in range(i, len(s), i): 
            if pattern == s[j:j + i]: #패턴과 일치하면
                count += 1
            else:
                if count >= 2: #count 2이상 일때 카운트 + pattern 으로 압축
                    compressed += str(count) + pattern
                else: #pattern만 다시 적어줌
                    compressed += pattern

                pattern = s[j:j + i] #다음 패턴으로 초기화
                count = 1

        #남은 문자열 처리
        if count >= 2:
            compressed += str(count) + pattern
            
        else:
            compressed += pattern

        answer = min(answer, len(compressed)) #이전 자릿수 압축의 결과와 현재 자릿수 압축의 결과중 더 작은것

    return answer

print(solution("aabbaccc")) #7
print(solution("ababcdcdababcdcd")) #9
print(solution("abcabcdede")) #8
print(solution("abcabcabcabcdededededede")) #14
print(solution("xababcdcdababcdcd")) #17