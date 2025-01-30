def solution(arr, n):
    temp_len = len(arr)
    answer_arr = arr[:] 

    if temp_len % 2 == 0:
        for i in range(1, temp_len, 2):
            answer_arr[i] += n
    else:  
        for i in range(0, temp_len, 2):
            answer_arr[i] += n

    return answer_arr