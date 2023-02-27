#page 315 (볼링공 고르기)
n,m = map(int, input().split())
ball = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i, n):
        if ball[i] != ball[j]:
            result += 1
print(result)
