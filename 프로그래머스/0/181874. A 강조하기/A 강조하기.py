def solution(myString):
    myString = myString.lower()
    
    if "a" in myString:
        result = myString.replace("a", "A")
    else:
        result = myString
    
    return result