#page 115
count = 0 
location = input()
moving_case = [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]

convert_input ={   #알파벳 인풋을 정수형 좌표로 
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : 5,
    'f' : 6,
    'g' : 7,
    'h' : 8
}

for moving in moving_case:
    #알파벳 좌표 + 수평 무빙 케이스
    if convert_input[location[0]] + moving[0] > 0:  
        #숫자 좌표 + 수직 무빙 케이스
        if int(location[1]) + moving[1] > 0:
            count += 1

print(count)
