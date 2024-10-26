import math

def solution(numer1, denom1, numer2, denom2):
    
    temp_denom = denom1 * denom2
    temp_numer = numer1 * denom2 + numer2 * denom1
    
    #최대 공약수 구하기
    temp_gcd = math.gcd(temp_numer, temp_denom)
    

    answer_numer = temp_numer // temp_gcd
    answer_denom = temp_denom // temp_gcd
    
    answer = [answer_numer, answer_denom]
    
    return answer
