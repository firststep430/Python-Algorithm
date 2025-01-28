import math

def solution(array):
    result = []
    result.append(max(array))
    
    for i in range(len(array)):
        if array[i] == max(array):
            result.append(i)
    
    return result