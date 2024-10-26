def solution(array):
    temp = 0
    length = range(len(array) - 1)
    
    array.sort()
    
    half = len(array) // 2
    
    # 짝수
    if len(array) % 2 == 0:
        answer = ( array[half-1] + array[half] ) / 2
        return answer 
    
    # 홀수
    else:
        answer = array[half]
        return answer
    
    
    