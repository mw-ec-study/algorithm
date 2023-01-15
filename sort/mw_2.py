N = int(input())

input_list = []
for _ in range(N):
    input_value = input().split()
    input_list.append([input_value[0], int(input_value[1])])

input_list.sort(key = lambda data:data[1])
for name in input_list:
    print(name[0], end = ' ')

