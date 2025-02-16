def solution(s):
    s = s.lower()
    count_p = 0
    count_y = 0
    
    for char in s:
        if char == "p":
            count_p = count_p + 1
        if char == "y":
            count_y = count_y + 1
        
    return count_p == count_y