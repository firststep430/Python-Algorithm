def solution(arr):
    for i in range(len(arr)):
        if arr[i] < 50 and not arr[i] % 2 == 0:
            arr[i] = arr[i] * 2
        
        elif 50 <= arr[i] and arr[i] % 2 == 0:
            arr[i] = arr[i] / 2
    
    return arr
        