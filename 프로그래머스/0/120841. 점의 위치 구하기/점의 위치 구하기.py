def solution(dot):
    if dot[0] > 0:
        if dot[1] > 0:
            return 1
        elif 0 > dot[1]:
            return 4
    elif 0 > dot[0]:
        if dot[1] > 0 :
            return 2
        elif 0 > dot[1]:
            return 3
        