def solution(d, budget):
    all_cost = 0
    count = 0
    for i in range(len(d)):
        all_cost = all_cost + d[i]
    
    if all_cost == budget:
        return len(d)
    elif all_cost < budget:
        return len(d)
    else:
        d.sort()
        for i in range(len(d)):
            budget = budget - d[i]
            if not budget < 0:
                count = count + 1
            if budget < 0:
                break
        return count