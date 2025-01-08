import math

def solution(n):
    temp = math.sqrt(n)
    if temp.is_integer():
        return 1
    else:
        return 2