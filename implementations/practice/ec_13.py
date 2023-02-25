from itertools import combinations

def get_sum(candidates, house):
    result = 0
    
    for h in house:
        distance = 10 * n
        for candi in candidates:
            distance = min(
                abs(h[0] - candi[0]) + abs(h[1] - candi[1]),
                distance
            )
        result += distance
    return result

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))
print(candidates)

result = 1e9
for candi in candidates:
    result = min(result, get_sum(candi, house))
    
print(result)
    


    
