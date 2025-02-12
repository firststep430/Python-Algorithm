def solution(num_list):
    num_list.insert(0,0)
    temp1 = 0
    temp2 = 0
    for i in range(0, len(num_list), 2):
        temp1 += num_list[i]
    
    for j in range(1, len(num_list), 2):
        temp2 += num_list[j]
        
    if temp1 < temp2:
        return temp2
    elif temp2 < temp1:
        return temp1
    else:
        return temp1