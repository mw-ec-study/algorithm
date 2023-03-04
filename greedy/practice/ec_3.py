s = input()

a0 = len(s) - len(s.replace("01", "2"))
a1 = len(s) - len(s.replace("10", "2"))

if s[-1] == 0:
    a0 += 1
else:
    a1 += 1
    
print(min(a0, a1))
