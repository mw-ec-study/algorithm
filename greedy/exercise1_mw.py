# #page 92
N, M, K = map(int,input().split()) #첫줄
second_row = list(map(int, input().split())) #둘째줄
second_row.sort()

res = 0 #결과값
i = 0 #M번 만큼 반복을 위한 비교 변수

while True:
    for j in range(K):
        if i == 8: 
            break
        res += second_row[-1] #정렬한것에서 맨 뒤(제일 큰 수)
        i += 1
    if i == 8:
        break
    res += second_row[-2] #맨 뒤에서 두번째(두번째로 큰 수)
    i += 1

print(res)

