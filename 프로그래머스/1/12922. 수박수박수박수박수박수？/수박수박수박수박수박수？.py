def solution(n):
    temp_odd = "박"
    temp_even = "수"
    answer = ""
    for i in range(n):
        if i % 2 != 0:
            answer = answer + temp_odd
        else:
            answer = answer + temp_even
        
    return answer