num = int(input())
num_str = str(num)
mid = int(len(num_str)/2)
left = sum(list([int(i) for i in num_str[:mid]]))
right = sum(list([int(i) for i in num_str[mid:]]))
if left == right:
    print("LUCKY")
else:
    print("READY") 