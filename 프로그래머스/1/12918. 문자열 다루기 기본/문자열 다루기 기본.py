def solution(s):
    if len(s) == 4 or len(s) == 6:
        for char in s:
            if char not in "0123456789":
                return False
        return True
    return False
