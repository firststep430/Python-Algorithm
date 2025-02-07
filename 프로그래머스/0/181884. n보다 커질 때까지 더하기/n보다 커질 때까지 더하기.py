def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        answer = answer + numbers[i]
        if n < answer:
            return answer
        else:
            pass