nums = [1, 1, 2, 3, 9]
nums.sort(reverse=True)

i = 1
while True:
    n = i
    for num in nums:
        n -= num
        if n == 0: break
        elif n < 0: n += num
    if n > 0:
        break
    i += 1
    
print(i)
