def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0, n+1, 2):
            answer = answer + i**2
        return answer
    
    else:
        for i in range(1, n+1, 2):
            answer = answer + i
        return answer
    
