def solution(s):
    temp = len(s) % 2
    temp2 = len(s) // 2
    temp3 = ""
    if temp != 0: # 홀수
        return s[temp2]
    
    else: # 짝수
        temp3 = temp3 + s[temp2 - 1] + s[temp2]
        return temp3
        