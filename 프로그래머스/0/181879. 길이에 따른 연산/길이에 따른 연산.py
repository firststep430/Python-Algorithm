def solution(num_list):
    answer11 = 0
    answer10 = 0
    if len(num_list) > 10:
        for i in range(len(num_list)):
            answer11 = answer11 + num_list[i]
        return answer11
    
    elif len(num_list) < 11:
        for i in range(len(num_list)):
            if answer10 == 0:
                answer10 = num_list[i]
            else:
                answer10 = answer10 * num_list[i]
        return answer10