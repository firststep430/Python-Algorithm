def solution(phone_number):
    temp = len(phone_number)
    back = phone_number[-4:]
    return "*"*(temp-4) + back