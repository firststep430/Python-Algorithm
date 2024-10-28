def solution(n):
    answer_array = []
    
    for i in range(1, n+1):
        if i % 2 != 0:
            answer_array.append(i)
    
    return answer_array