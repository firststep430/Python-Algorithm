import math

def solution(n):
    i = 0
    while True:
        temp = math.factorial(i)
        if temp > n:
            break
        i = i + 1
    
    return i - 1