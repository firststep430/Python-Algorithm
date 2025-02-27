def solution(price, money, count):
    sum_t = 0
    answer = 0
    for i in range(1, count + 1):
        sum_t = sum_t + price*i
    
    if money <= sum_t:
        answer = sum_t - money
        return answer
    else:
        return 0