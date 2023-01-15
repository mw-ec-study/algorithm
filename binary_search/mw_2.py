N, M = map(int, input().split())
tteok = list(map(int, input().split()))
tteok.sort()

def binary_search(data, start, end, find_value):
    res = 0
    
    while start <= end:
        tteok_length = 0
        middle = (start+end)//2 #중간 지점 = 기계 설정 높이값 

        for value in data:
            if value > middle: #중간지점 길이보다 길면 
                tteok_length += value - middle #자른 길이 추가

        if tteok_length == find_value: #자른 떡의 총 길이 = 요청길이
            return middle

        elif tteok_length < find_value: #자른 떡의 총 길이 < 요청길이 이면 
            end = middle - 1 #중간값을 더 줄여서 자르는 길이를 늘림 (왼쪽 탐색)

        else:
            start = middle + 1 #중간값을  더 늘려 자르는 길이를 줄임 (오른쪽 탐색)
            res = middle #요청길이 보다 조금 넘더라도 최소값이 필요

    return res

print(binary_search(tteok, 0, tteok[N-1], M)) #떡 길이 정보, 시작, 떡 길이중 가장 긴 것, 요청 길이
        

