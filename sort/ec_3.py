def solution(k, a:list, b:list):
    a.sort()
    b.sort(reverse=True)
    a[:k], b[:k] = b[:k], a[:k]
    return sum(a)

print(solution(3, [1,2,5,4,3], [5,5,6,6,5]))