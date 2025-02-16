def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif b < a:
        while True:
            if a < b:
                break
            answer = answer + b
            b = b + 1
        return answer
    elif a < b:
        while True:
            if b < a:
                break
            answer = answer + a
            a = a + 1
        return answer