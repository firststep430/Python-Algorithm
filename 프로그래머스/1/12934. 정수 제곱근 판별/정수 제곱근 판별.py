import math

def solution(n):
    temp = math.sqrt(n)
    
    if not temp.is_integer():
        return -1
    else:
        return (temp+1)**2