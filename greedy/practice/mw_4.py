#page 314 (만들 수 없는 금액)
n = int(input())
money = list(map(int, input().split()))
money.sort()

result = 1 #1원부터 만들 수 없으면 답은 1
# money : 1 1 2 3 9 
# result : 1 2 3 5 8
for i in money:
    if i > result:
        break
    result += i

print(result)