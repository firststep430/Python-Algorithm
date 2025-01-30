def solution(strArr):
    temp = []
    answer = []
    for i in range(len(strArr)):
        if not "ad" in strArr[i]:
            temp.append(i)
        else:
            pass
        
    for i in temp:
        answer.append(strArr[i])

    return answer