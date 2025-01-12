def solution(rsp):
    answer = ""
    one_text = ""
    for i in range(len(rsp)):
        one_text = rsp[i]
        if one_text == "2":
            answer = answer + "0"
        elif one_text == "0":
            answer = answer + "5"
        elif one_text == "5":
            answer = answer + "2"
        else:
            pass
        
    return answer