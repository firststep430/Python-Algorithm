def solution(n):
    n = str(n)
    temp = []
    for digit in n:
        temp.append(digit)
    
    temp.reverse()
    
    temp = [int(i) for i in temp]
    
    return temp