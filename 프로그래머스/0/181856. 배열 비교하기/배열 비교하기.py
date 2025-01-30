def solution(arr1, arr2):
    temp_len1 = len(arr1)
    temp_len2 = len(arr2)
    
    sum_len1 = 0
    sum_len2 = 0
    
    if temp_len2 < temp_len1:
        return 1
    elif temp_len1 < temp_len2:
        return -1
    else:
        for i in range(0,temp_len1):
            sum_len1 = sum_len1 + arr1[i]
            sum_len2 = sum_len2 + arr2[i]
            
        if sum_len2 < sum_len1:
            return 1
        elif sum_len1 < sum_len2:
            return -1
        else:
            return 0