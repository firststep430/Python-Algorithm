def solution(n):
    total = 0
    while n:
        total = total + (n % 10)
        n = n // 10
            
            
    return total