count = 0 #반복한 횟수
min_count = 999999999 #최소 개수

'''
나눠지는 숫자에 있는 계산 횟수+1(2, 3, 5 중에서 나눠짐) vs 전 숫자 횟수+1(그냥 +1)
'''

def counter(x, count):
    global min_count
    
    if count > min_count:
        #이미 반복한 횟수가 최소값을 넘었다면 return
        return
    
    if x == 1:
        #x가 1이면 최소값 갱신
        if count < min_count:
            min_count = count
    
    count += 1
    if x%2 == 0:
        counter(x//2, count)
    if x%5 == 0:
        counter(x//5, count)
    if x-1 > 0:
        counter(x-1, count)
    if x%3 == 0:
        counter(x//3, count)
    
x = 30000
counter(x, 0)
print(min_count)

# print(count)