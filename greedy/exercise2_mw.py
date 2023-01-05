#page 96
N, M = map(int, input().split())

res = 0 
for i in range(N):
    row = list(map(int, input().split()))
    lowest = min(row) #입력 받은 행에서 최소값
    if lowest > res: res = lowest #최소값중 가장 큰 값을 res에 저장
print(res)

