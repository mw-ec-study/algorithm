def binary_search(data, start, end, find_value):
    while start <= end:
        middle = (start + end) // 2 #중간점 
        if data[middle] == find_value: #찾음 
            return True
        elif data[middle] > find_value: #중간점 기준 왼쪽을 탐색
            end = middle - 1
        else: #오른쪽 탐색
            start = middle + 1
    return False


N = int(input())
input_1 = list(map(int, input().split()))
M = int(input())
input_2 = list(map(int, input().split()))

input_1.sort() #이진 탐색을 위해 오름차순 정렬

for find_value in input_2:
    res = binary_search(input_1, 0, N - 1, find_value)
    if res:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

'''
대체 이진탐색을 왜쓰는 것인가?

N = int(input())
input_1 = list(map(int, input().split()))
M = int(input())
input_2 = list(map(int, input().split()))

for find_value in input_2:
    if find_value in input_1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
'''
