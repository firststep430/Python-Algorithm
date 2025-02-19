def solution(x):
    temp = []
    sum = 0
    for char in str(x):
        temp.append(char)
    
    for i in range(len(temp)):
        sum = sum + int(temp[i])
    
    if x % sum == 0:
        return True
    else:
        return False