def solution(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    
    answer = sum / len(arr)
    
    return answer