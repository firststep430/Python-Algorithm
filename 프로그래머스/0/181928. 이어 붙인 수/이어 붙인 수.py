def solution(num_list):
    odd = ''
    even = ''
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            odd = odd + str(num_list[i])
            
        else:
            even = even + str(num_list[i])
        
    answer = int(odd) + int(even)
        
    return answer
    
    