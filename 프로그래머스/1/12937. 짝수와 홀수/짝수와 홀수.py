def solution(num):
    if num % 2 == 0 or num == 0:
        return "Even"
    elif num % 2 != 0:
        return "Odd"