def solution(numbers, k):
    point = 0
    count = 1
    
    temp = len(numbers)
    
    while count < k:
            point = (point + 2) % temp
            count = count + 1
                
    answer = numbers[point]
    
    return answer