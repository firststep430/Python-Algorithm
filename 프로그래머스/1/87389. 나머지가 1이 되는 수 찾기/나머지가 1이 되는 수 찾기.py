def solution(n):
    result = 0
    for i in range(2, n, 1):
        if n % i == 1:
            result = i
            break
    return result