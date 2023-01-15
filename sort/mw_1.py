N = int(input())

input_list = []

for i in range(N):
    input_list.append(int(input()))

input_list.sort(reverse=True)
print(input_list)