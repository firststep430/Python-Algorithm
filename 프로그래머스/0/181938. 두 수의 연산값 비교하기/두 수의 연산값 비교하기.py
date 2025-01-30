def solution(a, b):
    temp_A = str(a) + str(b)
    temp_B = 2*a*b
    
    if temp_B < int(temp_A) or temp_B == int(temp_A) :
        answer = int(temp_A)
        return answer
    else:
        answer = temp_B
        return answer
    
    