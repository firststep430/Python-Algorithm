def solution(myString, pat):
    answer = ""
    list_my = list(myString)
    for i in range(len(list_my)):
        if list_my[i] == "A":
            answer = answer + "B"
        
        elif list_my[i] == "B":
            answer = answer + "A"
    
    if pat in answer:
        return 1
    else:
        return 0
    
    
    