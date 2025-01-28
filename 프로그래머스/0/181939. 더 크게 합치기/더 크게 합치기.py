def solution(a, b):
    temp_a = str(a)
    temp_b = str(b)
    answer_a = int(temp_a + temp_b)
    answer_b = int(temp_b + temp_a)

    if answer_b < answer_a:
        return answer_a
    elif answer_a < answer_b:
        return answer_b
    else:
        return answer_a