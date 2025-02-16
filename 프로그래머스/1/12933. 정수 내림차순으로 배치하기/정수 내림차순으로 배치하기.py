def solution(n):
    answer = ""
    
    temp = [int(digit) for digit in str(n)]
    
    temp.sort(reverse=True)
    
    for i in range(len(temp)):
        answer = answer + str(temp[i])
    
    return int(answer)