def solution(rny_string):
    for my in rny_string:
        rny_string = rny_string.replace("m", "rn")
    return rny_string