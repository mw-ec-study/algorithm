#page 99
N, K = map(int, input().split())

count = 0

while True:
    if N == 1: #1이면 종료
        break
    elif N % K == 0: #N을 K로 나눈 나머지가 0이면
        N /= K
    else:
        N -= 1
    count += 1

print(count) 