def solution(n):
    less = []
    temp = 0
    while not n==0:
        temp = n%3
        less.append(temp)
        n = n//3
    
    less = less[::-1]
    
    answer = 0
    
    for i, digit in enumerate(less):
        answer = answer + digit*(3**i)
        
    return answer