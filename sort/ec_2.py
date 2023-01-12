def solution(stu:list):
    return sorted(stu, key=score)
    
    
def score(data):
    return data[1]

stu = [
    ("Lee", 55),
    ("joe", 70),
    ("kim", 33)
]
    

print([name[0] for name in solution(stu)])