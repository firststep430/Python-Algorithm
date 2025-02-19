def solution(arr):
    temp = [-1]
    if len(arr) == 1:
        return temp
    else:
        min_value = min(arr)
        arr.remove(min_value)
        
        return arr
                
    
    