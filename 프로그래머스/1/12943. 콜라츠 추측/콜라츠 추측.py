def solution(num):
    count = 0
    while (num != 1 and count < 500):
        if num % 2 == 0:
            num = num // 2
            count = count + 1
        elif num % 2 != 0:
            num = num * 3 + 1
            count = count + 1
    
    if num == 1:
        return count

    else:
        return -1