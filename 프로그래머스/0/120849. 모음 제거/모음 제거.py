def solution(my_string):
    answer = ""
    
    for i in range(len(my_string)):
        char = my_string[i]
        
        if char in "aeiou":
            pass
        
        else:
            answer = answer + my_string[i]

    return answer