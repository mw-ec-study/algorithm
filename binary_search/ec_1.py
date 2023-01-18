def solution(hosts, clients):
   for c in clients:
       if c in hosts:
           print("yes", end=" ")
       else:           
           print("no", end=" ")
           
solution([8, 3, 7, 9, 2], [5, 7, 9])