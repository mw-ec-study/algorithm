#page 321 (럭키 스트레이트)
n = input()
left = 0
right = 0
center = len(n)//2
for i in range(len(n)):
    if i < center:
        left += int(n[i])
    else:
        right += int(n[i])

if left == right:
    print('LUCKY')
else:
    print('READY')
