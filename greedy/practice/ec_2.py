s = input()
answer = 0

for str in s:
    answer = max(answer+int(str), answer*int(str))
    
print(answer)
    