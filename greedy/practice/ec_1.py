# 실전 문제
n = int(input())
people = list(map(int, input().split()))

i = 0
answer = 0

people.sort()

for person in people:
    i += person
    if (i <= n):
        answer += 1

print(answer)