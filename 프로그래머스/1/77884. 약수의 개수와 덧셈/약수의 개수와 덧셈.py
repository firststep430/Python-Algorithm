def solution(left, right):
    answer = 0
    for i in range(left, right+1): #left 부터 right까지
        count = 0;
        for j in range(1, i+1):
            if i % j == 0: 
                count = count + 1;
        if count % 2 == 0:
            answer = answer + i
        if count % 2 != 0:
            answer = answer - i
    return answer
            