def solution(numbers):
    numbers.sort()
    temp = len(numbers)
    
    answer1 = numbers[temp-1] * numbers[temp-2]
    answer2 = numbers[0] * numbers[1]

    return max(answer1, answer2)