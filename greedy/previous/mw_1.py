#page 311 (모험가 길드)
n = int(input())
people = list(map(int, input().split()))
people.sort()

count_p = 1 #그룹에 모인 사람 수
count_g = 0 #완성된 그룹 수

for person in people:
    if person <= count_p:
        count_g += 1
        count_p = 1
    else:
        count_p += 1

print(count_g)