def solution(arr, divisor):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
        else:
            pass
    
    if len(answer) != 0:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer