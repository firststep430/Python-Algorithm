def solution(n, numlist):
    answer = []
    
    for i in range(len(numlist)):
        if numlist[i] % n == 0:
            temp = numlist[i]
            answer.append(temp)
            
    return answer